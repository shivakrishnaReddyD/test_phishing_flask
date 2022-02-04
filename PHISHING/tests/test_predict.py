from phishing.app import app

def test_get_method():
    response = app.test_client().get('/predict')
    print(response.data)
    assert response.status_code == 400
    
    #assert response.data == b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n'
    #assert b'Internal Server Error' in response.data
    #assert b'The server encountered an internal error and was unable to complete your request.' in response.data

def test_post_method():

    response = app.test_client().post('/predict')
    #,
                                #data=dict(message='hi hello.'),
                                #follow_redirects=True)
    assert response.status_code == 400
    #assert b'PhishingEmail Detector For SMS Messages' in response.data
    assert b'Machine Learning App with Flask' not in response.data


def test_msg_post():

    response = app.test_client().get('/predict',
                                data=dict(message='dskreddy123456'),
                                follow_redirects=True)
    assert response.status_code == 500

    #assert b'Machine Learning App with Flask' in response.data

def test_predict_p3():

    response = app.test_client().get('/predict',
                                data=dict(message='dskreddy123456'),
                                follow_redirects=True)
    assert response.status_code == 500

    assert b'Machine Learning App with Flask' not in response.data

def test_type():
    response = app.test_client().get('/predict')
    print(response.data)

    #assert response.content_type == text
    #assert response.json['Result'] == 39

