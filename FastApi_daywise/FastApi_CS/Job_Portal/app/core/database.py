from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

#Create SQLAlchemy Engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,    #log enabling
    future=True             #SQLAlchemy 2.0 and above
)

#SessionFactory
SessionLocal=sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

#Base class for models
Base = declarative_base()

#Dependency Injection
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()