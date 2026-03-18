from pydantic import BaseModel
from typing import Optional

class ProductSchema(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: str
    stock: int

class ProductResponse(ProductSchema):
    id: str

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[str] = None
    stock: Optional[int] = None
