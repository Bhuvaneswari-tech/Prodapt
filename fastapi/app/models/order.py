from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Order(BaseModel):
    id: Optional[str]
    customer_id: str
    product_ids: list[str]
    total_amount: float
    order_date: datetime
    status: str
