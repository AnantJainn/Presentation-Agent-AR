# main.py
import env
from graph import graph
import os

# --- 1. PASTE YOUR RESEARCH PAPER TEX HERE ---
# (This is a dummy example of a Quantum Computing paper)
dummy_tex_paper = r"""
\documentclass{article}
\title{Quantum-Classical Hybrid Architectures for Drug Discovery}
\author{Dr. A. Turing, Dr. R. Feynman}
\begin{document}
\maketitle

\begin{abstract}
We propose a novel hybrid algorithm combining Variational Quantum Eigensolvers (VQE) with classical deep learning to accelerate molecular docking. Our method achieves a 40% speedup over pure classical approaches.
\end{abstract}

\section{Introduction}
Drug discovery is computationally expensive. Classical simulation of molecular dynamics scales exponentially with electron count. Quantum computing offers a solution via superposition.

\section{Methodology}
We utilize a parameterized quantum circuit (PQC) acting as a kernel for a classical Support Vector Machine (SVM). The dataset consists of 5000 protein-ligand pairs.
\begin{equation}
H = \sum_{i} c_i P_i
\end{equation}

\section{Results}
Our hybrid model identified 15 high-affinity candidates for the target protein kinase-3. The accuracy was 94.5% compared to 89% for classical Random Forest.

\section{Conclusion}
Hybrid quantum-classical workflows are the near-term future of pharmaceutical R&D, bridging the gap until fault-tolerant quantum hardware arrives.
\end{document}
"""

# --- 2. CONFIGURE YOUR AGENT ---
state = {
    "tex_content": dummy_tex_paper,
    "output_format": "beamer",  # Options: "pptx" OR "beamer"
    "audience": "Academic Peers"
}

# --- 3. RUN ---
print(f"🚀 Parsing Paper & Building {state['output_format'].upper()} Presentation...")
final_state = graph.invoke(state)

print("\n✅ DONE!")
if state["output_format"] == "pptx":
    print(f"📂 PPTX saved: {os.path.abspath('output.pptx')}")
else:
    print(f"📂 Beamer TeX saved: {os.path.abspath('presentation.tex')}")
    print("👉 Compile this file using 'pdflatex presentation.tex' or Overleaf.")