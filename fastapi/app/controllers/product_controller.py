from fastapi import APIRouter, HTTPException
from app.services.product_service import ProductService
from app.schemas.product import ProductSchema, ProductUpdate

router = APIRouter()
service = ProductService()

@router.post("/", response_model=dict)
async def create_product(product: ProductSchema):
    product_id = await service.create_product(product)
    return {"id": product_id}

@router.get("/{product_id}", response_model=dict)
async def get_product(product_id: str):
    product = await service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/", response_model=list)
async def list_products():
    return await service.list_products()

@router.put("/{product_id}")
async def update_product(product_id: str, product: ProductUpdate):
    await service.update_product(product_id, product)
    return {"msg": "Product updated"}

@router.delete("/{product_id}")
async def delete_product(product_id: str):
    await service.delete_product(product_id)
    return {"msg": "Product deleted"}
