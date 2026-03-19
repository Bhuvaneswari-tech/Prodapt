from sqlalchemy.orm import Session
from app.repositories import user_repository

def get_user(db: Session, user_id: int):
    return user_repository.get_user(db, user_id)

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return user_repository.get_users(db, skip, limit)

def create_user(db: Session, name: str, email: str):
    return user_repository.create_user(db, name, email)
