from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def pptx_agent(state):
    prs = Presentation()
    # Widescreen 16:9
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)

    for slide_data in state["presentation"]["slides"]:
        design = slide_data.get("design", {})
        
        # Create Blank Slide
        slide = prs.slides.add_slide(prs.slide_layouts[6]) 

        # 1. Background -> Always Clean White for Modern Look
        bg = slide.background.fill
        bg.solid()
        bg.fore_color.rgb = RGBColor(255, 255, 255)

        # 2. Get Theme Color (Handle missing key safely)
        hex_color = design.get("theme_color", "#4285F4").lstrip('#')
        try:
            r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        except:
            r, g, b = 66, 133, 244 # Default Blue

        # 3. Add Accent Sidebar (The "Premium" look)
        # Adds a colored strip on the far left
        sidebar = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, 
            Inches(0), Inches(0), Inches(0.4), Inches(7.5)
        )
        sidebar.fill.solid()
        sidebar.fill.fore_color.rgb = RGBColor(r, g, b)
        sidebar.line.fill.background() # No outline

        # 4. Title
        title_box = slide.shapes.add_textbox(
            Inches(0.8), Inches(0.5), Inches(11), Inches(1.2)
        )
        tf = title_box.text_frame
        p = tf.paragraphs[0]
        p.text = slide_data["title"]
        p.font.size = Pt(32)
        p.font.bold = True
        p.font.name = "Arial"
        p.font.color.rgb = RGBColor(50, 50, 50) # Dark Grey

        # 5. Bullets
        body_box = slide.shapes.add_textbox(
            Inches(0.8), Inches(1.8), Inches(8), Inches(5)
        )
        tf = body_box.text_frame
        tf.word_wrap = True
        
        for bullet in slide_data["bullets"]:
            p = tf.add_paragraph()
            p.text = bullet
            p.font.size = Pt(18)
            p.level = 0
            p.space_after = Pt(14) # Spacing between bullets

    prs.save("output.pptx")
    return state