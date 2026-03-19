from pydantic import BaseModel
from typing import Optional

class JobBase(BaseModel):
    title: str
    description: Optional[str] = None

class JobCreate(JobBase):
    owner_id: int

class JobOut(JobBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True
