from backend.llm.gemini_client import get_ai_validation

dummy_report = {
    "Validation Summary": "FAIL",
    "Business Impact": [
        "Missing values",
        "Duplicate records"
    ]
}

response = get_ai_validation(dummy_report)

print(response)