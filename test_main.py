from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is in the file named 'main.py'

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": None}


def test_read_item_with_query_param():
    response = client.get("/items/42?q=testquery")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "testquery"}
