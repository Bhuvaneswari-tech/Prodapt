from app.repositories import job_repository
from app.utils.webhook import send_webhook

def create_job_service(db, job):
    db_job = job_repository.create_job(db, job)
    send_webhook("job_created", {"id": db_job.id, "title": db_job.title})
    return db_job

def get_jobs_service(db, title, skip, limit):
    return job_repository.get_jobs(db, title, skip, limit)

def get_job_by_id_service(db, job_id):
    job = job_repository.get_job_by_id(db, job_id)
    return job