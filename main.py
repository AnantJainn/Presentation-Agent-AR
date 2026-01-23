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







# main.py
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
import sys
from utils.arxiv_loader import load_tex_from_source

# Check if running in Google Colab
try:
    from google.colab import files
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

def get_user_input():
    print("\n--- Presentation Source ---")
    print("1. Enter ArXiv Link")
    print("2. Upload .tar File")
    print("3. Use Dummy Data")
    
    choice = input("👉 Select Option (1/2/3): ").strip()
    
    if choice == "1":
        return input("🔗 Paste ArXiv URL: ").strip()
        
    elif choice == "2":
        if IN_COLAB:
            print("📂 Uploading file via Google Colab...")
            uploaded = files.upload()
            if not uploaded:
                print("❌ No file uploaded.")
                sys.exit()
            # Return the name of the first file uploaded
            return list(uploaded.keys())[0]
        else:
            # Fallback for local (non-Colab) execution
            path = input("📂 Enter path to local .tar file: ").strip()
            if not os.path.exists(path):
                print("❌ File not found.")
                sys.exit()
            return path
        
    elif choice == "3":
        return None # Triggers dummy data fallback
        
    else:
        print("❌ Invalid selection.")
        sys.exit()

# --- MAIN WORKFLOW ---
user_source = get_user_input()
tex_content = ""

if user_source:
    try:
        print(f"⏳ Processing source: {user_source}...")
        tex_content = load_tex_from_source(user_source)
        print(f"✅ Successfully loaded {len(tex_content)} characters of LaTeX.")
    except Exception as e:
        print(f"❌ Error loading source: {e}")
        # Print full traceback for debugging if needed
        import traceback
        traceback.print_exc()
        sys.exit(1)
else:
    print("ℹ️ Using default dummy LaTeX...")
    tex_content = r"""
    \documentclass{article}
    \title{Trust-proof Decentralized Learning}
    \begin{abstract}
    This is a dummy placeholder for testing the pipeline without an external file.
    \end{abstract}
    \begin{document}
    \maketitle
    \section{Introduction}
    Traditional blockchain consensus mechanisms...
    \end{document}
    """

state = {
    "tex_content": tex_content, 
    "output_format": "beamer",  # Options: 'beamer' or 'pptx'
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