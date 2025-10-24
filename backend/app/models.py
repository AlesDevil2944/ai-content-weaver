from pydantic import BaseModel
from enum import Enum
from typing import Optional

class ContentType(str, Enum):
    blog = "informative_blog"
    promo = "promotional_article"
    creative = "creative_writing"

class Tone(str, Enum):
    professional = "Professional"
    casual = "Casual"
    witty = "Witty"
    persuasive = "Persuasive"

class GenerateRequest(BaseModel):
    brief: str
    content_type: ContentType
    tone: Tone
    length: int = 500

class ContentResponse(BaseModel):
    content_html: str
    content_md: str
    meta_title: str
    meta_description: str
    readability_score: float
    readability_grade: str