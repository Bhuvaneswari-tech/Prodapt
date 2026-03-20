from app.models.order import Order
from typing import Optional
from pymongo.collection import Collection

class OrderRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def get_by_id(self, id: str) -> Optional[Order]:
        from bson import ObjectId
        try:
            obj_id = ObjectId(id)
        except Exception:
            return None
        data = await self.collection.find_one({"_id": obj_id})
        if data:
            data["id"] = str(data["_id"])
            return Order(**data)
        return None

    async def create(self, order: Order) -> str:
        result = await self.collection.insert_one(order.dict())
        return str(result.inserted_id)
