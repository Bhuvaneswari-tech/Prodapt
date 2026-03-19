from app.model.user import User

def create_user(db, user):
    db_user = User(**user.dict()) 
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db):
    return db.query(User).all()
    
    

#** - takes key-value pair from dictionary and pass them as arguments

#dict() - convert into dictionary format
#** - keyword arguments

#User(name="John", email="john@gmail.com")