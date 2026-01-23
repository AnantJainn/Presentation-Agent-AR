import json
import re

def extract_json(text: str):
    """
    Extract the first valid JSON object from LLM output.
    """
    if not text or not text.strip():
        raise ValueError("LLM returned empty output")

    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError(f"No JSON found in LLM output:\n{text}")

    return json.loads(match.group())
