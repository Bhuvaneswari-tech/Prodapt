from app.repositories.order_repository import OrderRepository
from app.models.order import Order
from app.schemas.order_schema import OrderCreate


class OrderService:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    async def create_order(self, order_data: OrderCreate):
        order = Order(**order_data.dict(), status="pending")
        return await self.repo.create(order)

    async def get_order_by_id(self, id: str):
        return await self.repo.get_by_id(id)

#Business layer - Logic