from app.repositories.order_repository import OrderRepository
from app.schemas.order import OrderSchema, OrderUpdate

class OrderService:
    def __init__(self):
        self.repo = OrderRepository()

    async def create_order(self, data: OrderSchema):
        return await self.repo.create(data.dict())

    async def get_order(self, order_id: str):
        return await self.repo.get(order_id)

    async def list_orders(self):
        return await self.repo.list()

    async def update_order(self, order_id: str, data: OrderUpdate):
        await self.repo.update(order_id, data.dict(exclude_unset=True))

    async def delete_order(self, order_id: str):
        await self.repo.delete(order_id)
