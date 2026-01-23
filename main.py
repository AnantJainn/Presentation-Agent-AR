# main.py
import env
from graph import graph
import os

# --- PASTE YOUR LATEX HERE ---
# (Example: A snippet of a physics paper)
dummy_tex = r"""
\documentclass{article}
\title{Deep Learning for Quantum State Reconstruction}
\author{Jane Doe}
\begin{document}
\section{Introduction}
Quantum state tomography is slow. We introduce a neural network approach.
\section{Methods}
We use a Convolutional Neural Network (CNN) trained on 10,000 synthetic states.
\section{Results}
Our method achieves 99\% fidelity with 100x fewer measurements.
\end{document}
"""

state = {
    "tex_content": dummy_tex,   # <--- Put your real TeX here
    "output_format": "pptx",  # <--- Select 'beamer' or 'pptx'
    "audience": "PhD Researchers"
}

print(f"🚀 Parsing Paper & Building {state['output_format'].upper()} Presentation...")
final_state = graph.invoke(state)

print("\n✅ DONE!")
if state.get("output_format") == "pptx":
    print(f"📂 PPTX saved: {os.path.abspath('output.pptx')}")
else:
    print(f"📂 Beamer TeX saved: {os.path.abspath('presentation.tex')}")
    print("👉 Download 'presentation.tex' and compile it on Overleaf/LaTeX.")