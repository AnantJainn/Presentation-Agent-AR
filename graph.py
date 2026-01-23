# graph.py
from langgraph.graph import StateGraph
from agents.narrative_agent import narrative_agent
from agents.pptx_agent import pptx_agent

builder = StateGraph(dict)

builder.add_node("narrative", narrative_agent)
builder.add_node("pptx", pptx_agent)

builder.set_entry_point("narrative")

builder.add_edge("narrative", "pptx")
# builder.add_edge("pptx", "google")  <-- REMOVED THIS LINE

graph = builder.compile()