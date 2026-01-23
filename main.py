# main.py
import env
from graph import graph

state = {
    "topic": "Quantum Machine Learning for Healthcare",
    "audience": "PhD Researchers"
}

final_state = graph.invoke(state)

print("PPTX generated.")
print("Google Slides ID:", final_state["google_slides_id"])
