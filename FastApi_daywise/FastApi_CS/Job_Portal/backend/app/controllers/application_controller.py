from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.application_schema import ApplicationCreate
from app.services import application_service

router = APIRouter(prefix="/applications")

@router.post("/")
def apply_job(application: ApplicationCreate, db: Session = Depends(get_db)):
    return application_service.apply_job_service(db, application)

@router.get("/")
def get_applications(db: Session = Depends(get_db)):
    return application_service.get_applications_service(db)