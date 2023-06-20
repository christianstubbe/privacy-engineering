# TODO: implement actual tests
from fastapi.testclient import TestClient
import pytest
from .app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

@pytest.mark.parametrize("item_id, query_param", [(1, "test"), (2, None)])
def test_read_item(item_id, query_param):
    response = client.get(f"/items/{item_id}", params={"query_param": query_param})
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "query_param": query_param}
