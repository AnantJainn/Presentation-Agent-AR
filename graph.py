# graph.py
from langgraph.graph import StateGraph
from agents.narrative_agent import narrative_agent
from agents.design_agent import design_agent
from agents.pptx_agent import pptx_agent
from agents.google_slides_agent import google_slides_agent

builder = StateGraph(dict)

builder.add_node("narrative", narrative_agent)
builder.add_node("design", design_agent)
builder.add_node("pptx", pptx_agent)
builder.add_node("google", google_slides_agent)

builder.set_entry_point("narrative")

builder.add_edge("narrative", "design")
builder.add_edge("design", "pptx")
builder.add_edge("pptx", "google")

graph = builder.compile()
