from llm import call_llm
from utils.json_utils import extract_json

def narrative_agent(state):
    topic = state["topic"]
    audience = state["audience"]

    prompt = f"""
You are a professional presentation designer.

Return ONLY valid JSON.
No markdown. No explanation.

Schema:
{{
  "audience": "{audience}",
  "theme": "string",
  "slides": [
    {{
      "title": "string",
      "bullets": ["string"],
      "layout": "title_content | two_column",
      "design": {{
        "background": "light | dark | gradient_blue | gradient_purple",
        "title_font": "Montserrat | Inter | Poppins",
        "accent_color": "#RRGGBB",
        "visual": "icon:healthcare | image:mri_scan | none",
        "animation": "fade_in | slide_up | none"
      }}
    }}
  ]
}}

Audience: {audience}
Topic: {topic}

Design rules:
- Minimal text
- Strong visual hierarchy
- Academic but modern
"""


    content = call_llm(prompt)

    # 🔍 Debug once (keep for now)
    print("\n===== RAW LLM OUTPUT =====")
    print(content)
    print("===== END OUTPUT =====\n")

    state["presentation"] = extract_json(content)
    return state
