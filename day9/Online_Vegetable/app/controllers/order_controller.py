from fastapi import APIRouter, Depends
from app.schemas.order_schema import OrderCreate, OrderOut
from app.services.order_service import OrderService
from app.core.dependencies import get_order_service
from app.core.auth import get_current_user

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/", response_model=OrderOut)
async def create_order(order: OrderCreate, service: OrderService = Depends(get_order_service), 
                      current_user=Depends(get_current_user)):
    order_id = await service.create_order(order)
    return {"id": order_id, **order.dict(), "status": "pending"}


@router.get("/{id}", response_model=OrderOut)
async def get_order(id: str, service: OrderService = Depends(get_order_service)):
    return await service.get_order_by_id(id)
