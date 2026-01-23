# agents/narrative_agent.py
from llm import call_llm
from utils.json_utils import extract_json

def narrative_agent(state):
    topic = state["topic"]
    audience = state["audience"]

    prompt = f"""
You are a creative director for a high-end presentation.

Return ONLY valid JSON.
No markdown.

Schema:
{{
  "audience": "{audience}",
  "theme": "string",
  "slides": [
    {{
      "title": "Short, Punchy Title (Max 6 words)",
      "content": "A detailed, engaging paragraph (50-70 words) explaining the concept.",
      "key_points": ["Key Point 1", "Key Point 2"],
      "visual_description": "A descriptive prompt for an AI image generator. Example: 'futuristic quantum chip glowing blue in a sterile lab'"
    }}
  ]
}}

Topic: {topic}
Audience: {audience}

Constraints:
1. Create 8-10 slides.
2. Ensure 'visual_description' is specific and artistic.
3. Keep titles short to fit the layout.
4. The 'content' field must be DETAILED and EXPLANATORY (not just bullets).
"""

    content = call_llm(prompt)
    state["presentation"] = extract_json(content)
    return state