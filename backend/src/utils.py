"""
Utility functions for the backend application
"""
from datetime import datetime


def get_timestamp():
    """Get current timestamp in ISO format"""
    return datetime.utcnow().isoformat()


def format_response(data, status='success', message=None):
    """Format API response"""
    response = {
        'status': status,
        'timestamp': get_timestamp()
    }
    
    if message:
        response['message'] = message
    
    if data is not None:
        response['data'] = data
    
    return response


def validate_request_data(data, required_fields):
    """Validate that required fields are present in request data"""
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    
    return True, None
