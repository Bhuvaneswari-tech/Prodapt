from app.repositories.category_repository import CategoryRepository
from app.schemas.category import CategorySchema, CategoryUpdate

class CategoryService:
    def __init__(self):
        self.repo = CategoryRepository()

    async def create_category(self, data: CategorySchema):
        return await self.repo.create(data.dict())

    async def get_category(self, category_id: str):
        return await self.repo.get(category_id)

    async def list_categories(self):
        return await self.repo.list()

    async def update_category(self, category_id: str, data: CategoryUpdate):
        await self.repo.update(category_id, data.dict(exclude_unset=True))

    async def delete_category(self, category_id: str):
        await self.repo.delete(category_id)
