def check_duplicates(df):
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        return {
            "status": "FAIL",
            "duplicate_records": int(duplicate_count)
        }

    return {
        "status": "PASS",
        "details": "No duplicate records found."
    }