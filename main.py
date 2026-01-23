# main.py
import env
from graph import graph
import os
from utils.arxiv_loader import load_tex_from_source

# --- CONFIGURATION ---
print("--- Presentation Agent ---")
print("1. Paste ArXiv Link (e.g., https://arxiv.org/abs/2401.xxxxx)")
print("2. Provide Path to local .tar file")
print("3. Use Dummy Text (Press Enter)")

user_input = input("Enter option or path: ").strip()

tex_content = ""

if user_input:
    try:
        print("⏳ Processing source...")
        tex_content = load_tex_from_source(user_input)
        print(f"✅ Successfully loaded {len(tex_content)} characters of LaTeX.")
    except Exception as e:
        print(f"❌ Error loading source: {e}")
        exit(1)
else:
    print("ℹ️ Using default dummy LaTeX...")
    tex_content = r"""
    \documentclass{article}
    \title{Trust-proof Decentralized Learning}
    \begin{document}
    \maketitle
    \section{Introduction}
    Traditional blockchain consensus...
    \end{document}
    """ # (You can keep your long dummy text here if you want)

# --- WORKFLOW ---
state = {
    "tex_content": tex_content, 
    "output_format": "beamer",  # Change to 'pptx' if desired
    "audience": "PhD Researchers"
}

print(f"🚀 Building {state['output_format'].upper()} Presentation...")
final_state = graph.invoke(state)

print("\n✅ DONE!")
if state.get("output_format") == "pptx":
    print(f"📂 PPTX saved: {os.path.abspath('output.pptx')}")
else:
    print(f"📂 Beamer TeX saved: {os.path.abspath('presentation.tex')}")
    print("👉 Download 'presentation.tex' and compile it on Overleaf/LaTeX.")