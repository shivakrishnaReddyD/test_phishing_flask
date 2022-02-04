from urllib import response
from phishing.app import app

def test_get():
    response = app.test_client().get('/signin')
    assert response.status_code == 500

def test_post():
    response = app.test_client().post('/signin')
    assert response.status_code == 405