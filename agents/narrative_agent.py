# agents/narrative_agent.py
from llm import call_llm
from utils.json_utils import extract_json

def narrative_agent(state):
    topic = state["topic"]
    audience = state["audience"]

    prompt = f"""
You are a premium presentation designer for a high-stakes keynote.

Return ONLY valid JSON.
No markdown. No explanation.

Schema:
{{
  "audience": "{audience}",
  "theme": "string",
  "slides": [
    {{
      "title": "string",
      "bullets": ["string 1", "string 2", "string 3"],
      "design": {{
        "theme_color": "#HexColor",
        "visual_keyword": "microchip | dna | robot | brain | network | doctor"
      }}
    }}
  ]
}}

Audience: {audience}
Topic: {topic}

Constraints:
1. **MAXIMUM 3 Bullets per slide.**
2. **MAXIMUM 12 words per bullet.** (Crucial for modern design).
3. **No sub-bullets.**
4. **Visuals:** Choose one keyword that best fits the slide concept.
5. Create exactly 5 slides.
"""

    content = call_llm(prompt)
    print("\n===== RAW LLM OUTPUT =====")
    print(content)
    print("===== END OUTPUT =====\n")

    state["presentation"] = extract_json(content)
    return state