#!/usr/bin/env python3
"""Export approved resume variants to HTML, DOCX, and PDF.

Pipeline: Markdown -> HTML and Markdown -> DOCX via pandoc, then
HTML -> PDF via headless Chrome/Chromium (so the PDF matches the styled
HTML, including the print stylesheet). Falls back to LibreOffice Writer
(DOCX -> PDF) if no Chrome-family browser is available.

Only the variants in APPROVED are exported. The master resume is excluded
until its "Resume TODO Before Public Use" items are resolved (see
exports/README.md). This script never modifies resume content.

Usage:
  python3 scripts/export_resumes.py            # export all approved variants
  python3 scripts/export_resumes.py --only ai-operations-consultant
  python3 scripts/export_resumes.py --formats html,docx
  python3 scripts/export_resumes.py --stamp 2026-07

Dependencies: pandoc (system binary, or `pip install pypandoc-binary`);
for PDF: Chrome/Chromium (preferred) or LibreOffice with Writer.
Override PDF engine detection with RESUME_PDF_ENGINE=/path/to/browser.
"""

import argparse
import datetime
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RESUMES_DIR = REPO_ROOT / "resumes"
EXPORTS_DIR = REPO_ROOT / "exports"
CSS_FILE = Path(__file__).resolve().parent / "resume.css"

# Approved for export. Master resume intentionally excluded (unresolved TODOs).
APPROVED = [
    "ai-operations-consultant",
    "operations-manager",
    "project-manager",
    "customer-success",
    "digital-marketing",
]

FORMATS = ("html", "docx", "pdf")

CHROME_CANDIDATES = (
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
    "/opt/pw-browsers/chromium",
)


def find_pandoc() -> list[str]:
    """Return the pandoc invocation prefix, preferring the system binary."""
    if shutil.which("pandoc"):
        return ["pandoc"]
    try:
        import pypandoc  # noqa: PLC0415

        return [str(Path(pypandoc.get_pandoc_path()))]
    except Exception:
        sys.exit(
            "pandoc not found. Install it (apt install pandoc) "
            "or `pip install pypandoc-binary`."
        )


def find_pdf_engine() -> tuple[str, str] | None:
    """Return (kind, path) where kind is 'chrome' or 'soffice'."""
    override = os.environ.get("RESUME_PDF_ENGINE")
    if override:
        return ("chrome", override)
    for name in CHROME_CANDIDATES:
        path = name if Path(name).is_file() else shutil.which(name)
        if path:
            return ("chrome", path)
    for name in ("soffice", "libreoffice"):
        path = shutil.which(name)
        if path:
            return ("soffice", path)
    return None


def display_title(variant: str) -> str:
    return variant.replace("-", " ").title().replace("Ai ", "AI ")


def markdown_to_html(src: Path, out: Path, variant: str, pandoc: list[str]) -> None:
    header = out.with_suffix(".style.tmp")
    header.write_text("<style>\n" + CSS_FILE.read_text() + "\n</style>\n")
    try:
        subprocess.run(
            [
                *pandoc,
                str(src),
                "--standalone",
                "--include-in-header",
                str(header),
                "--metadata",
                f"pagetitle=Tyrone Nelms — {display_title(variant)}",
                "-o",
                str(out),
            ],
            check=True,
        )
    finally:
        header.unlink(missing_ok=True)


def run_captured(cmd: list[str]) -> None:
    """Run a command, surfacing captured stderr if it fails."""
    try:
        subprocess.run(cmd, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        stderr = e.stderr.decode(errors="replace") if e.stderr else str(e)
        sys.exit(f"command failed: {cmd[0]}\n{stderr}")


def html_to_pdf_chrome(browser: str, html: Path, pdf: Path) -> None:
    run_captured(
        [
            browser,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            f"--print-to-pdf={pdf}",
            "--no-pdf-header-footer",
            html.resolve().as_uri(),
        ]
    )


def docx_to_pdf_soffice(soffice: str, docx: Path) -> None:
    # soffice exits 0 even on failure; output existence is checked by caller.
    run_captured(
        [
            soffice,
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            str(EXPORTS_DIR),
            str(docx.resolve()),
        ]
    )


def export_variant(
    variant: str,
    formats: list[str],
    stamp: str,
    pandoc: list[str],
    pdf_engine: tuple[str, str] | None,
) -> list[Path]:
    src = RESUMES_DIR / f"{variant}.md"
    if not src.exists():
        sys.exit(f"missing source file: {src}")
    base = f"{variant}-{stamp}"
    outputs: list[Path] = []

    html_out = EXPORTS_DIR / f"{base}.html"
    docx_out = EXPORTS_DIR / f"{base}.docx"
    pdf_out = EXPORTS_DIR / f"{base}.pdf"

    need_html = "html" in formats or (
        "pdf" in formats and pdf_engine and pdf_engine[0] == "chrome"
    )
    need_docx = "docx" in formats or (
        "pdf" in formats and pdf_engine and pdf_engine[0] == "soffice"
    )

    if need_html:
        markdown_to_html(src, html_out, variant, pandoc)
        if "html" in formats:
            outputs.append(html_out)
    if need_docx:
        subprocess.run([*pandoc, str(src), "-o", str(docx_out)], check=True)
        if "docx" in formats:
            outputs.append(docx_out)

    if "pdf" in formats:
        if not pdf_engine:
            sys.exit(
                "no PDF engine found: install Chrome/Chromium or LibreOffice "
                "Writer, or set RESUME_PDF_ENGINE."
            )
        kind, path = pdf_engine
        # Remove any prior output so the existence check below can only
        # pass on a PDF produced by this run (soffice can fail silently).
        pdf_out.unlink(missing_ok=True)
        if kind == "chrome":
            html_to_pdf_chrome(path, html_out, pdf_out)
        else:
            docx_to_pdf_soffice(path, docx_out)
        if not pdf_out.exists() or pdf_out.stat().st_size == 0:
            sys.exit(f"PDF conversion produced no output for {variant}")
        outputs.append(pdf_out)
        # Clean up intermediates that weren't requested as outputs.
        if "html" not in formats and need_html:
            html_out.unlink(missing_ok=True)
        if "docx" not in formats and need_docx:
            docx_out.unlink(missing_ok=True)

    return outputs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", help="export a single variant by name")
    parser.add_argument(
        "--formats",
        default=",".join(FORMATS),
        help=f"comma-separated subset of {FORMATS}",
    )
    parser.add_argument(
        "--stamp",
        default=datetime.date.today().strftime("%Y-%m"),
        help="date stamp for filenames (default: current YYYY-MM)",
    )
    args = parser.parse_args()

    formats = [f.strip() for f in args.formats.split(",") if f.strip()]
    for f in formats:
        if f not in FORMATS:
            sys.exit(f"unknown format: {f} (choose from {FORMATS})")

    variants = [args.only] if args.only else APPROVED
    if args.only and args.only not in APPROVED:
        sys.exit(f"'{args.only}' is not in the approved export list: {APPROVED}")

    pandoc = find_pandoc()
    pdf_engine = find_pdf_engine() if "pdf" in formats else None
    EXPORTS_DIR.mkdir(exist_ok=True)

    all_outputs: list[Path] = []
    for variant in variants:
        outputs = export_variant(variant, formats, args.stamp, pandoc, pdf_engine)
        all_outputs.extend(outputs)
        print(f"{variant}: " + ", ".join(o.name for o in outputs))

    missing = [o for o in all_outputs if not o.exists()]
    if missing:
        sys.exit(f"expected outputs missing: {missing}")
    print(f"\n{len(all_outputs)} files in {EXPORTS_DIR.relative_to(REPO_ROOT)}/")


if __name__ == "__main__":
    main()
