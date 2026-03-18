from fastapi import APIRouter, HTTPException
from app.services.category_service import CategoryService
from app.schemas.category import CategorySchema, CategoryUpdate

router = APIRouter()
service = CategoryService()

@router.post("/", response_model=dict)
async def create_category(category: CategorySchema):
    category_id = await service.create_category(category)
    return {"id": category_id}

@router.get("/{category_id}", response_model=dict)
async def get_category(category_id: str):
    category = await service.get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.get("/", response_model=list)
async def list_categories():
    return await service.list_categories()

@router.put("/{category_id}")
async def update_category(category_id: str, category: CategoryUpdate):
    await service.update_category(category_id, category)
    return {"msg": "Category updated"}

@router.delete("/{category_id}")
async def delete_category(category_id: str):
    await service.delete_category(category_id)
    return {"msg": "Category deleted"}
