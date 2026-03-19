from app.repositories import user_repository

def create_user_service(db, user):
    return user_repository.create_user(db,user)

def get_users_service(db, skip, limit):
    return user_repository.get_users(db, skip, limit)

def get_user_by_id_service(db, user_id):
    return user_repository.get_user_by_id(db, user_id)

#Business logic layer