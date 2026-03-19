from fastapi import FastAPI
from app.core.database import Base, engine

from app.routes import user_router, job_router, application_router

from app.middleware.cors import add_cors_middleware
from app.middleware.logging import logging_middleware
from app.middleware.exception import exception_middleware
from app.middleware.log_config import setup_logging

Base.metadata.create_all(bind=engine)

# Setup logging to file
setup_logging()

app = FastAPI()

# Add CORS middleware
add_cors_middleware(app)

# Add logging and exception middleware
app.middleware("http")(logging_middleware)
app.middleware("http")(exception_middleware)

# Routers for separation of concerns
app.include_router(user_router)
app.include_router(job_router)
app.include_router(application_router)
