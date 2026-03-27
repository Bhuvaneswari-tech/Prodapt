from sqlalchemy.orm import Session
from app.repositories import repository
from app.schemas import schemas

def get_student_service(db: Session, student_id: int):
    return repository.get_student(db, student_id)

def get_students_service(db: Session, skip: int = 0, limit: int = 10):
    return repository.get_students(db, skip, limit)

def create_student_service(db: Session, student: schemas.StudentCreate):
    return repository.create_student(db, student)

def get_course_service(db: Session, course_id: int):
    return repository.get_course(db, course_id)

def get_courses_service(db: Session, skip: int = 0, limit: int = 10):
    return repository.get_courses(db, skip, limit)

def create_course_service(db: Session, course: schemas.CourseCreate):
    return repository.create_course(db, course)
