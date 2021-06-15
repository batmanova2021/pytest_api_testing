import requests
import pytest


@pytest.mark.jsonplaceholdertest
def test_validate_response_code():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200
    assert 'application/json; charset=utf-8' in response.headers["Content-Type"]


@pytest.mark.jsonplaceholdertest
def test_validate_userid_and_id():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200
    assert 'application/json; charset=utf-8' in response.headers["Content-Type"]
    data = response.json()
    assert data[0]['userId'] == 1
    assert data[0]['id'] == 1
