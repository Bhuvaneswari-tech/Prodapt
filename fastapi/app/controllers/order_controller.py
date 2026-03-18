from fastapi import APIRouter, HTTPException
from app.services.order_service import OrderService
from app.schemas.order import OrderSchema, OrderUpdate

router = APIRouter()
service = OrderService()

@router.post("/", response_model=dict)
async def create_order(order: OrderSchema):
    order_id = await service.create_order(order)
    return {"id": order_id}

@router.get("/{order_id}", response_model=dict)
async def get_order(order_id: str):
    order = await service.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.get("/", response_model=list)
async def list_orders():
    return await service.list_orders()

@router.put("/{order_id}")
async def update_order(order_id: str, order: OrderUpdate):
    await service.update_order(order_id, order)
    return {"msg": "Order updated"}

@router.delete("/{order_id}")
async def delete_order(order_id: str):
    await service.delete_order(order_id)
    return {"msg": "Order deleted"}
