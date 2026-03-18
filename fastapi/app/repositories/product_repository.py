from app.core.database import db
from app.models.product import Product

class ProductRepository:
    def __init__(self):
        self.collection = db["products"]

    async def create(self, product: dict):
        result = await self.collection.insert_one(product)
        return str(result.inserted_id)

    async def get(self, product_id: str):
        return await self.collection.find_one({"_id": product_id})

    async def list(self):
        return await self.collection.find().to_list(100)

    async def update(self, product_id: str, data: dict):
        await self.collection.update_one({"_id": product_id}, {"$set": data})

    async def delete(self, product_id: str):
        await self.collection.delete_one({"_id": product_id})
