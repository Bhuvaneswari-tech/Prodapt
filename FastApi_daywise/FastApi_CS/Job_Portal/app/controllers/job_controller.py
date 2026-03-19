from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.job_schema import JobCreate, JobResponse
from app.services import job_service

router = APIRouter(prefix="/jobs")

@router.post("/",response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    return job_service.create_job_service(db,job)

@router.get("/",response_model=list[JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    return job_service.get_jobs_service(db)