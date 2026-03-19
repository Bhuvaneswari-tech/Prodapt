from app.repositories import application_repository

def apply_job_service(db,application):
    return application_repository.apply_job(db,application)