# Requirements Traceability Matrix (RTM) Template

| Field | Value |
|---|---|
| System | [System name and version] |
| GAMP 5 category | [3 / 4 / 5] |
| Document ID | RTM-### |
| Version | [x.y] |

## Matrix

| Req ID | Requirement (URS/FRS) | Risk (H/M/L) | Part 11 clause | Test type | Test ID | Result | Deviation |
|---|---|---|---|---|---|---|---|
| URS-001 | System records user ID, date, and time for every record change | H | 11.10(e) | Scripted (OQ) | OQ-014 | Pass | |
| URS-002 | Reason for change is required before saving an edited result | H | 11.10(e) | Scripted (OQ) | OQ-015 | Pass | |
| URS-003 | Electronic signature shows printed name, date/time, and meaning | H | 11.50 | Scripted (OQ) | OQ-021 | Fail | DEV-007 |
| URS-004 | Only QA role can approve final results | H | 11.10(d), (g) | Scripted (OQ) | OQ-030 | Pass | |
| URS-005 | Results export to PDF with audit trail | M | 11.10(b) | Unscripted (CSA) | UT-005 | Pass | |
| URS-006 | Dashboard refreshes within 5 seconds | L | n/a | Exploratory (CSA) | EX-002 | Pass | |

## Coverage Summary

| Metric | Count |
|---|---|
| Requirements | [n] |
| Requirements with at least one test | [n] |
| Tests passed / failed | [n] / [n] |
| Open deviations | [n] |

## Guidance

- High-risk requirements (patient safety, product quality, data integrity) get scripted testing with documented evidence.
- Medium and low-risk requirements may use unscripted or exploratory testing under FDA Computer Software Assurance (CSA) guidance.
- Every failed test links to a deviation, and every deviation links to its resolution before release.
