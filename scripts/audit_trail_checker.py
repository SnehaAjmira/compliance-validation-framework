"""
audit_trail_checker.py

Checks an exported audit trail for the record content expected under
FDA 21 CFR Part 11 (11.10(e)): who made the change, when, what changed
(old and new value), and why.

Usage:
    python scripts/audit_trail_checker.py --log-file examples/sample_audit_trail.csv \
                                          --report examples/audit_report.csv
Accepts CSV or JSON (a list of objects with the same field names).
"""

import argparse
import csv
import json
import logging
from datetime import datetime, timezone
from typing import Dict, List

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

REQUIRED_FIELDS = [
    "timestamp", "user_id", "action_type", "record_id",
    "field_name", "old_value", "new_value", "reason_for_change",
]
# Fields that may legitimately be blank: no prior value on CREATE, no new value on DELETE.
OPTIONAL_BY_ACTION = {"CREATE": {"old_value"}, "DELETE": {"new_value"}}
EMPTY_TOKENS = {"", "null", "none", "n/a"}
GENERIC_REASONS = {"test", "n/a", "none", "tbd", "update", "change", "fix"}
TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S"


def parse_log(path: str) -> List[Dict]:
    if path.lower().endswith(".csv"):
        with open(path, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _clean(value) -> str:
    return "" if value is None else str(value).strip()


def validate_entry(entry: Dict) -> List[str]:
    """Return a list of violations for one audit trail entry (empty list = compliant)."""
    issues = []
    action = _clean(entry.get("action_type")).upper()
    for name in REQUIRED_FIELDS:
        if name in OPTIONAL_BY_ACTION.get(action, set()):
            continue
        if _clean(entry.get(name)).lower() in EMPTY_TOKENS:
            issues.append(f"Missing {name}")

    reason = _clean(entry.get("reason_for_change")).lower()
    if reason and reason in GENERIC_REASONS:
        issues.append("Reason for change is generic")

    ts = _clean(entry.get("timestamp"))
    if ts:
        try:
            datetime.strptime(ts[:19], TIMESTAMP_FORMAT)
        except ValueError:
            issues.append("Timestamp not in ISO 8601 format")
    return issues


def run_check(entries: List[Dict]) -> Dict:
    errors = []
    for row, entry in enumerate(entries, start=1):
        issues = validate_entry(entry)
        if issues:
            errors.append({"row": row, "record_id": _clean(entry.get("record_id")) or "?", "issues": issues})
    total = len(entries)
    valid = total - len(errors)
    return {
        "total": total,
        "valid": valid,
        "invalid": len(errors),
        "compliance_pct": round(100 * valid / total, 1) if total else 0.0,
        "errors": errors,
    }


def save_report(results: Dict, path: str) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["21 CFR Part 11 Audit Trail Check"])
        w.writerow(["Generated (UTC)", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")])
        w.writerow(["Entries checked", results["total"]])
        w.writerow(["Compliant entries", results["valid"]])
        w.writerow(["Compliance %", results["compliance_pct"]])
        w.writerow([])
        w.writerow(["Row", "Record ID", "Issues"])
        for e in results["errors"]:
            w.writerow([e["row"], e["record_id"], "; ".join(e["issues"])])
    logger.info("Report written to %s", path)


def main():
    p = argparse.ArgumentParser(description="21 CFR Part 11 audit trail completeness check")
    p.add_argument("--log-file", required=True, help="Audit trail export (.csv or .json)")
    p.add_argument("--report", default="audit_report.csv", help="Output CSV report")
    args = p.parse_args()
    results = run_check(parse_log(args.log_file))
    logger.info("%s of %s entries compliant (%s%%)", results["valid"], results["total"], results["compliance_pct"])
    save_report(results, args.report)


if __name__ == "__main__":
    main()
