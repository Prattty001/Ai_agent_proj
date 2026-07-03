from fastapi import APIRouter, UploadFile, File
from fastapi.encoders import jsonable_encoder   # <-- NEW
import shutil
import os
import json

from agent import DataValidationAgent
from backend.llm.gemini_client import get_ai_validation

router = APIRouter()


def load_schema():

    with open("config/schema.json", "r") as f:
        return json.load(f)


@router.post("/validate")
def validate(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        file.filename
    )

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    agent = DataValidationAgent()

    expected_schema = load_schema()

    validation_report = agent.validate(
        file_path,
        expected_schema
    )

    try:

        ai_reasoning = get_ai_validation(
            validation_report
        )

    except Exception as e:

        ai_reasoning = f"""
# AI Reasoning Error

Unable to generate AI reasoning.

Reason:

{str(e)}
"""

    if os.path.exists(file_path):
        os.remove(file_path)

    response = jsonable_encoder({
        "validation_report": validation_report,
        "ai_summary": ai_reasoning
    })

    return response