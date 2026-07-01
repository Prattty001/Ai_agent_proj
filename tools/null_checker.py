import pandas as pd

def check_nulls(df):
    null_counts = df.isnull().sum()
    total_rows = len(df)

    issues = []


    for column, count in null_counts.items():
        if count > 0:
            issues.append({
                "column": column,
                "null_count": int(count),
                "null_percentage": round((count / total_rows) * 100, 2)
            })

    if issues:
        return {
            "status": "FAIL",
            "issues": issues
        }

    return {
        "status": "PASS",
        "details": "No null values found."
    }