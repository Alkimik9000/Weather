import pytest
from weather_app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_current_weather_route(client):
    response = client.get('/current-weather?city=London')
    assert response.status_code == 200
    assert 'city' in response.json
    assert response.json['city'] == 'London'

def test_future_weather_route(client):
    response = client.get('/future-weather?city=London&date=2024-12-25')
    assert response.status_code in [200, 404]  # The future date might or might not have data

def test_current_weather_route_no_city(client):
    response = client.get('/current-weather')
    assert response.status_code == 404

def test_future_weather_route_no_city(client):
    response = client.get('/future-weather?date=2024-12-25')
    assert response.status_code == 404
## testing if the CI pipeline works