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





# utils/arxiv_loader.py
import os
import tarfile
import requests
import shutil
import re
import tempfile

def is_url(string):
    return string.startswith("http://") or string.startswith("https://")

def download_arxiv_source(url, save_path):
    """
    Downloads the source tarball from an ArXiv URL.
    Converts /abs/ links to /e-print/ links automatically.
    """
    # Convert 'abs' URL to 'e-print' URL (source)
    if "/abs/" in url:
        url = url.replace("/abs/", "/e-print/")
    
    print(f"⬇️ Downloading source from {url}...")
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, stream=True)
    response.raise_for_status()
    
    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    return save_path

def find_main_tex_file(directory):
    r"""
    Heuristic to find the main .tex file:
    1. Looks for a file with \documentclass
    2. Prioritizes files named 'main.tex' or 'ms.tex'
    """
    tex_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".tex"):
                tex_files.append(os.path.join(root, file))

    if not tex_files:
        raise FileNotFoundError("No .tex files found in the archive.")

    # Check for \documentclass
    for path in tex_files:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if r"\documentclass" in content:
                return path

    return tex_files[0] # Fallback to first found

def flatten_tex(main_file_path):
    r"""
    Reads the main .tex file and recursively replaces \input{...} 
    with the actual content of the referenced files.
    """
    base_dir = os.path.dirname(main_file_path)
    
    with open(main_file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Regex to find \input{filename} or \include{filename}
    input_pattern = re.compile(r'\\(?:input|include)\{([^}]+)\}')

    def replace_match(match):
        filename = match.group(1)
        if not filename.endswith('.tex'):
            filename += '.tex'
        
        full_path = os.path.join(base_dir, filename)
        
        if os.path.exists(full_path):
            return flatten_tex(full_path)
        else:
            print(f"⚠️ Warning: Could not find included file {filename}")
            return f"% MISSING FILE: {filename}\n"

    # Replace all occurrences
    flattened_content = input_pattern.sub(replace_match, content)
    return flattened_content

def load_tex_from_source(input_source):
    """
    Main entry point.
    input_source: Can be an ArXiv URL or a local .tar path.
    Returns: The full flattened LaTeX string.
    """
    temp_dir = tempfile.mkdtemp()
    tar_path = ""

    try:
        # 1. Handle Input Type
        if is_url(input_source):
            tar_path = os.path.join(temp_dir, "source.tar")
            download_arxiv_source(input_source, tar_path)
        else:
            if not os.path.exists(input_source):
                raise FileNotFoundError(f"File not found: {input_source}")
            tar_path = input_source

        # 2. Extract
        extract_path = os.path.join(temp_dir, "extracted")
        os.makedirs(extract_path, exist_ok=True)
        
        try:
            with tarfile.open(tar_path, "r:*") as tar:
                tar.extractall(path=extract_path)
        except tarfile.ReadError:
            print("⚠️ Warning: File might not be a standard tarball. Attempting to read as plain text...")
            pass

        # 3. Find Main File
        main_file = find_main_tex_file(extract_path)
        print(f"📄 Found main file: {os.path.basename(main_file)}")

        # 4. Flatten content
        full_content = flatten_tex(main_file)
        return full_content

    finally:
        # Cleanup temp directory (only if we downloaded/created it)
        if is_url(input_source):
            shutil.rmtree(temp_dir, ignore_errors=True)