from fastapi import APIRouter, HTTPException
from app.services.customer_service import CustomerService
from app.schemas.customer import CustomerSchema, CustomerUpdate

router = APIRouter()
service = CustomerService()

@router.post("/", response_model=dict)
async def create_customer(customer: CustomerSchema):
    customer_id = await service.create_customer(customer)
    return {"id": customer_id}

@router.get("/{customer_id}", response_model=dict)
async def get_customer(customer_id: str):
    customer = await service.get_customer(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.get("/", response_model=list)
async def list_customers():
    return await service.list_customers()

@router.put("/{customer_id}")
async def update_customer(customer_id: str, customer: CustomerUpdate):
    await service.update_customer(customer_id, customer)
    return {"msg": "Customer updated"}

@router.delete("/{customer_id}")
async def delete_customer(customer_id: str):
    await service.delete_customer(customer_id)
    return {"msg": "Customer deleted"}
