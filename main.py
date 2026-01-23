# main.py
import env
from graph import graph
import os

state = {
    "topic": "Quantum Machine Learning for Healthcare",
    "audience": "PhD Researchers"
}

# Run the graph
final_state = graph.invoke(state)

print("\n✅ SUCCESS: Presentation Generated!")
print(f"📂 File saved locally as: {os.path.abspath('output.pptx')}")
print("👉 Click the folder icon on the left to download 'output.pptx'")