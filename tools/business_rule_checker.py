def check_business_rules(df):
    issues = []

    if "amount" in df.columns:
        invalid = df[df["amount"] <= 0]

        if len(invalid):
            issues.append({
                "rule": "Amount must be greater than zero",
                "failed_records": len(invalid)
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