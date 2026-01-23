# agents/google_slides_agent.py
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import time

# --- PUBLIC IMAGE LIBRARY (Reliable Wikimedia/Unsplash URLs) ---
IMAGE_MAP = {
    "quantum_computer": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IBM_Q_System_One_2019.jpg/800px-IBM_Q_System_One_2019.jpg",
    "dna": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/DNA_Overview.png/800px-DNA_Overview.png",
    "brain_scan": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Computed_tomography_of_human_brain_-_large.png/800px-Computed_tomography_of_human_brain_-_large.png",
    "chip": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Raspberry_Pi_4_Model_B_-_Side.jpg/800px-Raspberry_Pi_4_Model_B_-_Side.jpg",
    "healthcare": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Physician_Assistant_Checking_Patient.jpg/800px-Physician_Assistant_Checking_Patient.jpg",
    "generic": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python_logo_notext.svg/800px-Python_logo_notext.svg.png"
}

def google_slides_agent(state):
    print("🚀 Connecting to Google Services...")
    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=[
            "https://www.googleapis.com/auth/presentations",
            "https://www.googleapis.com/auth/drive"
        ]
    )

    slides_service = build("slides", "v1", credentials=creds)
    drive_service = build("drive", "v3", credentials=creds)

    # 1️⃣ Create File
    FOLDER_ID = "1HZWU82y-D0BpDKUS9jFDYfDCp4f3Hyt4"
    presentation_title = state.get("topic", "Generated Presentation")
    
    print(f"📂 Creating '{presentation_title}'...")
    file_metadata = {
        'name': presentation_title,
        'mimeType': 'application/vnd.google-apps.presentation',
        'parents': [FOLDER_ID] 
    }
    
    presentation_file = drive_service.files().create(
        body=file_metadata,
        fields='id'
    ).execute()
    
    presentation_id = presentation_file.get('id')
    print(f"✅ Created ID: {presentation_id}")

    # 2️⃣ Generate Slides
    slides_data = state["presentation"]["slides"]
    requests = []
    slide_ids = []

    for i, slide in enumerate(slides_data):
        unique_id = f"slide_{i}_gen"
        slide_ids.append(unique_id)
        
        # Force 2-Column Layout (Left=Text, Right=Image)
        requests.append({
            "createSlide": {
                "objectId": unique_id,
                "insertionIndex": i + 1,
                "slideLayoutReference": {"predefinedLayout": "TITLE_AND_TWO_COLUMNS"}
            }
        })
        
        # Background Color
        if slide.get("design"):
            bg_color = slide["design"].get("background", "light")
            rgb = {"red": 1, "green": 1, "blue": 1} # Default white
            if bg_color == "dark": rgb = {"red": 0.1, "green": 0.1, "blue": 0.2}
            elif bg_color == "gradient_blue": rgb = {"red": 0.9, "green": 0.95, "blue": 1.0}
            elif bg_color == "gradient_purple": rgb = {"red": 0.95, "green": 0.9, "blue": 1.0}

            requests.append({
                "updatePageProperties": {
                    "objectId": unique_id,
                    "pageProperties": {
                        "pageBackgroundFill": {"solidFill": {"color": {"rgbColor": rgb}}}
                    },
                    "fields": "pageBackgroundFill"
                }
            })

    # Execute Batch 1: Create Slides
    if requests:
        slides_service.presentations().batchUpdate(
            presentationId=presentation_id,
            body={'requests': requests}
        ).execute()

    # 3️⃣ Populate Content (Text + Images)
    prs = slides_service.presentations().get(presentationId=presentation_id).execute()
    text_requests = []
    
    for i, slide_obj in enumerate(prs.get("slides", [])):
        page_id = slide_obj["objectId"]
        if page_id not in slide_ids: continue
            
        data_index = slide_ids.index(page_id)
        slide_content = slides_data[data_index]
        
        # Identify Placeholders
        title_id, body_id, image_placeholder_id = None, None, None
        
        # In TITLE_AND_TWO_COLUMNS: Index 0=Title, Index 1=Left Body, Index 2=Right Body
        placeholders = []
        for element in slide_obj.get("pageElements", []):
            if "shape" in element and "placeholder" in element["shape"]:
                placeholders.append(element)
        
        # Sort by vertical position (Y) to separate Title from Body, then X for columns
        # (Simplified approach relying on standard API order)
        for element in placeholders:
            type_ = element["shape"]["placeholder"]["type"]
            idx = element["shape"]["placeholder"].get("index", 0)
            
            if type_ == "TITLE" or type_ == "CENTERED_TITLE":
                title_id = element["objectId"]
            elif type_ == "BODY":
                if body_id is None: body_id = element["objectId"] # First body (Left)
                else: image_placeholder_id = element["objectId"]  # Second body (Right)

        # A. Insert Title
        if title_id:
            text_requests.append({"insertText": {"objectId": title_id, "text": slide_content["title"]}})

        # B. Insert Bullets (Left Column) & Fix Font Size
        if body_id and slide_content.get("bullets"):
            bullet_text = "\n".join(slide_content["bullets"])
            text_requests.append({"insertText": {"objectId": body_id, "text": bullet_text}})
            
            # Force smaller font size to prevent overflow
            text_requests.append({
                "updateTextStyle": {
                    "objectId": body_id,
                    "style": {
                        "fontSize": {"magnitude": 11, "unit": "PT"},
                        "bold": False
                    },
                    "fields": "fontSize,bold"
                }
            })

        # C. Insert Image (Right Column)
        if image_placeholder_id:
            visual_key = slide_content.get("design", {}).get("visual", "generic")
            # Clean key (e.g. "image:mri_scan" -> "mri_scan")
            if ":" in visual_key: visual_key = visual_key.split(":")[1]
            
            # Fallback to generic if key not found
            image_url = IMAGE_MAP.get(visual_key, IMAGE_MAP["generic"])
            
            # We replace the placeholder with the image
            text_requests.append({
                "createImage": {
                    "url": image_url,
                    "elementProperties": {
                        "pageObjectId": page_id,
                        # We use the position of the second column placeholder
                        "size": {"height": {"magnitude": 300, "unit": "PT"}, "width": {"magnitude": 400, "unit": "PT"}},
                        "transform": {
                            "scaleX": 1, "scaleY": 1,
                            "translateX": 4500000, # Approx right side (EMU)
                            "translateY": 1500000,
                            "unit": "EMU"
                        }
                    }
                }
            })
            # Remove the empty text box that was there
            text_requests.append({"deleteObject": {"objectId": image_placeholder_id}})

    if text_requests:
        slides_service.presentations().batchUpdate(
            presentationId=presentation_id,
            body={'requests': text_requests}
        ).execute()

    print("✨ Slides populated with Text & Images!")
    state["google_slides_id"] = presentation_id
    return state