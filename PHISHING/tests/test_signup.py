from phishing.app import app
def test_get_method():
    response = app.test_client().get('/signup')
    print(response.data)
    #assert response.data == b'<!DOCTYPE html>\n<html lang="en">\n\n<head>\n\t<meta charset="utf-8">\n\t<title>Login</title>\n\n\t<!-- Google Fonts -->\n\t<link href=\'https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700|Lato:400,100,300,700,900\' rel=\'stylesheet\' type=\'text/css\'>\n\n\t<link rel="stylesheet" href="static/css/animate.css">\n\t<!-- Custom Stylesheet -->\n\t<link rel="stylesheet" href="static/css/style.css">\n\n\t<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>\n</head>\n\n<body>\n\t<div class="container">\n\t\t\n\t\t<div class="login-box animated fadeInUp">\n\t\t\t<div class="box-header">\n\t\t\t\t<h2>Log In</h2>\n\t\t\t</div>\n\t\t\t<form action="/signin" method="GET">\n\t\t\t<label for="username">Username</label>\n\t\t\t<br/>\n\t\t\t<input type="text" name="user" id="username">\n\t\t\t<br/>\n\t\t\t<label for="password">Password</label>\n\t\t\t<br/>\n\t\t\t<input type="password" name="password" id="password">\n\t\t\t<br/>\n\t\t\t<button type="submit">Sign In</button>\n\t\t</form>\n\t\t\t<br/>\n\t\t\t<a href="#"><p class="small">Forgot your password?</p></a>\n\t\t\t<p style="font-size: smaller;">Register here! <a href="/logon">Sign Up</a></p>\n\t\t</div>\n\t</div>\n</body>\n\n<script>\n\t$(document).ready(function () {\n    \t$(\'#logo\').addClass(\'animated fadeInDown\');\n    \t$("input:text:visible:first").focus();\n\t});\n\t$(\'#username\').focus(function() {\n\t\t$(\'label[for="username"]\').addClass(\'selected\');\n\t});\n\t$(\'#username\').blur(function() {\n\t\t$(\'label[for="username"]\').removeClass(\'selected\');\n\t});\n\t$(\'#password\').focus(function() {\n\t\t$(\'label[for="password"]\').addClass(\'selected\');\n\t});\n\t$(\'#password\').blur(function() {\n\t\t$(\'label[for="password"]\').removeClass(\'selected\');\n\t});\n</script>\n\n</html>'
    assert response.status_code == 200
    assert b'user' in response.data
    assert b'name' in response.data
    #assert b'email' in response.data
    #assert b'mobile' in response.data
    assert b'password' in response.data
    assert b'Sign In' in response.data
    assert b'Forgot your password?' in response.data

def test_post_method():
    response = app.test_client().get('/signup')
    print(response.data)
    assert response.status_code == 200 
    responce = app.test_client().post('/signup',data={'user':'a','email':'a@', 'password':'123','mobile':'9876655','name':'aa'} )

def test_post_method():
    response = app.test_client().post('/signup')
    print(response.data)
    assert response.status_code == 405
    '''
    assert b'user' in response.data
    assert b'name' in response.data
    assert b'email' in response.data
    assert b'mobile' in response.data
    assert b'password' in response.data
    assert b'Sign In' in response.data
    assert b'Forgot your password?' in response.data
    '''

