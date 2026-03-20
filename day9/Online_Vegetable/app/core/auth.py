from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.core.config import settings
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.core.dependencies import get_user_repository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token", scopes={})

# Dummy RBAC
roles_permissions = {
    "admin": ["admin", "user"],
    "user": ["user"]
}

def create_access_token(data: dict):
    return jwt.encode(data, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme), 
                          repo: UserRepository = Depends(get_user_repository)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, 
                             algorithms=[settings.JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await repo.get_by_email(email)
    if user is None:
        raise credentials_exception
    return user

def require_role(role: str):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role not in roles_permissions.get(role, []):
            raise HTTPException(status_code=403, detail="Insufficient permissions")
    return role_checker
