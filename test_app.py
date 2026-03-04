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
