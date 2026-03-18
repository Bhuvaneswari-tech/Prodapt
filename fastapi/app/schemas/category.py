from pydantic import BaseModel
from typing import Optional

class CategorySchema(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryResponse(CategorySchema):
    id: str

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
