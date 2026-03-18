from app.core.database import db
from app.models.category import Category

class CategoryRepository:
    def __init__(self):
        self.collection = db["categories"]

    async def create(self, category: dict):
        result = await self.collection.insert_one(category)
        return str(result.inserted_id)

    async def get(self, category_id: str):
        return await self.collection.find_one({"_id": category_id})

    async def list(self):
        return await self.collection.find().to_list(100)

    async def update(self, category_id: str, data: dict):
        await self.collection.update_one({"_id": category_id}, {"$set": data})

    async def delete(self, category_id: str):
        await self.collection.delete_one({"_id": category_id})
