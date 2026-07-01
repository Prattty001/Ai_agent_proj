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
        "Rule Results": {},
        "Business Impact": [],
        "Severity": "LOW",
        "Root Cause Hints": [],
        "Remediation Plan": [],
        "Prevention Recommendations": [],
        "Readiness Decision": "READY"
    }

    severity = "LOW"

    for rule_name, result in results.items():

        report["Rule Results"][rule_name] = result

        if result.get("status") == "FAIL":

            report["Validation Summary"] = "FAIL"
            report["Readiness Decision"] = "NOT READY"

            # ---------------- Schema ----------------

            if rule_name == "Schema":

                severity = "HIGH"

                report["Business Impact"].append(
                    "Schema mismatch can break downstream ETL pipelines and reporting."
                )

                report["Root Cause Hints"].append(
                    "Source schema changed or datatype mismatch detected."
                )

                report["Remediation Plan"].append(
                    "Update schema mapping or correct source datatypes."
                )

                report["Prevention Recommendations"].append(
                    "Implement schema contract validation before ingestion."
                )

            # ---------------- Null ----------------

            elif rule_name == "Null Check":

                severity = "HIGH"

                report["Business Impact"].append(
                    "Missing values may affect reporting, analytics and ML models."
                )

                report["Root Cause Hints"].append(
                    "Incomplete source records or failed ingestion."
                )

                report["Remediation Plan"].append(
                    "Fill missing values or reject incomplete records."
                )

                report["Prevention Recommendations"].append(
                    "Add mandatory field validation in ingestion pipeline."
                )

            # ---------------- Duplicate ----------------

            elif rule_name == "Duplicate Check":

                severity = "HIGH"

                report["Business Impact"].append(
                    "Duplicate records may inflate business metrics."
                )

                report["Root Cause Hints"].append(
                    "Duplicate ingestion or missing primary-key validation."
                )

                report["Remediation Plan"].append(
                    "Remove duplicate records before publishing."
                )

                report["Prevention Recommendations"].append(
                    "Add uniqueness constraint for Order ID."
                )

            # ---------------- Business Rules ----------------

            elif rule_name == "Business Rules":

                severity = "HIGH"

                report["Business Impact"].append(
                    "Invalid business records reduce data reliability."
                )

                report["Root Cause Hints"].append(
                    "Business validation rule violated."
                )

                report["Remediation Plan"].append(
                    "Correct invalid records before consumption."
                )

                report["Prevention Recommendations"].append(
                    "Automate business rule validation during ETL."
                )

            # ---------------- Freshness ----------------

            elif rule_name == "Freshness":

                severity = "MEDIUM"

                report["Business Impact"].append(
                    "Stale data may produce outdated business decisions."
                )

                report["Root Cause Hints"].append(
                    "Delayed pipeline execution."
                )

                report["Remediation Plan"].append(
                    "Rerun latest ingestion pipeline."
                )

                report["Prevention Recommendations"].append(
                    "Configure freshness SLA monitoring."
                )

    report["Severity"] = severity

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as f:
        json.dump(report, f, indent=4)

    return report