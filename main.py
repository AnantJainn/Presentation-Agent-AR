# # main.py
# import env
# from graph import graph
# import os
# from utils.arxiv_loader import load_tex_from_source

# # --- CONFIGURATION ---
# print("--- Presentation Agent ---")
# print("1. Paste ArXiv Link (e.g., https://arxiv.org/abs/2401.xxxxx)")
# print("2. Provide Path to local .tar file")
# print("3. Use Dummy Text (Press Enter)")

# user_input = input("Enter option or path: ").strip()

# tex_content = ""

# if user_input:
#     try:
#         print("⏳ Processing source...")
#         tex_content = load_tex_from_source(user_input)
#         print(f"✅ Successfully loaded {len(tex_content)} characters of LaTeX.")
#     except Exception as e:
#         print(f"❌ Error loading source: {e}")
#         exit(1)
# else:
#     print("ℹ️ Using default dummy LaTeX...")
#     tex_content = r"""
#     \documentclass{article}
#     \title{Trust-proof Decentralized Learning}
#     \begin{document}
#     \maketitle
#     \section{Introduction}
#     Traditional blockchain consensus...
#     \end{document}
#     """ # (You can keep your long dummy text here if you want)

# # --- WORKFLOW ---
# state = {
#     "tex_content": tex_content, 
#     "output_format": "beamer",  # Change to 'pptx' if desired
#     "audience": "PhD Researchers"
# }

# print(f"🚀 Building {state['output_format'].upper()} Presentation...")
# final_state = graph.invoke(state)

# print("\n✅ DONE!")
# if state.get("output_format") == "pptx":
#     print(f"📂 PPTX saved: {os.path.abspath('output.pptx')}")
# else:
#     print(f"📂 Beamer TeX saved: {os.path.abspath('presentation.tex')}")
#     print("👉 Download 'presentation.tex' and compile it on Overleaf/LaTeX.")







# # main.py
# import env
# from graph import graph
# import os
# from utils.arxiv_loader import load_tex_from_source

# def get_user_input():
#     print("\n--- Presentation Source ---")
#     print("1. Enter ArXiv Link")
#     print("2. Enter Path to Local .tar File")
#     print("3. Use Dummy Data")
    
#     choice = input("👉 Select Option (1/2/3): ").strip()
    
#     if choice == "1":
#         return input("🔗 Paste ArXiv URL: ").strip()
        
#     elif choice == "2":
#         # REPLACED GUI with simple text input
#         path = input("📂 Enter the full path to the .tar file: ").strip()
#         # Remove quotes if user copied as "path/to/file"
#         path = path.strip('"').strip("'")
        
#         if not os.path.exists(path):
#             print(f"❌ Error: File not found at '{path}'")
#             exit()
#         return path
        
#     elif choice == "3":
#         return None # Triggers dummy data fallback
        
#     else:
#         print("❌ Invalid selection.")
#         exit()

# # --- MAIN WORKFLOW ---
# user_source = get_user_input()
# tex_content = ""

# if user_source:
#     try:
#         print("⏳ Processing source...")
#         tex_content = load_tex_from_source(user_source)
#         print(f"✅ Successfully loaded {len(tex_content)} characters of LaTeX.")
#     except Exception as e:
#         print(f"❌ Error loading source: {e}")
#         exit(1)
# else:
#     print("ℹ️ Using default dummy LaTeX...")
#     tex_content = r"""
#     \documentclass{article}
#     \title{Trust-proof Decentralized Learning}
#     \begin{abstract}
#     This is a dummy placeholder for testing the pipeline without an external file.
#     \end{abstract}
#     \begin{document}
#     \maketitle
#     \section{Introduction}
#     Traditional blockchain consensus mechanisms...
#     \end{document}
#     """

# state = {
#     "tex_content": tex_content, 
#     "output_format": "beamer",  # Options: 'beamer' or 'pptx'
#     "audience": "PhD Researchers"
# }

# print(f"🚀 Building {state['output_format'].upper()} Presentation...")
# final_state = graph.invoke(state)

# print("\n✅ DONE!")
# if state.get("output_format") == "pptx":
#     print(f"📂 PPTX saved: {os.path.abspath('output.pptx')}")
# else:
#     print(f"📂 Beamer TeX saved: {os.path.abspath('presentation.tex')}")
#     print("👉 Download 'presentation.tex' and compile it on Overleaf/LaTeX.")





# main.py
import env
from graph import graph
import os
from utils.arxiv_loader import load_tex_from_source

def get_user_input():
    print("\n--- 🤖 Presentation Agent (OpenRouter Edition) ---")
    print("1. Enter ArXiv Link")
    print("2. Enter Path to Local .tar File")
    print("3. Use Dummy Data")
    
    choice = input("👉 Select Option (1/2/3): ").strip()
    
    if choice == "1":
        return input("🔗 Paste ArXiv URL: ").strip()
    elif choice == "2":
        path = input("📂 Enter the full path to the .tar file: ").strip().strip('"')
        if not os.path.exists(path):
            print(f"❌ Error: File not found at '{path}'")
            exit()
        return path
    elif choice == "3":
        return None
    else:
        print("❌ Invalid selection.")
        exit()

# --- INITIAL SETUP ---
user_source = get_user_input()
tex_content = ""

if user_source:
    try:
        print("⏳ Processing source...")
        tex_content = load_tex_from_source(user_source)
        print(f"✅ Loaded {len(tex_content)} chars.")
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)
else:
    print("ℹ️ Using default dummy LaTeX...")
    tex_content = r"""\documentclass{article}\title{The Future of AI}\begin{document}\section{Intro}AI is changing the world...\end{document}"""

# Initialize State
state = {
    "tex_content": tex_content, 
    "output_format": "beamer",
    "audience": "PhD Researchers",
    "iteration": 0,
    "critique": "",
    "user_feedback": "",
    "presentation": None
}

# --- INTERACTIVE LOOP ---
while True:
    print(f"\n🚀 Running Optimization Cycle (Max 3 Internal Iterations)...")
    
    # Run the graph
    # Note: The graph itself handles the 3 internal iterations via the 'critique' node loop
    final_state = graph.invoke(state)
    
    # Update our local state with the result
    state = final_state
    
    print("\n" + "="*40)
    print("✅ Generation Complete!")
    if state["output_format"] == "beamer":
        print(f"📂 Output: {os.path.abspath('presentation.tex')}")
    else:
        print(f"📂 Output: {os.path.abspath('output.pptx')}")
    print("="*40)

    # --- USER SATISFACTION CHECK ---
    user_sat = input("\n🤔 Are you satisfied with this result? (y/n): ").lower().strip()
    
    if user_sat == 'y':
        print("🎉 Awesome! Exiting.")
        break
    else:
        print("\n🔧 Let's fix it.")
        feedback = input("👉 What should be changed? (e.g., 'Make it more detailed', 'Add a slide about X', 'Too concise'): ")
        
        # Reset iteration count to allow the graph to loop again for the new request
        state["iteration"] = 0 
        state["user_feedback"] = feedback
        state["critique"] = "User requested changes." # Trigger the refinement logic
        print("\n🔄 Restarting agent with your feedback...")