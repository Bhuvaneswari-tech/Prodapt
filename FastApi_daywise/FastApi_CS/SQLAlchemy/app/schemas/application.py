from pydantic import BaseModel

class ApplicationBase(BaseModel):
    user_id: int
    job_id: int

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationOut(ApplicationBase):
    id: int
    class Config:
        orm_mode = True
