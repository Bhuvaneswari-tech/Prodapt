from pydantic import BaseModel
from typing import Optional

class CustomerSchema(BaseModel):
    name: str
    email: str
    address: Optional[str] = None

class CustomerResponse(CustomerSchema):
    id: str

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
