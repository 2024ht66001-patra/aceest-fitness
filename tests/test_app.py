import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    response = client.get('/')
    assert response.status_code == 200


def test_add_data(client):
    response = client.post('/add', json={'name': 'Test Item'})
    assert response.status_code == 201
    assert b"success" in response.data

def test_remove_data(client):
    # First, add an item to ensure there is something to delete
    add_response = client.post('/add', json={'name': 'Item to Delete'})
    item_id = add_response.get_json().get('id')
    # Now, delete the item
    delete_response = client.delete(f'/delete/{item_id}')
    assert delete_response.status_code == 200
    assert b"deleted" in delete_response.data