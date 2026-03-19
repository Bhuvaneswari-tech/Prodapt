from sqlalchemy.orm import Session
from app.repositories import job_repository

def get_job(db: Session, job_id: int):
    return job_repository.get_job(db, job_id)

def get_jobs(db: Session, skip: int = 0, limit: int = 10):
    return job_repository.get_jobs(db, skip, limit)

def create_job(db: Session, title: str, description: str, owner_id: int):
    return job_repository.create_job(db, title, description, owner_id)
