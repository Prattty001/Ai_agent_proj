import pandas as pd


def check_business_rules(df):

    issues = []

    if "amount" in df.columns:

        invalid = df[df["amount"] <= 0]

        if not invalid.empty:

            sample_records = (
                invalid
                .head(5)
                .fillna("NULL")
                .to_dict(orient="records")
            )

            issues.append({

                "rule": "Amount must be greater than zero",

                "failed_records": len(invalid),

                "minimum_amount": float(
                    invalid["amount"].min()
                ),

                "sample_records": sample_records

            })

    if issues:

        return {

            "status": "FAIL",

            "issues": issues

        }

    return {

        "status": "PASS",

        "details": "Business rules passed."

    }