from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Request
from app.core.config import settings

class Database:
    client: AsyncIOMotorClient = None

    @classmethod
    def connect(cls):
        cls.client = AsyncIOMotorClient(settings.MONGODB_URI)

    @classmethod
    def get_db(cls):
        return cls.client[settings.DB_NAME]
