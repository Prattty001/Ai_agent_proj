def validate_schema(df, expected_schema):
    """
    Validates dataframe schema against expected schema.
    Returns structured validation evidence for AI reasoning.
    """

    missing_columns = [
        col
        for col in expected_schema
        if col not in df.columns
    ]

    extra_columns = [
        col
        for col in df.columns
        if col not in expected_schema
    ]

    datatype_issues = []

    for col, expected_dtype in expected_schema.items():

        if col in df.columns:

            actual_dtype = str(df[col].dtype)

            # Treat object and string as equivalent
            if (
                expected_dtype == "object"
                and actual_dtype == "str"
            ) or (
                expected_dtype == "str"
                and actual_dtype == "object"
            ):
                continue

            if expected_dtype not in actual_dtype:

                datatype_issues.append({

                    "column": col,

                    "expected_dtype": expected_dtype,

                    "actual_dtype": actual_dtype

                })

    if (
        not missing_columns
        and not extra_columns
        and not datatype_issues
    ):

        return {

            "status": "PASS",

            "details": "Schema validation passed."

        }

    return {

        "status": "FAIL",

        "missing_columns": missing_columns,

        "extra_columns": extra_columns,

        "datatype_issues": datatype_issues,

        "summary": {

            "missing_count": len(missing_columns),

            "extra_count": len(extra_columns),

            "datatype_issue_count": len(datatype_issues)

        }

    }