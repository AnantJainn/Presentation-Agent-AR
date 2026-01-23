# schema.py
from pydantic import BaseModel
from typing import List, Optional

class Slide(BaseModel):
    title: str
    bullets: List[str]
    layout: str
    emphasis: Optional[str] = None

class Presentation(BaseModel):
    audience: str
    theme: str
    slides: List[Slide]
