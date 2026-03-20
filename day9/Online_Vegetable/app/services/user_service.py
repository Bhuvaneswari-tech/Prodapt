from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.schemas.user_schema import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def create_user(self, user_data: UserCreate):
        hashed_password = pwd_context.hash(user_data.password)
        user = User(username=user_data.username, email=user_data.email, hashed_password=hashed_password, 
                    role=user_data.role)
        return await self.repo.create(user)

    def get_user_by_email(self, email: str):
        return self.repo.get_by_email(email)
