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
      "bullets": ["string 1", "string 2"],
      "layout": "two_column",
      "design": {{
        "background": "light | dark | gradient_blue | gradient_purple",
        "title_font": "Montserrat | Inter | Poppins",
        "accent_color": "#RRGGBB",
        "visual": "quantum_computer | dna | brain_scan | chip | healthcare | generic",
        "animation": "fade_in"
      }}
    }}
  ]
}}

Audience: {audience}
Topic: {topic}

Design Constraints:
1. **Concise & High-Density**: Use academic language but keep bullets under 20 words each to prevent text overflow.
2. **Visuals**: Choose the most relevant 'visual' keyword from the list provided in the schema.
3. **Structure**: 5-7 slides maximum.
"""

    content = call_llm(prompt)

    print("\n===== RAW LLM OUTPUT =====")
    print(content)
    print("===== END OUTPUT =====\n")

    state["presentation"] = extract_json(content)
    return state