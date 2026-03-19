from sqlalchemy.orm import Session
from app.models import Application

def create_application(db: Session, user_id: int, job_id: int):
    db_app = Application(user_id=user_id, job_id=job_id)
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app

def get_applications(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Application).offset(skip).limit(limit).all()
