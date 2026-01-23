# agents/narrative_agent.py
from llm import call_llm
from utils.json_utils import extract_json

def narrative_agent(state):
    tex_content = state.get("tex_content", "")
    audience = state.get("audience", "General Audience")

    # Truncate if too huge
    if len(tex_content) > 20000:
        tex_content = tex_content[:20000] + "... [Truncated]"

    prompt = f"""
You are an expert Research Assistant transforming a Paper into a Presentation.

INPUT CONTEXT (LaTeX Source):
\"\"\"
{tex_content}
\"\"\"

TASK:
1. Analyze the structure (Title, Authors, Abstract, Sections).
2. Create a presentation structure (5-7 slides).
3. **CRITICAL:** The 'content' and 'key_points' must be **PLAIN ENGLISH**. 
   - DO NOT write LaTeX code (e.g. do NOT write \\frac{{a}}{{b}}, write 'a divided by b').
   - DO NOT use backslashes.

Return ONLY valid JSON. No Markdown.

Schema:
{{
  "title": "Paper Title",
  "slides": [
    {{
      "title": "Slide Title",
      "content": "Summary paragraph in plain text.",
      "key_points": ["Point 1", "Point 2"],
      "visual_description": "Description of a diagram or image for this section."
    }}
  ]
}}
"""

    content = call_llm(prompt)
    state["presentation"] = extract_json(content)
    return state