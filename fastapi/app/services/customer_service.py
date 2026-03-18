from app.repositories.customer_repository import CustomerRepository
from app.schemas.customer import CustomerSchema, CustomerUpdate

class CustomerService:
    def __init__(self):
        self.repo = CustomerRepository()

    async def create_customer(self, data: CustomerSchema):
        return await self.repo.create(data.dict())

    async def get_customer(self, customer_id: str):
        return await self.repo.get(customer_id)

    async def list_customers(self):
        return await self.repo.list()

    async def update_customer(self, customer_id: str, data: CustomerUpdate):
        await self.repo.update(customer_id, data.dict(exclude_unset=True))

    async def delete_customer(self, customer_id: str):
        await self.repo.delete(customer_id)
