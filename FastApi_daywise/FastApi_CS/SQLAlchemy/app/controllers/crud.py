from sqlalchemy.orm import Session
from app.models import User, Job, Application

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, name: str, email: str):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_job(db: Session, job_id: int):
    return db.query(Job).filter(Job.id == job_id).first()

def get_jobs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Job).offset(skip).limit(limit).all()

def create_job(db: Session, title: str, description: str, owner_id: int):
    db_job = Job(title=title, description=description, owner_id=owner_id)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def create_application(db: Session, user_id: int, job_id: int):
    db_app = Application(user_id=user_id, job_id=job_id)
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app

def get_applications(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Application).offset(skip).limit(limit).all()
