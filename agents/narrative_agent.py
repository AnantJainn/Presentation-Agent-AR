from llm import call_llm
from utils.json_utils import extract_json

def narrative_agent(state):
    topic = state["topic"]
    audience = state["audience"]

    prompt = f"""
You MUST output ONLY valid JSON.
No explanations. No markdown. No text.

Schema:
{{
  "audience": "{audience}",
  "theme": "string",
  "slides": [
    {{
      "title": "string",
      "bullets": ["string"],
      "layout": "title_content"
    }}
  ]
}}

Topic: {topic}
Audience: {audience}
"""

    content = call_llm(prompt)

    # 🔍 Debug once (keep for now)
    print("\n===== RAW LLM OUTPUT =====")
    print(content)
    print("===== END OUTPUT =====\n")

    state["presentation"] = extract_json(content)
    return state
