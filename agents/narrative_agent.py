# # agents/narrative_agent.py
# from llm import call_llm
# from utils.json_utils import extract_json

# def narrative_agent(state):
#     tex_content = state.get("tex_content", "")
#     audience = state.get("audience", "General Audience")

#     # Truncate if too huge
#     if len(tex_content) > 20000:
#         tex_content = tex_content[:20000] + "... [Truncated]"

#     prompt = f"""
# You are an expert Research Assistant transforming a Paper into a Presentation.

# INPUT CONTEXT (LaTeX Source):
# \"\"\"
# {tex_content}
# \"\"\"

# TASK:
# 1. Analyze the structure (Title, Authors, Abstract, Sections, Working Mechanism, Related Work).
# 2. Create a presentation structure (8-10 slides) that should very detail and cover all main things.
# 3. **CRITICAL:** The 'content' and 'key_points' must be **PLAIN ENGLISH**. 
#    - DO NOT write LaTeX code (e.g. do NOT write \\frac{{a}}{{b}}, write 'a divided by b').
#    - DO NOT use backslashes.

# Return ONLY valid JSON. No Markdown.

# Schema:
# {{
#   "title": "Paper Title",
#   "slides": [
#     {{
#       "title": "Slide Title",
#       "content": "Summary paragraph in plain text.",
#       "key_points": ["Point 1", "Point 2"],
#       "visual_description": "Description of a diagram or image for this section."
#     }}
#   ]
# }}
# """

#     content = call_llm(prompt)
#     state["presentation"] = extract_json(content)
#     return state






# agents/narrative_agent.py
from llm import call_llm
from utils.json_utils import extract_json

def narrative_agent(state):
    tex_content = state.get("tex_content", "")
    images_list = state.get("images_list", [])
    
    # Truncate if too huge
    if len(tex_content) > 50000:
        tex_content = tex_content[:50000] + "... [Truncated]"

    prompt = f"""
You are an expert Research Assistant transforming a Paper into a Presentation.

AVAILABLE IMAGES: {images_list}
(These are image files extracted from the source folder. You must use them if the paper references them.)

INPUT CONTEXT (LaTeX Source):
\"\"\"
{tex_content}
\"\"\"

TASK:
1. Analyze the structure (Title, Authors, Abstract, Sections, Working Mechanism, Related Work).
2. Create a presentation structure (10-11 slides) that should very detail and cover all main things.
3. **IMAGE MAPPING:** Look for \\includegraphics{{filename}} in the LaTeX source. If a slide covers that section, INCLUDE the corresponding filename from the 'AVAILABLE IMAGES' list.
4. **EXPLANATION:** If you include an image, write a short 1-sentence caption explaining it in 'image_caption'.

Return ONLY valid JSON.

Schema:
{{
  "title": "Paper Title",
  "slides": [
    {{
      "title": "Slide Title",
      "content": "Summary paragraph in plain text.",
      "key_points": ["Point 1", "Point 2"],
      "image_filename": "example.png (OR null if no image)",
      "image_caption": "Explanation of the image."
    }}
  ]
}}
"""

    content = call_llm(prompt)
    state["presentation"] = extract_json(content)
    return state