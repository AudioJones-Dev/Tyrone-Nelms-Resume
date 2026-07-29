# Featured Systems Portfolio

This portfolio presents selected systems designed and developed by Tyrone Nelms. Maturity labels distinguish verified implementation from operational pilots, planning foundations, and conceptual frameworks.

## AJ Digital OS V1

**Category:** AI operations platform  
**Maturity:** Working local-first implementation with documented CLI and browser control surfaces  
**Repository:** https://github.com/AudioJones-Dev/AJ-DIGITAL-OS-V1

### Operating problem

AI-assisted work can become fragmented across chats, tools, files, and ungoverned automations. Operators need continuity, approval controls, durable history, recoverability, and visibility into what the system is doing.

### System response

AJ Digital OS V1 provides a local-first operating layer for:

- assistant and orchestrated workflows
- task and conversation persistence
- semantic memory indexing and retrieval
- run inspection and lifecycle tracking
- human approval queues
- governed execution and publishing
- deliverable routing by brand and status
- operator health checks and dashboards
- tool, integration, and model profile scaffolds

### Governance characteristics

The platform preserves explicit human review through draft, pending approval, approved, and published states. Assistant workflows do not bypass approval boundaries, tool permissions, or the governed run lifecycle.

### Evidence

The repository documents build and run commands, operator flows, CLI command groups, persistence paths, semantic memory behavior, deliverable lifecycle states, a terminal conversation shell, and a browser-based control surface.

---

## Florida Ramp & Lift FieldOps Platform

**Category:** Field-service and contractor operations platform  
**Maturity:** Operational pilot application with a separately preserved planning and governance foundation  
**Repositories:**  
https://github.com/AudioJones-Dev/FRL-CONTRACTOR-PORTAL  
https://github.com/AudioJones-Dev/florida-ramp-and-lift-ops

### Operating problem

Field-service operations require coordination across installers, office staff, customers, jobs, safety requirements, completion records, billing, and contractor performance. Fragmented information and manual handoffs reduce visibility and increase operational risk.

### System response

The pilot portal supports role-based workflows for field installers, office administrators, and client read-only status views. The platform includes:

- React and TypeScript user interface
- Node and Express application runtime
- Supabase authentication, Postgres, row-level security, and storage
- field-image tagging through a server-side AI proxy
- PDF exports for draft invoices, payslips, and performance summaries
- local demo mode and authenticated operational-pilot mode

### Operational foundation

The supporting operations-intelligence repository preserves:

- a canonical Universal Job Object
- an operational data dictionary
- job, client, work-order, scope, safety, and invoice schemas
- safety, job-handling, and completion-closeout SOPs
- automation specifications for PDF intake, dispatch summaries, and billing extraction
- crew onboarding and PPE guidance
- reusable prompts and sanitized sample data
- explicit human review gates for safety-sensitive and financial actions

### Design distinction

The planning repository is intentionally frozen and does not claim production deployment. The canonical application resides in the contractor-portal repository. This distinction prevents roadmap concepts from being represented as completed runtime behavior.

---

## HDIKIT

**Category:** Truth-state and evidence-governance protocol  
**Maturity:** Designed framework; broader implementation maturity should be described only where repository evidence supports it  
**Repository:** https://github.com/AudioJones-Dev/HDIKIT

### Operating problem

Humans and AI systems can convert incomplete information, inference, or unsupported confidence into recommendations and operational action.

### System response

HDIKIT is a repo-native truth-state protocol designed to help humans and AI agents:

- verify claims
- expose false confidence
- distinguish evidence from inference and assumption
- disclose uncertainty
- preserve decision traceability
- prevent unverified claims from becoming action

### Intended application

The protocol is relevant to AI governance, research, business memory, operational recommendations, implementation plans, documentation, and agent-generated outputs.

---

## Business Memory Architecture

**Category:** Knowledge and operational continuity architecture  
**Maturity:** Architecture and schema work across AJ Digital systems

### Operating problem

Critical business knowledge often remains trapped in founder memory, isolated documents, chat histories, and disconnected tools. This creates dependency, inconsistent decisions, and repeated discovery work.

### System response

The business-memory architecture organizes:

- organizational context
- decisions and rationale
- workflows and operating rules
- client and project knowledge
- evidence provenance
- implementation history
- reusable patterns and constraints

The architecture connects stored knowledge to retrieval, governed workflow execution, and decision support so teams and AI systems can use context without treating every stored statement as equally verified.

---

## Professional Relevance

Together, these systems demonstrate capability across:

- business operations
- process and workflow design
- program and implementation management
- AI governance
- knowledge management
- systems architecture
- field-service operations
- human-in-the-loop controls
- documentation and SOP development
- cross-functional translation between business needs and technical implementation
