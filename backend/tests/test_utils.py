"""
Tests for utility functions
"""
import pytest
from src.utils import format_response, validate_request_data, get_timestamp


def test_get_timestamp():
    """Test timestamp generation"""
    timestamp = get_timestamp()
    assert isinstance(timestamp, str)
    assert 'T' in timestamp  # ISO format contains T


def test_format_response_success():
    """Test successful response formatting"""
    data = {'key': 'value'}
    response = format_response(data)
    
    assert response['status'] == 'success'
    assert response['data'] == data
    assert 'timestamp' in response


def test_format_response_with_message():
    """Test response formatting with message"""
    response = format_response(None, status='error', message='Test error')
    
    assert response['status'] == 'error'
    assert response['message'] == 'Test error'
    assert 'timestamp' in response


def test_validate_request_data_valid():
    """Test validation with valid data"""
    data = {'name': 'test', 'email': 'test@example.com'}
    required_fields = ['name', 'email']
    
    is_valid, error = validate_request_data(data, required_fields)
    assert is_valid is True
    assert error is None


def test_validate_request_data_missing_fields():
    """Test validation with missing fields"""
    data = {'name': 'test'}
    required_fields = ['name', 'email', 'password']
    
    is_valid, error = validate_request_data(data, required_fields)
    assert is_valid is False
    assert 'email' in error
    assert 'password' in error
