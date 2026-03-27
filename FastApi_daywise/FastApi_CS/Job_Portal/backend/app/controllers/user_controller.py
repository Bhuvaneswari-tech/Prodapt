#API Layer


from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.core.database import get_db
from app.schemas.user_schema import UserCreate, UserResponse, LoginRequest
from app.services import user_service
from app.model.user import User

router = APIRouter(prefix="/users")


# Registration endpoint
@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user. Requires: name, email, password, role ("admin" or "user").
    """
    return user_service.create_user_service(db, user)


@router.post("/login", response_model=UserResponse)
def login_user(credentials: LoginRequest, db: Session = Depends(get_db)):
    """
    Login a user with email and password.
    """
    email = credentials.email
    password = credentials.password
    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password required.")
    user = db.query(User).filter(and_(User.email == email, User.password == password)).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password.")
    return user

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



