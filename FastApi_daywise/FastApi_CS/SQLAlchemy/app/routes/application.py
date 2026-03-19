from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import application_service
from app.schemas.application import ApplicationCreate, ApplicationOut
from app.core.database import get_db
from typing import List

router = APIRouter(prefix="/applications", tags=["applications"])

@router.post("/", response_model=ApplicationOut)
def create_application(application: ApplicationCreate, db: Session = Depends(get_db)):
    return application_service.create_application(db, user_id=application.user_id, job_id=application.job_id)

@router.get("/", response_model=List[ApplicationOut])
def read_applications(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return application_service.get_applications(db, skip=skip, limit=limit)
