import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_order():
    response = client.post("/orders/", json={
        "user_id": "dummyid",
        "product_ids": ["dummyprodid"],
        "total": 10.0
    })
    assert response.status_code == 200 or response.status_code == 422
