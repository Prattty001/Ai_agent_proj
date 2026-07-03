import json
import os


def generate_report(results, output_file="outputs/validation_report.json"):

    report = {
        "Validation Summary": "PASS",

        "Scope Assessed": {
            "Dataset": "orders.csv",
            "Validation Checks": [
                "Schema",
                "Null Check",
                "Duplicate Check",
                "Business Rules",
                "Freshness"
            ]
        },

        # Raw validation evidence
        "Rule Results": {},

        # Overall severity
        "Severity": "LOW",

        # Final readiness
        "Readiness Decision": "READY",

        # Helpful metadata for AI
        "Validation Statistics": {
            "Total Checks": len(results),
            "Passed Checks": 0,
            "Failed Checks": 0,
            "Failed Rules": []
        }
    }

    severity = "LOW"

    passed = 0
    failed = 0
    failed_rules = []

    for rule_name, result in results.items():

        report["Rule Results"][rule_name] = result

        if result.get("status") == "PASS":

            passed += 1

        else:

            failed += 1

            failed_rules.append(rule_name)

            report["Validation Summary"] = "FAIL"

            report["Readiness Decision"] = "NOT READY"

            if rule_name in [
                "Schema",
                "Null Check",
                "Duplicate Check",
                "Business Rules"
            ]:
                severity = "HIGH"

            elif (
                rule_name == "Freshness"
                and severity != "HIGH"
            ):
                severity = "MEDIUM"

    report["Severity"] = severity

    report["Validation Statistics"]["Passed Checks"] = passed
    report["Validation Statistics"]["Failed Checks"] = failed
    report["Validation Statistics"]["Failed Rules"] = failed_rules

    os.makedirs(
        os.path.dirname(output_file),
        exist_ok=True
    )

    with open(output_file, "w") as f:

        json.dump(
            report,
            f,
            indent=4
        )

    return report