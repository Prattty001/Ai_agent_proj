import pandas as pd


def check_nulls(df):

    total_rows = len(df)

    issues = []

    for column in df.columns:

        null_count = int(df[column].isnull().sum())

        if null_count > 0:

            # Convert NaN -> "NULL" before sending as JSON
            sample_records = (
                df[df[column].isnull()]
                .head(5)
                .fillna("NULL")
                .to_dict(orient="records")
            )

            issues.append({
                "column": column,
                "null_count": null_count,
                "null_percentage": round(
                    (null_count / total_rows) * 100,
                    2
                ),
                "sample_records": sample_records
            })

    if issues:

        return {
            "status": "FAIL",
            "total_columns_with_nulls": len(issues),
            "issues": issues
        }

    return {
        "status": "PASS",
        "details": "No null values found."
    }