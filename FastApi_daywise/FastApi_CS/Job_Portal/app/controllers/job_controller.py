from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.job_schema import JobCreate, JobResponse
from app.services import job_service

router = APIRouter(prefix="/jobs")

@router.post("/",response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    return job_service.create_job_service(db,job)

# ✅ Query Params (Filtering + Pagination)
@router.get("/", response_model=list[JobResponse])
def get_jobs(
    title: str = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db)
):
    return job_service.get_jobs_service(db, title, skip, limit)


# ✅ Path Param
@router.get("/{job_id}", response_model=JobResponse)
def get_job_by_id(job_id: int, db: Session = Depends(get_db)):
    return job_service.get_job_by_id_service(db, job_id)