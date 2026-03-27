
from app.repositories import application_repository
from app.utils.webhook import send_webhook

def apply_job_service(db, application):
    db_application = application_repository.apply_job(db, application)
    # Send webhook after job application
    send_webhook("job_applied", {"id": db_application.id, "user_id": db_application.user_id, "job_id": db_application.job_id})
    return db_application

def get_applications_service(db):
    return application_repository.get_applications(db)