import pytest
import sys
import os

# Add parent directory to path to import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, db, User  # noqa: E402

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False # Disable CSRF for testing if implemented
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_index_redirect(client):
    """Test that root redirects to login when not authenticated."""
    rv = client.get('/')
    assert rv.status_code == 302
    assert '/login' in rv.location

def test_signup_and_login(client):
    """Test user signup and login flow."""
    # Signup
    rv = client.post('/signup', data=dict(name='TestUser', email='test@test.com', password='password'), follow_redirects=True)
    assert rv.status_code == 200
    
    # Login
    rv = client.post('/login', data=dict(name='TestUser', password='password'), follow_redirects=True)
    assert rv.status_code == 200
    assert b'TestUser' in rv.data  # Assuming dashboard shows username

def test_predict_endpoint_success_and_errors(client):
    """Test the /predict endpoint for success and various error conditions."""
    # Signup and login a user to get an authenticated session
    client.post('/signup', data=dict(name='ApiUser', email='api@test.com', password='password'))
    client.post('/login', data=dict(name='ApiUser', password='password'))

    # Test a successful prediction
    rv = client.post('/predict', json={'Amount': 100})
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['prediction'] == 'Not Fraud'
    assert 'probability' in json_data

    # Test a successful prediction with extra, unknown fields
    rv = client.post('/predict', json={'Amount': 200, 'V1': 0.5, 'V2': -1.2})
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['prediction'] == 'Not Fraud'
    assert 'probability' in json_data

    # Test invalid input (missing required field)
    rv = client.post('/predict', json={'NotAmount': 50})
    assert rv.status_code == 400
    json_data = rv.get_json()
    assert 'error' in json_data
    assert isinstance(json_data['error'], str)
    assert 'Amount: Missing data for required field.' in json_data['error']

    # Test validation error (amount <= 0)
    rv = client.post('/predict', json={'Amount': -50})
    assert rv.status_code == 400
    json_data = rv.get_json()
    assert 'error' in json_data
    assert isinstance(json_data['error'], str)
    assert 'Amount' in json_data['error']
