#API Layer

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from app.services import user_service

router = APIRouter(prefix="/users")

@router.post("/",response_model=UserResponse)
def create_user(user: UserCreate, db:Session = Depends(get_db)):
    return user_service.create_user_service(db,user)

# @router.get("/",response_model=list[UserResponse])
# def get_users(db: Session = Depends(get_db)):
#     return user_service.get_users_service(db)

# SELECT * FROM users OFFSET :skip LIMIT :limit;

#GET /users?skip=0&limit=10

#Query Params (Pagination)
@router.get("/", response_model=list[UserResponse])
def get_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db)
):
    return user_service.get_users_service(db, skip, limit)

# Path Param
@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user_by_id_service(db, user_id)



