# Compliance Validation Framework

> Reusable validation protocol templates and Python automation tools for FDA 21 CFR Part 11, GAMP 5, and CSA-compliant software system deployments in regulated pharmaceutical and laboratory environments.
>
> ![FDA](https://img.shields.io/badge/FDA%2021%20CFR%20Part%2011-compliant-red) ![GAMP5](https://img.shields.io/badge/GAMP%205-validated-blue) ![CSA](https://img.shields.io/badge/CSA-aligned-purple) ![Python](https://img.shields.io/badge/Python-automation-blue?logo=python)
>
> ---
>
> ## 📌 Project Overview
>
> This framework provides structured validation artifacts and automation scripts to support **Computer System Validation (CSV)** activities for LIMS, QMS, ERP, and enterprise software implementations in regulated environments. It is designed to reduce validation cycle time while maintaining full compliance with relevant regulations.
>
> **Applicable Regulations & Standards:**
> - FDA 21 CFR Part 11 (Electronic Records & Electronic Signatures)
> - - GAMP 5 (Good Automated Manufacturing Practice)
>   - - CSA (Computer Software Assurance) — FDA 2022 guidance
>     - - ICH Q10 (Pharmaceutical Quality System)
>       - - ISO 27001 (Information Security)
>        
>         - ---
>
> ## 📁 Project Structure
>
> ```
> compliance-validation-framework/
> ├── protocols/
> │   ├── IQ_protocol_template.md      # Installation Qualification template
> │   ├── OQ_protocol_template.md      # Operational Qualification template
> │   ├── PQ_protocol_template.md      # Performance Qualification template
> │   └── validation_plan_template.md  # Master Validation Plan
> ├── scripts/
> │   ├── audit_trail_checker.py       # Verify audit trail completeness
> │   ├── electronic_signature_validator.py  # 21 CFR Part 11 e-sig check
> │   └── validation_report_generator.py    # Auto-generate validation summary
> ├── templates/
> │   ├── SOP_template.md              # Standard Operating Procedure template
> │   ├── deviation_report_template.md # Deviation/CAPA template
> │   └── traceability_matrix.md       # Requirements traceability matrix (RTM)
> ├── docs/
> │   ├── gamp5_category_guide.md      # GAMP 5 software categorization guide
> │   └── csa_risk_framework.md        # CSA risk-based approach guide
> └── README.md
> ```
>
> ---
>
> ## ✅ Validation Lifecycle
>
> ```
> Phase 1: Planning
>     └── Master Validation Plan (MVP)
>     └── Risk Assessment (GAMP 5 categorization)
>     └── Requirements Traceability Matrix (RTM)
>
> Phase 2: Installation Qualification (IQ)
>     └── System installation verified
>     └── Configuration documented
>     └── Environment confirmed
>
> Phase 3: Operational Qualification (OQ)
>     └── Functional requirements tested
>     └── Edge cases and error handling verified
>     └── SOP compliance confirmed
>
> Phase 4: Performance Qualification (PQ)
>     └── End-to-end process validation
>     └── User acceptance testing (UAT)
>     └── Production environment confirmed
>
> Phase 5: Validation Report & Release
>     └── Deviations resolved
>     └── Stakeholder sign-off obtained
>     └── System released to production
> ```
>
> ---
>
> ## 🔧 Automation Scripts
>
> ### `audit_trail_checker.py`
> Verifies that all system actions are captured in the audit trail per 21 CFR Part 11 requirements. Checks for required fields: timestamp, user ID, action type, before/after values.
>
> ```bash
> python scripts/audit_trail_checker.py --log-file system_audit.log --report audit_report.csv
> ```
>
> ### `validation_report_generator.py`
> Automatically generates a validation summary report from executed test scripts and deviation logs.
>
> ```bash
> python scripts/validation_report_generator.py --iq iq_results.csv --oq oq_results.csv --pq pq_results.csv
> ```
>
> ---
>
> ## 📋 GAMP 5 Software Categories
>
> | Category | Description | Examples | Validation Effort |
> |---|---|---|---|
> | 1 | Infrastructure software | OS, network | Minimal |
> | 3 | Non-configured commercial software | MS Office | Low |
> | 4 | Configured commercial software | LIMS, ERP | Medium |
> | 5 | Custom software | Bespoke systems | High |
>
> *This framework primarily supports Category 4 and 5 validation activities.*
>
> ---
>
> ## 📋 21 CFR Part 11 Key Requirements
>
> | Requirement | Description | Automated Check |
> |---|---|---|
> | Audit Trail | All record changes logged with user, timestamp, reason | `audit_trail_checker.py` |
> | Electronic Signatures | Unique to individual, bound to record | `electronic_signature_validator.py` |
> | Access Controls | Role-based access, unique user IDs | Manual review + SOPs |
> | Record Integrity | Records cannot be altered without detection | Checksum verification |
> | System Validation | Software validated for intended use | This framework |
>
> ---
>
> ## 🚀 Getting Started
>
> ```bash
> git clone https://github.com/SnehaAjmira/compliance-validation-framework.git
> cd compliance-validation-framework
>
> # Install dependencies
> pip install pandas jinja2 python-docx
>
> # Run audit trail check
> python scripts/audit_trail_checker.py --help
>
> # Generate validation report
> python scripts/validation_report_generator.py --help
> ```
>
> ---
>
> ## ⚠️ Disclaimer
>
> These templates are provided as starting points for validation activities. All validation protocols must be reviewed and approved by qualified personnel before use. Adapt to your specific system, regulatory context, and organizational SOPs.
>
> ---
>
> *Built by [Sneha Ajmira](https://linkedin.com/in/contactsnehaajmira) | Product Owner & BSA specializing in regulated environments*
