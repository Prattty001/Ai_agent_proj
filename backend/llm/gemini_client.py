import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_ai_validation(validation_report):

    prompt = f"""
You are a Senior Data Validation Engineer.

Analyze the validation report and respond ONLY using the information provided.

Do NOT invent additional validation failures.

If the dataset passes all validations, explain why it is READY.

Respond in Markdown using exactly these sections:

## Validation Summary
(2-3 lines)

## Business Impact
- Bullet points

## Root Cause
- Bullet points

## Recommendations
- Bullet points

## Final Readiness Decision
READY or NOT READY with one short explanation.

Keep the response under 300 words.

Validation Report:

{validation_report}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text