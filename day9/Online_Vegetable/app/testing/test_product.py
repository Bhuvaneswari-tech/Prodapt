import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products/", json={
        "name": "Tomato",
        "price": 2.5,
        "stock": 100
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Tomato"
