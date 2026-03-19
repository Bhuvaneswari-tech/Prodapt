from app.repositories import job_repository

def create_job_service(db, job):
    return job_repository.create_job(db,job)

def get_jobs_service(db, title, skip, limit):
    return job_repository.get_jobs(db, title, skip, limit)

def get_job_by_id_service(db, job_id):
    return job_repository.get_job_by_id(db, job_id)