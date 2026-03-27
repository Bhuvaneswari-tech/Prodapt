from app.model.application import Application

def apply_job(db, application):
    db_app = Application(**application.dict())
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app

def get_applications(db):
    return db.query(Application).all()