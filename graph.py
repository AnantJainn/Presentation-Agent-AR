# graph.py
from langgraph.graph import StateGraph, END
from agents.narrative_agent import narrative_agent
from agents.pptx_agent import pptx_agent
from agents.beamer_agent import beamer_agent

def route_output_format(state):
    # Return the name of the node to visit next
    if state.get("output_format") == "beamer":
        return "beamer"
    else:
        return "pptx"

builder = StateGraph(dict)

builder.add_node("narrative", narrative_agent)
builder.add_node("pptx", pptx_agent)
builder.add_node("beamer", beamer_agent)

builder.set_entry_point("narrative")

# CONDITIONAL EDGE: Narrative -> (PPTX or Beamer)
builder.add_conditional_edges(
    "narrative",
    route_output_format,
    {
        "pptx": "pptx",
        "beamer": "beamer"
    }
)

builder.add_edge("pptx", END)
builder.add_edge("beamer", END)

graph = builder.compile()