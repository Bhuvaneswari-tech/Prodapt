from app.core.database import db
from app.models.customer import Customer

class CustomerRepository:
    def __init__(self):
        self.collection = db["customers"]

    async def create(self, customer: dict):
        result = await self.collection.insert_one(customer)
        return str(result.inserted_id)

    async def get(self, customer_id: str):
        return await self.collection.find_one({"_id": customer_id})

    async def list(self):
        return await self.collection.find().to_list(100)

    async def update(self, customer_id: str, data: dict):
        await self.collection.update_one({"_id": customer_id}, {"$set": data})

    async def delete(self, customer_id: str):
        await self.collection.delete_one({"_id": customer_id})
