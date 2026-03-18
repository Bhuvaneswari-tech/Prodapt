from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URL: str = "mongodb://localhost:27017"
    MONGODB_DB_NAME: str = "ecommerce_db"
    APP_NAME: str = "Ecommerce FastAPI"
    class Config:
        env_file = ".env"

settings = Settings()
