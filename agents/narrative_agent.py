# agents/narrative_agent.py
from llm import call_llm
from utils.json_utils import extract_json

def narrative_agent(state):
    topic = state["topic"]
    audience = state["audience"]

    prompt = f"""
You are a professional academic presentation designer.

Return ONLY valid JSON.
No markdown. No explanation.

Schema:
{{
  "audience": "{audience}",
  "theme": "string",
  "slides": [
    {{
      "title": "string",
      "bullets": ["detailed string 1", "detailed string 2"],
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
- Provide detailed, comprehensive academic content for each bullet point.
- Ensure 4-6 detailed bullet points per slide.
- Use strong professional vocabulary.
- Create 5-7 slides total.
"""

    content = call_llm(prompt)

    print("\n===== RAW LLM OUTPUT =====")
    print(content)
    print("===== END OUTPUT =====\n")

    state["presentation"] = extract_json(content)
    return state