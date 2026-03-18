from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductSchema, ProductUpdate

class ProductService:
    def __init__(self):
        self.repo = ProductRepository()

    async def create_product(self, data: ProductSchema):
        return await self.repo.create(data.dict())

    async def get_product(self, product_id: str):
        return await self.repo.get(product_id)

    async def list_products(self):
        return await self.repo.list()

    async def update_product(self, product_id: str, data: ProductUpdate):
        await self.repo.update(product_id, data.dict(exclude_unset=True))

    async def delete_product(self, product_id: str):
        await self.repo.delete(product_id)
