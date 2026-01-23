from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

def pptx_agent(state):
    prs = Presentation()
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)

    for slide_data in state["presentation"]["slides"]:
        design = slide_data["design"]

        slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank

        # Background
        bg = slide.background.fill
        bg.solid()

        if design["background"] == "dark":
            bg.fore_color.rgb = RGBColor(20, 24, 40)
        else:
            bg.fore_color.rgb = RGBColor(245, 247, 255)

        # Title
        title_box = slide.shapes.add_textbox(
            Inches(1), Inches(0.8), Inches(11), Inches(1.5)
        )
        tf = title_box.text_frame
        p = tf.paragraphs[0]
        p.text = slide_data["title"]
        p.font.size = Pt(36)
        p.font.bold = True
        p.font.name = design["title_font"]
        p.font.color.rgb = RGBColor.from_string(design["accent_color"][1:])

        # Bullets
        body = slide.shapes.add_textbox(
            Inches(1.5), Inches(2.5), Inches(10), Inches(4)
        )
        tf = body.text_frame
        tf.clear()

        for b in slide_data["bullets"]:
            bp = tf.add_paragraph()
            bp.text = b
            bp.font.size = Pt(20)
            bp.level = 1

    prs.save("output.pptx")
    return state
