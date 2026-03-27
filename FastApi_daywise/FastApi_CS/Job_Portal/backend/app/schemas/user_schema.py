from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str
    
class UserResponse(UserCreate):
    id: int

    class Config:
        orm_mode = True