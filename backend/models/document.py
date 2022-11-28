from pydantic import BaseModel
from typing import Optional

class Document(BaseModel):
    name: str
    type: str
    category: list[str]
    stock: int 
