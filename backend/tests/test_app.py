"""
Tests for the main application
"""
import pytest
from src.app import app


@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    """Test root endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'DevOps Pipeline Backend API'
    assert data['status'] == 'running'


def test_health(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['service'] == 'backend-api'


def test_get_data(client):
    """Test data endpoint"""
    response = client.get('/api/v1/data')
    assert response.status_code == 200
    data = response.get_json()
    assert 'data' in data
    assert len(data['data']) == 3
    assert data['data'][0]['id'] == 1


def test_not_found(client):
    """Test 404 error handling"""
    response = client.get('/nonexistent')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Not found'
