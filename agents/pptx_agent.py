# agents/pptx_agent.py
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
import requests
from io import BytesIO

# --- ASSET LIBRARY (Public Domain High-Res Images) ---
IMAGE_MAP = {
    "microchip": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IBM_Q_System_One_2019.jpg/800px-IBM_Q_System_One_2019.jpg",
    "dna": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/DNA_Overview.png/800px-DNA_Overview.png",
    "brain": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Computed_tomography_of_human_brain_-_large.png/800px-Computed_tomography_of_human_brain_-_large.png",
    "network": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Social_Network_Analysis_Visualization.png/800px-Social_Network_Analysis_Visualization.png",
    "doctor": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Physician_Assistant_Checking_Patient.jpg/800px-Physician_Assistant_Checking_Patient.jpg",
    "robot": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Honda_ASIMO_at_Auto_Shanghai_2011.jpg/800px-Honda_ASIMO_at_Auto_Shanghai_2011.jpg"
}

def download_image(keyword):
    """Fetches image bytes from URL"""
    url = IMAGE_MAP.get(keyword, IMAGE_MAP["microchip"])
    try:
        response = requests.get(url)
        return BytesIO(response.content)
    except:
        return None

def pptx_agent(state):
    print("🎨 Generative PPTX Engine Starting...")
    prs = Presentation()
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)

    slides_data = state["presentation"]["slides"]

    for i, slide_data in enumerate(slides_data):
        # Create Blank Slide
        slide = prs.slides.add_slide(prs.slide_layouts[6]) 
        
        # --- BACKGROUND & DESIGN ---
        # 1. Accent Bar (Left)
        sidebar = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, 
            Inches(0), Inches(0), Inches(0.5), Inches(7.5)
        )
        sidebar.fill.solid()
        sidebar.fill.fore_color.rgb = RGBColor(0, 102, 204) # Deep Blue
        sidebar.line.fill.background()

        # 2. Top Header Bar
        header = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, 
            Inches(0.5), Inches(0.5), Inches(12.83), Inches(0.1)
        )
        header.fill.solid()
        header.fill.fore_color.rgb = RGBColor(200, 200, 200) # Light Grey
        header.line.fill.background()

        # --- TEXT CONTENT ---
        # 3. Title
        title_box = slide.shapes.add_textbox(
            Inches(0.8), Inches(0.6), Inches(10), Inches(1.0)
        )
        tf = title_box.text_frame
        p = tf.paragraphs[0]
        p.text = slide_data["title"]
        p.font.size = Pt(36)
        p.font.bold = True
        p.font.name = "Arial"
        p.font.color.rgb = RGBColor(40, 40, 40)

        # 4. Detailed Paragraph (Left Side)
        content_box = slide.shapes.add_textbox(
            Inches(0.8), Inches(1.8), Inches(7.5), Inches(3.5)
        )
        tf = content_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = slide_data.get("content", "")
        p.font.size = Pt(16)
        p.font.name = "Georgia" # Academic Serif font
        p.line_spacing = 1.2

        # 5. Key Points (Bottom Left)
        if "key_points" in slide_data:
            kp_box = slide.shapes.add_textbox(
                Inches(0.8), Inches(5.5), Inches(7.5), Inches(2.0)
            )
            tf = kp_box.text_frame
            for point in slide_data["key_points"]:
                p = tf.add_paragraph()
                p.text = f"• {point}"
                p.font.size = Pt(14)
                p.font.bold = True
                p.font.color.rgb = RGBColor(0, 102, 204)

        # --- IMAGERY ---
        # 6. Insert Image (Right Side)
        visual_key = slide_data.get("visual_keyword", "microchip")
        image_stream = download_image(visual_key)
        
        if image_stream:
            # Place image on the right side
            try:
                slide.shapes.add_picture(
                    image_stream, 
                    Inches(8.5), Inches(1.8), # Left, Top
                    width=Inches(4.5), height=Inches(4.5)
                )
            except Exception as e:
                print(f"⚠️ Could not add image for {visual_key}: {e}")

    output_file = "output.pptx"
    prs.save(output_file)
    print(f"✅ Generated {output_file} with {len(slides_data)} detailed slides.")
    return state