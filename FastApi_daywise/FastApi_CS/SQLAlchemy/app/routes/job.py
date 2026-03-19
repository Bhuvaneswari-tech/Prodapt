from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import job_service
from app.schemas.job import JobCreate, JobOut
from app.core.database import get_db
from typing import List

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.post("/", response_model=JobOut)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    return job_service.create_job(db, title=job.title, description=job.description, owner_id=job.owner_id)

@router.get("/", response_model=List[JobOut])
def read_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return job_service.get_jobs(db, skip=skip, limit=limit)
