from phishing.app import app

def test_get_method():
    response = app.test_client().get('/logon')
    print(response.data)
    assert response.status_code == 200
    
    assert b'user' in response.data
    assert b'name' in response.data
    assert b'email' in response.data
    assert b'Mobile Number' in response.data
    assert b'password' in response.data

def test_exist():
    response = app.test_client().get('/lognon')
    print(response.data)
    assert response.status_code == 404

def test_post_method():
    response = app.test_client().post('/logon')
    print(response.data)
    assert response.status_code == 405

def test_text():
    response = app.test_client().get('/logon')
    print(response.data)
    assert response.status_code == 200
    assert b'name' in response.data
def test_post_method1():
    response = app.test_client().post('/logon')
    print(response.data)
    assert response.status_code == 405
    assert b'Register Here' not in response.data
    assert b'Method Not Allowed' in response.data

