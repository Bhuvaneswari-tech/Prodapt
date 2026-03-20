from pydantic import BaseModel, EmailStr
from typing import Optional
from bson import ObjectId

class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: EmailStr
    hashed_password: str
    role: str
