from app.repositories import user_repository
from app.utils.webhook import send_webhook

def create_user_service(db, user):
    try:
        db_user = user_repository.create_user(db, user)
    except ValueError as e:
        # Optionally, raise HTTPException here if using FastAPI
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=str(e))
    send_webhook("user_registered", {"id": db_user.id, "name": db_user.name, "email": db_user.email})
    return db_user

def get_users_service(db, skip, limit):
    return user_repository.get_users(db, skip, limit)

def get_user_by_id_service(db, user_id):
    return user_repository.get_user_by_id(db, user_id)

#Business logic layer