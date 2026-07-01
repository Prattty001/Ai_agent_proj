from tools.read_data import load_data
from tools.schema_validator import validate_schema
from tools.null_checker import check_nulls
from tools.duplicate_checker import check_duplicates
from tools.business_rule_checker import check_business_rules
from tools.freshness_checker import check_freshness
from tools.report_generator import generate_report

class DataValidationAgent:
    def __init__(self):
        print("Data Validation Agent Initialized")

    def validate(self, file_path, expected_schema):

        df = load_data(file_path)

        results = {
            "Schema": validate_schema(df, expected_schema),
            "Null Check": check_nulls(df),
            "Duplicate Check": check_duplicates(df),
            "Business Rules": check_business_rules(df),
            "Freshness": check_freshness(df)
        }
# This one is quick consoel summary !..

        self.summarize(results)

        report = generate_report(results)

        return report

    def summarize(self, results):

        print("\n========== VALIDATION REPORT ==========\n")

        overall = "READY"

        for check, result in results.items():

            print(f"{check}")
            print(result)
            print()

            if result.get("status") == "FAIL":
                overall = "NOT READY"

        print("=======================================")
        print(f"Final Readiness Decision : {overall}")