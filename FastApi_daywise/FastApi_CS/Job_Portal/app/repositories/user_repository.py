from app.model.user import User

def create_user(db, user):
    db_user = User(**user.dict()) 
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db, skip, limit):
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db, user_id):
    return db.query(User).filter(User.id == user_id).first()
    
    

#** - takes key-value pair from dictionary and pass them as arguments

#dict() - convert into dictionary format
#** - keyword arguments

#User(name="John", email="john@gmail.com")