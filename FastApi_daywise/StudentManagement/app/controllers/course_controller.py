from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.services import service
from app.models.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/courses/", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return service.create_course_service(db, course)

@router.get("/courses/", response_model=list[schemas.Course])
def read_courses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return service.get_courses_service(db, skip, limit)

@router.get("/courses/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = service.get_course_service(db, course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course
