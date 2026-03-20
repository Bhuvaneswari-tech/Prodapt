from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str

class UserOut(BaseModel):
    id: str
    username: str
    email: EmailStr
    role: str
