from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Job(Base):
    __tablename__ = "jobs"
    
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    description=Column(String)
    
    #Relationship
    application = relationship("Application", back_populates="job")