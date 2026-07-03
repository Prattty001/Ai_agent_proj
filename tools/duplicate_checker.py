import pandas as pd


def check_duplicates(df):

    duplicate_rows = df[df.duplicated(keep=False)]

    duplicate_count = int(df.duplicated().sum())

    if duplicate_count > 0:

        sample_records = (
            duplicate_rows
            .head(5)
            .fillna("NULL")
            .to_dict(orient="records")
        )

        duplicate_columns = []

        if "order_id" in df.columns:
            duplicate_columns.append("order_id")

        return {

            "status": "FAIL",

            "duplicate_count": duplicate_count,

            "possible_duplicate_columns": duplicate_columns,

            "sample_duplicate_records": sample_records

        }

    return {

        "status": "PASS",

        "details": "No duplicate records found."

    }