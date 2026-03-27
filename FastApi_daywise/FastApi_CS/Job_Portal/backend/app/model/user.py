from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    email=Column(String,unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False, default="user")
    
    #Relationship
    application = relationship("Application",back_populates="user")