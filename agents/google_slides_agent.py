# agents/google_slides_agent.py
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import time

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

    # User's Shared Folder ID
    FOLDER_ID = "1HZWU82y-D0BpDKUS9jFDYfDCp4f3Hyt4"
    presentation_title = state.get("topic", "Generated Presentation")

    # ---------------------------------------------------------
    # 1️⃣ FIX 403 ERROR: Create directly in the shared folder
    # ---------------------------------------------------------
    print(f"📂 Creating '{presentation_title}' in folder...")
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
    print(f"✅ Created Presentation ID: {presentation_id}")

    # ---------------------------------------------------------
    # 2️⃣ BUILD SLIDES: Generate 'createSlide' requests
    # ---------------------------------------------------------
    slides_data = state["presentation"]["slides"]
    requests = []
    
    # We keep track of the new slide IDs we are creating
    # Format: "slide_0", "slide_1", etc.
    slide_ids = []

    for i, slide in enumerate(slides_data):
        unique_id = f"slide_{i}_generated"
        slide_ids.append(unique_id)
        
        # Determine Layout
        layout = "TITLE_AND_BODY"
        if slide.get("layout") == "two_column":
            layout = "TITLE_AND_TWO_COLUMNS"
        
        # Request: Create Slide
        requests.append({
            "createSlide": {
                "objectId": unique_id,
                "insertionIndex": i + 1, # Append after title slide
                "slideLayoutReference": {
                    "predefinedLayout": layout
                }
            }
        })
        
        # Request: Set Background (Beautification)
        if slide.get("design"):
            bg_color = slide["design"].get("background", "light")
            rgb = {"red": 1, "green": 1, "blue": 1} # Default white
            
            if bg_color == "dark":
                rgb = {"red": 0.1, "green": 0.1, "blue": 0.2}
            elif bg_color == "gradient_blue":
                rgb = {"red": 0.9, "green": 0.95, "blue": 1.0}
            elif bg_color == "gradient_purple":
                rgb = {"red": 0.95, "green": 0.9, "blue": 1.0}

            requests.append({
                "updatePageProperties": {
                    "objectId": unique_id,
                    "pageProperties": {
                        "pageBackgroundFill": {
                            "solidFill": {
                                "color": {
                                    "rgbColor": rgb
                                }
                            }
                        }
                    },
                    "fields": "pageBackgroundFill"
                }
            })

    # Execute Batch 1: Create the blank slides
    if requests:
        slides_service.presentations().batchUpdate(
            presentationId=presentation_id,
            body={'requests': requests}
        ).execute()

    # ---------------------------------------------------------
    # 3️⃣ POPULATE CONTENT: Insert Text into Placeholders
    # ---------------------------------------------------------
    # We must fetch the presentation to get the placeholder IDs (Title/Body)
    # for the slides we just created.
    
    prs = slides_service.presentations().get(
        presentationId=presentation_id
    ).execute()
    
    text_requests = []
    
    # Create a map of our custom slide IDs to the actual slide objects
    # Note: The API might change IDs slightly or we match by logic.
    # Since we set objectId, we can find them directly.
    
    for i, slide_obj in enumerate(prs.get("slides", [])):
        page_id = slide_obj["objectId"]
        
        # Skip the default Title Slide (index 0 usually) unless we used it
        if page_id not in slide_ids:
            continue
            
        # Find which data corresponds to this slide
        data_index = slide_ids.index(page_id)
        slide_content = slides_data[data_index]
        
        # Find Placeholders
        title_id = None
        body_id = None
        
        for element in slide_obj.get("pageElements", []):
            if "shape" in element and "placeholder" in element["shape"]:
                type_ = element["shape"]["placeholder"]["type"]
                if type_ == "TITLE" or type_ == "CENTERED_TITLE":
                    title_id = element["objectId"]
                elif type_ == "BODY":
                    body_id = element["objectId"]
        
        # 1. Insert Title
        if title_id:
            text_requests.append({
                "insertText": {
                    "objectId": title_id,
                    "text": slide_content["title"]
                }
            })
            # Style Title (Accent Color)
            if slide_content.get("design", {}).get("accent_color"):
                hex_color = slide_content["design"]["accent_color"].lstrip('#')
                # Convert Hex to RGB
                r = int(hex_color[0:2], 16) / 255.0
                g = int(hex_color[2:4], 16) / 255.0
                b = int(hex_color[4:6], 16) / 255.0
                
                text_requests.append({
                    "updateTextStyle": {
                        "objectId": title_id,
                        "style": {
                            "foregroundColor": {
                                "opaqueColor": {
                                    "rgbColor": {"red": r, "green": g, "blue": b}
                                }
                            },
                            "bold": True,
                            "fontSize": {"magnitude": 24, "unit": "PT"}
                        },
                        "fields": "foregroundColor,bold,fontSize"
                    }
                })

        # 2. Insert Bullets
        if body_id and slide_content.get("bullets"):
            bullet_text = "\n".join(slide_content["bullets"])
            text_requests.append({
                "insertText": {
                    "objectId": body_id,
                    "text": bullet_text
                }
            })

    # Execute Batch 2: Insert Text
    if text_requests:
        slides_service.presentations().batchUpdate(
            presentationId=presentation_id,
            body={'requests': text_requests}
        ).execute()

    print("✨ Slides populated successfully!")
    state["google_slides_id"] = presentation_id
    return state