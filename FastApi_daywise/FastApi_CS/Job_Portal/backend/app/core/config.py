from pydantic_settings import BaseSettings
from dotenv import load_dotenv

#load .env file
load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL:str
    APP_NAME: str
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
        