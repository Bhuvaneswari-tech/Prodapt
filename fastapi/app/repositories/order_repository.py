from app.core.database import db
from app.models.order import Order

class OrderRepository:
    def __init__(self):
        self.collection = db["orders"]

    async def create(self, order: dict):
        result = await self.collection.insert_one(order)
        return str(result.inserted_id)

    async def get(self, order_id: str):
        return await self.collection.find_one({"_id": order_id})

    async def list(self):
        return await self.collection.find().to_list(100)

    async def update(self, order_id: str, data: dict):
        await self.collection.update_one({"_id": order_id}, {"$set": data})

    async def delete(self, order_id: str):
        await self.collection.delete_one({"_id": order_id})
