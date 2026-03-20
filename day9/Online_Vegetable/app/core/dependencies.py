from app.repositories.user_repository import UserRepository
from app.repositories.product_repository import ProductRepository
from app.repositories.order_repository import OrderRepository
from app.services.user_service import UserService
from app.services.product_service import ProductService
from app.services.order_service import OrderService
from app.core.database import Database

# Dependency injection for repositories and services

def get_user_repository():
    db = Database.get_db()
    return UserRepository(db["users"])

def get_product_repository():
    db = Database.get_db()
    return ProductRepository(db["products"])

def get_order_repository():
    db = Database.get_db()
    return OrderRepository(db["orders"])

def get_user_service():
    return UserService(get_user_repository())

def get_product_service():
    return ProductService(get_product_repository())

def get_order_service():
    return OrderService(get_order_repository())
