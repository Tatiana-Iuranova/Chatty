from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_post():
    response = client.post("/posts", json={"title": "Test Post", "content": "Test Content"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Post"

def test_get_posts():
    response = client.get("/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_post_not_found():
    response = client.get("/posts/999")
    assert response.status_code == 404