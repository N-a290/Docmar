from pydantic import BaseModel
from typing import Optional

class Document(BaseModel):
    title: str
    type: str
    category: list[str]
    summary: str
    cover: str