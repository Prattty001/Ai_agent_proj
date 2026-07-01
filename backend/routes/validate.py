from fastapi import APIRouter, UploadFile, File
import shutil
import os
import json

from agent import DataValidationAgent
from backend.llm.gemini_client import get_ai_validation

router = APIRouter()

# expected_schema = {
#     "order_id": "int64",
#     "customer_name": "object",
#     "amount": "int64",
#     "status": "object",
#     "order_date": "object"
# }
def load_schema():

    with open("config/schema.json", "r") as f:
        return json.load(f)


@router.post("/validate")
def validate(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    agent = DataValidationAgent()

    expected_schema = load_schema()

    report = agent.validate(
        file_path,
        expected_schema
    )

    try:
        ai_summary = get_ai_validation(report)

    except Exception as e:

        ai_summary = f"""
AI Summary could not be generated.

Reason:
{str(e)}
"""

    # Delete uploaded file after validation
    if os.path.exists(file_path):
        os.remove(file_path)

    return {
        "validation_report": report,
        "ai_summary": ai_summary
    }