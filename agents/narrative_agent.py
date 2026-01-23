# agents/narrative_agent.py
from llm import call_llm
from utils.json_utils import extract_json

def narrative_agent(state):
    tex_content = state.get("tex_content", "")
    audience = state.get("audience", "General Audience")

    # If text is too long for context window, we truncate (simple logic for now)
    if len(tex_content) > 15000:
        tex_content = tex_content[:15000] + "... [Truncated]"

    prompt = f"""
You are an expert Research Assistant. 
Analyze the following LaTeX (TeX) source code of a research paper and convert it into a presentation structure.

INPUT TEX:
\"\"\"
{tex_content}
\"\"\"

TASK:
1. Extract the Title and Authors.
2. Summarize the paper into 5-7 logical slides (e.g., Intro, Problem, Method, Results, Conclusion).
3. For "content", write a clear, academic paragraph (50 words).
4. For "visual_description", describe a relevant scientific diagram or image prompt based on that section.

Return ONLY valid JSON. No markdown.

Schema:
{{
  "title": "Paper Title",
  "slides": [
    {{
      "title": "Slide Title (e.g., Methodology)",
      "content": "Very Detailed academic explanation...",
      "key_points": ["Bullet 1", "Bullet 2"],
      "visual_description": "A diagram showing a quantum circuit connected to a classical neural network"
    }}
  ]
}}
"""

    content = call_llm(prompt)
    state["presentation"] = extract_json(content)
    return state