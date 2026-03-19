from sqlalchemy.orm import Session
from app.repositories import application_repository

def create_application(db: Session, user_id: int, job_id: int):
    return application_repository.create_application(db, user_id, job_id)

def get_applications(db: Session, skip: int = 0, limit: int = 10):
    return application_repository.get_applications(db, skip, limit)
