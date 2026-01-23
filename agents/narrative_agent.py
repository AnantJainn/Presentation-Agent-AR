# agents/narrative_agent.py
from llm import call_llm
from utils.json_utils import extract_json

def narrative_agent(state):
    topic = state["topic"]
    audience = state["audience"]

    prompt = f"""
You are a Professor creating a deep-dive lecture slide deck.

Return ONLY valid JSON.
No markdown.

Schema:
{{
  "audience": "{audience}",
  "theme": "string",
  "slides": [
    {{
      "title": "string",
      "content": "A very detailed, 50-80 word academic paragraph explaining the concept in depth. Use formal language.",
      "key_points": ["Key Point 1", "Key Point 2"],
      "visual_keyword": "microchip | dna | brain | network | doctor | robot"
    }}
  ]
}}

Topic: {topic}
Audience: {audience}

Constraints:
1. Create 8-10 slides.
2. The 'content' field must be DETAILED and EXPLANATORY (not just bullets).
3. Select the best visual keyword for the slide context.
"""

    content = call_llm(prompt)
    state["presentation"] = extract_json(content)
    return state