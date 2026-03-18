from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class OrderSchema(BaseModel):
    customer_id: str
    product_ids: List[str]
    total_amount: float
    order_date: datetime
    status: str

class OrderResponse(OrderSchema):
    id: str

class OrderUpdate(BaseModel):
    status: Optional[str] = None
