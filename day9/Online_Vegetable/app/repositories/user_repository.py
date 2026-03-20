from app.models.user import User
from typing import Optional
from pymongo.collection import Collection

class UserRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def get_by_email(self, email: str) -> Optional[User]:
        data = await self.collection.find_one({"email": email})
        if data:
            data["id"] = str(data["_id"])
            return User(**data)
        return None

    async def create(self, user: User) -> str:
        result = await self.collection.insert_one(user.dict())
        return str(result.inserted_id)
