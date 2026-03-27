from fastapi import FastAPI
from app.models import models, database
from app.controllers import student_controller, course_controller
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_controller.router, prefix="/api", tags=["students"])
app.include_router(course_controller.router, prefix="/api", tags=["courses"])
