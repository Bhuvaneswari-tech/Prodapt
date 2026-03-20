from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user_schema import UserCreate, UserOut
from app.services.user_service import UserService
from app.core.dependencies import get_user_service
from app.core.auth import get_current_user, require_role

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserOut)
async def register(user: UserCreate, service: UserService = Depends(get_user_service)):
    user_id = await service.create_user(user)
    return {"id": user_id, **user.dict()}

@router.get("/me", response_model=UserOut)
async def get_me(current_user=Depends(get_current_user)):
    return current_user

@router.get("/admin", dependencies=[Depends(require_role("admin"))])
def admin_only():
    return {"msg": "Admin access granted"}
