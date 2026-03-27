from app.model.job import Job

def create_job(db,job):
    db_job = Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_jobs(db, title, skip, limit):
    query = db.query(Job)

    if title:
        query = query.filter(Job.title.contains(title))

    return query.offset(skip).limit(limit).all()


def get_job_by_id(db, job_id):
    return db.query(Job).filter(Job.id == job_id).first()