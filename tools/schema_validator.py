def validate_schema(df, expected_schema):
    """
    Validates whether the dataframe has the expected columns and datatypes.
    """
    # Check Missing Columns
    missing_columns = [
        col for col in expected_schema.keys()
        if col not in df.columns
    ]

    # Check Extra Columns
    extra_columns = [
        col for col in df.columns
        if col not in expected_schema.keys()
    ]

    # Check Data Types
    datatype_issues = []

    for col, expected_dtype in expected_schema.items():

        if col in df.columns:

            actual_dtype = str(df[col].dtype)

            # Treat pandas 'object' and python 'str' as equivalent
            if (
                (expected_dtype == "object" and actual_dtype == "str") or
                (expected_dtype == "str" and actual_dtype == "object")
            ):
                continue

            if expected_dtype not in actual_dtype:
                datatype_issues.append({
                    "column": col,
                    "expected": expected_dtype,
                    "actual": actual_dtype
                })

    if not missing_columns and not extra_columns and not datatype_issues:
        return {
            "status": "PASS",
            "details": "Schema is valid."
        }

    return {
        "status": "FAIL",
        "missing_columns": missing_columns,
        "extra_columns": extra_columns,
        "datatype_issues": datatype_issues
    }