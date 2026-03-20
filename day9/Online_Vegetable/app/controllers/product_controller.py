from fastapi import APIRouter, Depends, HTTPException
from app.schemas.product_schema import ProductCreate, ProductOut
from app.services.product_service import ProductService
from app.core.dependencies import get_product_service

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=ProductOut)
async def create_product(product: ProductCreate, service: ProductService = Depends(get_product_service)):
    product_id = await service.create_product(product)
    return {"id": product_id, **product.dict()}

@router.get("/{id}", response_model=ProductOut)
async def get_product(id: str, service: ProductService = Depends(get_product_service)):
    product = await service.get_product_by_id(id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
