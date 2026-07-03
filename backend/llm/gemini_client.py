import os
import json

from google import genai
from dotenv import load_dotenv

from backend.llm.prompts import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_ai_validation(validation_report):

    evidence = json.dumps(
        validation_report,
        indent=2
    )

    prompt = f"""
{SYSTEM_PROMPT}

Below is structured validation evidence produced by a deterministic validation engine.

Validation Evidence:
{evidence}

Instructions:

1. Analyze ONLY the provided evidence.
2. Do not invent validation failures.
3. Do not repeat the validation report.
4. Infer business impact from failed validations.
5. Infer likely technical root causes.
6. Prioritize the failed validations.
7. Recommend immediate remediation.
8. Recommend long-term prevention.
9. Mention affected downstream systems if applicable.
10. Give a confidence level.
11. End with a production readiness decision.

Return the answer in Markdown.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()