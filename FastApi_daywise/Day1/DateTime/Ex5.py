from typing import Dict

def register_user(user: Dict[str, int]):
    return f"User {user['name']} registered"

print(register_user({"name": "100"}))