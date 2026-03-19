from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import user_service
from app.schemas.user import UserCreate, UserOut
from app.core.database import get_db
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, name=user.name, email=user.email)

@router.get("/", response_model=List[UserOut])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user_service.get_users(db, skip=skip, limit=limit)
