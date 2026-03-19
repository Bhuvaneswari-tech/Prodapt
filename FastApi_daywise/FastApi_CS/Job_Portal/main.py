from fastapi import FastAPI
from app.core.database import Base, engine
from app.controllers import user_controller, job_controller, application_controller
from app.middleware.logging_middleware import log_requests
from app.middleware.cors import add_cors
from app.middleware.exception_middleware import custom_exception_handler  

app = FastAPI()

# Create DB tables
Base.metadata.create_all(bind=engine)

# Middleware
app.middleware("http")(log_requests)
add_cors(app)

# ✅ Register Exception Handler
app.add_exception_handler(Exception, custom_exception_handler)

# Routers
app.include_router(user_controller.router)
app.include_router(job_controller.router)
app.include_router(application_controller.router)

@app.get("/")
def root():
    return {"message": "Job Portal API Running"}




#uvicorn main:app --reload

