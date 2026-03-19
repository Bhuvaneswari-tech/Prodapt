def test_create_job(client):
    response = client.post("/jobs/", json={
        "title": "Python Developer",
        "description": "FastAPI + SQLAlchemy"
    })
    
    assert response.status_code == 200
    assert response.json()["title"] == "Python Developer"
    
def test_get_jobs(client):
    response = client.get("/jobs/")
    assert response.status_code == 200