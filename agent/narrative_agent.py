# agents/narrative_agent.py
import json
from llm import call_llm

def narrative_agent(state):
    topic = state["topic"]
    audience = state["audience"]

    prompt = f"""
Generate a presentation plan in JSON.

Topic: {topic}
Audience: {audience}

Rules:
- Max 10 slides
- Academic structure
- Output ONLY valid JSON
"""

    content = call_llm(prompt)

    print("\n===== RAW LLM OUTPUT =====")
    print(content)
    print("===== END OUTPUT =====\n")

    state["presentation"] = json.loads(content)
    return state
