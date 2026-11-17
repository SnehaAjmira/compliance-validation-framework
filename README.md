# Compliance Validation Framework

A tested Python tool that checks exported audit trails against FDA 21 CFR Part 11 record requirements, plus a requirements traceability matrix template for computer system validation (CSV/CSA).

| | |
|---|---|
| **Domain** | Computer system validation, data integrity, regulated laboratories (GxP) |
| **Tools** | Python 3 (standard library only), Markdown |
| **Standards referenced** | FDA 21 CFR Part 11, GAMP 5, FDA Computer Software Assurance (CSA), ALCOA+ |
| **Contents** | 1 script, 1 template, sample data, unit tests |

---

## 1. Contents

| File | Purpose |
|---|---|
| `scripts/audit_trail_checker.py` | Checks each audit trail entry for required content and writes a compliance report |
| `templates/traceability_matrix_template.md` | RTM linking requirements to risk, Part 11 clause, test, result, and deviation |
| `examples/sample_audit_trail.csv` | 8 example LIMS audit entries, including deliberate defects |
| `examples/audit_report.csv` | Report generated from the sample file |
| `tests/test_audit_trail_checker.py` | Unit tests for each rule |

## 2. Rules Checked

| Rule | Basis | Notes |
|---|---|---|
| Who: `user_id` present | 21 CFR 11.10(e), ALCOA+ Attributable | |
| When: ISO 8601 `timestamp` | 11.10(e), Contemporaneous | |
| What: `record_id`, `field_name`, `old_value`, `new_value` | 11.10(e), Original | `old_value` optional on CREATE, `new_value` optional on DELETE |
| Why: `reason_for_change` present and specific | 11.10(e), GMP practice | Rejects generic values such as "TBD", "update", "test" |

## 3. Example Result

Run against `examples/sample_audit_trail.csv`: **3 of 8 entries compliant (37.5%)**.

| Row | Record | Issue found |
|---:|---|---|
| 3 | SMP-1002 | Missing reason_for_change |
| 4 | SMP-1003 | Missing user_id |
| 5 | SMP-1004 | Reason for change is generic |
| 6 | SMP-1001 | Timestamp not in ISO 8601 format |
| 8 | SMP-1006 | Missing new_value |

## 4. How to Run

```bash
python scripts/audit_trail_checker.py --log-file examples/sample_audit_trail.csv --report examples/audit_report.csv
python -m unittest discover -s tests -v
```

Input: CSV or JSON with columns `timestamp, user_id, action_type, record_id, field_name, old_value, new_value, reason_for_change`.

## 5. Repository Structure

```
compliance-validation-framework/
├── scripts/audit_trail_checker.py
├── templates/traceability_matrix_template.md
├── examples/
│   ├── sample_audit_trail.csv
│   └── audit_report.csv
└── tests/test_audit_trail_checker.py
```

## 6. Disclaimer

This tool supports review of audit trail exports. It does not validate a system on its own. Validation deliverables must be approved by qualified personnel under your quality system.

Author: [Sneha Ajmira](https://linkedin.com/in/contactsnehaajmira)
