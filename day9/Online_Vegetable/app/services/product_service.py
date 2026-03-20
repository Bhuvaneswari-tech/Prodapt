from app.repositories.product_repository import ProductRepository
from app.models.product import Product
from app.schemas.product_schema import ProductCreate

class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    async def create_product(self, product_data: ProductCreate):
        product = Product(**product_data.dict())
        return await self.repo.create(product)

    async def get_product_by_id(self, id: str):
        return await self.repo.get_by_id(id)
