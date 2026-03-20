
from app.models.product import Product
from typing import Optional
from pymongo.collection import Collection
from bson import ObjectId

class ProductRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def get_by_id(self, id: str) -> Optional[Product]:
        try:
            obj_id = ObjectId(id)
        except Exception:
            return None
        data = await self.collection.find_one({"_id": obj_id})
        if data:
            data["id"] = str(data["_id"])
            return Product(**data)
        return None

    async def create(self, product: Product) -> str:
        result = await self.collection.insert_one(product.dict())
        return str(result.inserted_id)
