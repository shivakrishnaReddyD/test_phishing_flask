from app import app
import pytest

#import create_app
from db import init_db
import tempfile

def test_hello():
    response = app.test_client().get('/')
    print("anything")

    assert response.status_code == 200
    
    assert response.data == b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n    \n    <!-- SEO Meta Tags -->\n    <meta name="description" content="Your description">\n    <meta name="author" content="Your name">\n\n    <!-- OG Meta Tags to improve the way the post looks when you share the page on Facebook, Twitter, LinkedIn -->\n\t<meta property="og:site_name" content="" /> <!-- website name -->\n\t<meta property="og:site" content="" /> <!-- website link -->\n\t<meta property="og:title" content=""/> <!-- title shown in the actual shared post -->\n\t<meta property="og:description" content="" /> <!-- description shown in the actual shared post -->\n\t<meta property="og:image" content="" /> <!-- image link, make sure it\'s jpg -->\n\t<meta property="og:url" content="" /> <!-- where do you want your post to link to -->\n\t<meta name="twitter:card" content="summary_large_image"> <!-- to have large image post format in Twitter -->\n\n    <!-- Webpage Title -->\n    <title>Intro</title>\n    \n    <!-- Styles -->\n    <link rel="preconnect" href="https://fonts.gstatic.com">\n    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">\n    <link href="static/css/bootstrap.css" rel="stylesheet">\n    <link href="static/css/fontawesome-all.css" rel="stylesheet">\n    <link href="static/css/swiper.css" rel="stylesheet">\n\t<link href="static/css/magnific-popup.css" rel="stylesheet">\n\t<link href="static/css/styles.css" rel="stylesheet">\n\t\n\t<!-- Favicon  -->\n    <link rel="icon" href="static/images/favicon.png">\n</head>\n<body data-spy="scroll" data-target=".fixed-top">\n    \n    <!-- Navigation -->\n    <nav class="navbar navbar-expand-lg fixed-top navbar-light">\n        <div class="container">\n            \n            <!-- Text Logo - Use this if you don\'t have a graphic logo -->\n            <!-- <a class="navbar-brand logo-text page-scroll" href="index.html">Lomar</a> -->\n\n            <!-- Image Logo -->\n            <a class="navbar-brand logo-image" href="/"><img src="../static/images/download.svg" alt="alternative"></a> \n\n            <button class="navbar-toggler p-0 border-0" type="button" data-toggle="offcanvas">\n                <span class="navbar-toggler-icon"></span>\n            </button>\n\n            <div class="navbar-collapse offcanvas-collapse" id="navbarsExampleDefault">\n                <ul class="navbar-nav ml-auto">\n                    <li class="nav-item">\n                        <a class="nav-link page-scroll" href="/">Home <span class="sr-only">(current)</span></a>\n                    </li>\n                    <li class="nav-item">\n                        <a class="nav-link page-scroll" href="/logon">SignUp</a>\n                    </li>\n                    \n                </ul>\n                <span class="nav-item social-icons">\n                    <span class="fa-stack">\n                        <a href="#your-link">\n                            <i class="fas fa-circle fa-stack-2x"></i>\n                            <i class="fab fa-facebook-f fa-stack-1x"></i>\n                        </a>\n                    </span>\n                    <span class="fa-stack">\n                        <a href="#your-link">\n                            <i class="fas fa-circle fa-stack-2x"></i>\n                            <i class="fab fa-twitter fa-stack-1x"></i>\n                        </a>\n                    </span>\n                </span>\n            </div> <!-- end of navbar-collapse -->\n        </div> <!-- end of container -->\n    </nav> <!-- end of navbar -->\n    <!-- end of navigation -->\n\n\n    <!-- Header -->\n    <header class="ex-header">\n        <div class="container">\n            <div class="row">\n                <div class="col-xl-10 offset-xl-1">\n                    <h1>PHISHING E-MAILS DETECTION</h1>\n                    <br>\n                    <a class="btn-solid-reg mb-5" href="/logon">SignUp</a>\n                </div> <!-- end of col -->\n               \n            </div> <!-- end of row -->\n        </div> <!-- end of container -->\n    </header> <!-- end of ex-header -->\n    <!-- end of header -->\n\n\n    <!-- Basic -->\n    <div class="ex-basic-1 pt-5 pb-5">\n        <div class="container">\n            <div class="row">\n                <div class="col-lg-12">\n                    <img class="img-fluid mt-5 mb-3" src="static/images/1.jpg" width="1110" alt="alternative">\n                </div> <!-- end of col -->\n            </div> <!-- end of row -->\n        </div> <!-- end of container -->\n    </div> <!-- end of ex-basic-1 -->\n    <!-- end of basic -->\n\n\n    \n\n    \n\n\n    <!-- Footer -->\n    <div class="footer">\n        <div class="container">\n             <!-- Copyright -->\n    <div class="copyright">\n        <div class="container">\n            <div class="row">\n                <div class="col-lg-12">\n                    <p class="p-small">Copyright \xc2\xa9 <a href="#your-link">2021</a></p>\n                </div> <!-- end of col -->\n            </div> <!-- enf of row -->\n        </div> <!-- end of container -->\n    </div> <!-- end of copyright --> \n    <!-- end of copyright -->\n        </div> <!-- end of container -->\n    </div> <!-- end of footer -->  \n    <!-- end of footer -->\n\n\n   \n    \n    \t\n    <!-- Scripts -->\n    <script src="static/js/jquery.min.js"></script> <!-- jQuery for Bootstrap\'s JavaScript plugins -->\n    <script src="static/js/bootstrap.min.js"></script> <!-- Bootstrap framework -->\n    <script src="static/js/jquery.easing.min.js"></script> <!-- jQuery Easing for smooth scrolling between anchors -->\n    <script src="static/js/jquery.magnific-popup.js"></script> <!-- Magnific Popup for lightboxes -->\n    <script src="static/js/swiper.min.js"></script> <!-- Swiper for image and text sliders -->\n    <script src="static/js/scripts.js"></script> <!-- Custom scripts -->\n</body>\n</html>'
    assert b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n    \n    <!-- SEO Meta Tags -->\n    <meta name="description" content="Your description">\n    <meta name="author" content="Your name">\n\n    <!-- OG Meta Tags to improve the way the post looks when you share the page on Facebook, Twitter, LinkedIn -->\n\t<meta property="og:site_name" content="" /> <!-- website name -->\n\t<meta property="og:site" content="" /> <!-- website link -->\n\t<meta property="og:title" content=""/> <!-- title shown in the actual shared post -->\n\t<meta property="og:description" content="" /> <!-- description shown in the actual shared post -->\n\t<meta property="og:image" content="" /> <!-- image link, make sure it\'s jpg -->\n\t<meta property="og:url" content="" /> <!-- where do you want your post to link to -->\n\t<meta name="twitter:card" content="summary_large_image"> <!-- to have large image post format in Twitter -->\n\n    <!-- Webpage Title -->\n    <title>Intro</title>\n    \n    <!-- Styles -->\n    <link rel="preconnect" href="https://fonts.gstatic.com">\n    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">\n    <link href="static/css/bootstrap.css" rel="stylesheet">\n    <link href="static/css/fontawesome-all.css" rel="stylesheet">\n    <link href="static/css/swiper.css" rel="stylesheet">\n\t<link href="static/css/magnific-popup.css" rel="stylesheet">\n\t<link href="static/css/styles.css" rel="stylesheet">\n\t\n\t<!-- Favicon  -->\n    <link rel="icon" href="static/images/favicon.png">\n</head>\n<body data-spy="scroll" data-target=".fixed-top">\n    \n    <!-- Navigation -->\n    <nav class="navbar navbar-expand-lg fixed-top navbar-light">\n        <div class="container">\n            \n            <!-- Text Logo - Use this if you don\'t have a graphic logo -->\n            <!-- <a class="navbar-brand logo-text page-scroll" href="index.html">Lomar</a> -->\n\n            <!-- Image Logo -->\n            <a class="navbar-brand logo-image" href="/"><img src="../static/images/download.svg" alt="alternative"></a> \n\n            <button class="navbar-toggler p-0 border-0" type="button" data-toggle="offcanvas">\n                <span class="navbar-toggler-icon"></span>\n            </button>\n\n            <div class="navbar-collapse offcanvas-collapse" id="navbarsExampleDefault">\n                <ul class="navbar-nav ml-auto">\n                    <li class="nav-item">\n                        <a class="nav-link page-scroll" href="/">Home <span class="sr-only">(current)</span></a>\n                    </li>\n                    <li class="nav-item">\n                        <a class="nav-link page-scroll" href="/logon">SignUp</a>\n                    </li>\n                    \n                </ul>\n                <span class="nav-item social-icons">\n                    <span class="fa-stack">\n                        <a href="#your-link">\n                            <i class="fas fa-circle fa-stack-2x"></i>\n                            <i class="fab fa-facebook-f fa-stack-1x"></i>\n                        </a>\n                    </span>\n                    <span class="fa-stack">\n                        <a href="#your-link">\n                            <i class="fas fa-circle fa-stack-2x"></i>\n                            <i class="fab fa-twitter fa-stack-1x"></i>\n                        </a>\n                    </span>\n                </span>\n            </div> <!-- end of navbar-collapse -->\n        </div> <!-- end of container -->\n    </nav> <!-- end of navbar -->\n    <!-- end of navigation -->\n\n\n    <!-- Header -->\n    <header class="ex-header">\n        <div class="container">\n            <div class="row">\n                <div class="col-xl-10 offset-xl-1">\n                    <h1>PHISHING E-MAILS DETECTION</h1>\n                    <br>\n                    <a class="btn-solid-reg mb-5" href="/logon">SignUp</a>\n                </div> <!-- end of col -->\n               \n            </div> <!-- end of row -->\n        </div> <!-- end of container -->\n    </header> <!-- end of ex-header -->\n    <!-- end of header -->\n\n\n    <!-- Basic -->\n    <div class="ex-basic-1 pt-5 pb-5">\n        <div class="container">\n            <div class="row">\n                <div class="col-lg-12">\n                    <img class="img-fluid mt-5 mb-3" src="static/images/1.jpg" width="1110" alt="alternative">\n                </div> <!-- end of col -->\n            </div> <!-- end of row -->\n        </div> <!-- end of container -->\n    </div> <!-- end of ex-basic-1 -->\n    <!-- end of basic -->\n\n\n    \n\n    \n\n\n    <!-- Footer -->\n    <div class="footer">\n        <div class="container">\n             <!-- Copyright -->\n    <div class="copyright">\n        <div class="container">\n            <div class="row">\n                <div class="col-lg-12">\n                    <p class="p-small">Copyright \xc2\xa9 <a href="#your-link">2021</a></p>\n                </div> <!-- end of col -->\n            </div> <!-- enf of row -->\n        </div> <!-- end of container -->\n    </div> <!-- end of copyright --> \n    <!-- end of copyright -->\n        </div> <!-- end of container -->\n    </div> <!-- end of footer -->  \n    <!-- end of footer -->\n\n\n   \n    \n    \t\n    <!-- Scripts -->\n    <script src="static/js/jquery.min.js"></script> <!-- jQuery for Bootstrap\'s JavaScript plugins -->\n    <script src="static/js/bootstrap.min.js"></script> <!-- Bootstrap framework -->\n    <script src="static/js/jquery.easing.min.js"></script> <!-- jQuery Easing for smooth scrolling between anchors -->\n    <script src="static/js/jquery.magnific-popup.js"></script> <!-- Magnific Popup for lightboxes -->\n    <script src="static/js/swiper.min.js"></script> <!-- Swiper for image and text sliders -->\n    <script src="static/js/scripts.js"></script> <!-- Custom scripts -->\n</body>\n</html>'
    #print(response.data)
    #assert False 


def test_app1():
    response = app.test_client().get('/')
    assert response.data == b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n    \n    <!-- SEO Meta Tags -->\n    <meta name="description" content="Your description">\n    <meta name="author" content="Your name">\n\n    <!-- OG Meta Tags to improve the way the post looks when you share the page on Facebook, Twitter, LinkedIn -->\n\t<meta property="og:site_name" content="" /> <!-- website name -->\n\t<meta property="og:site" content="" /> <!-- website link -->\n\t<meta property="og:title" content=""/> <!-- title shown in the actual shared post -->\n\t<meta property="og:description" content="" /> <!-- description shown in the actual shared post -->\n\t<meta property="og:image" content="" /> <!-- image link, make sure it\'s jpg -->\n\t<meta property="og:url" content="" /> <!-- where do you want your post to link to -->\n\t<meta name="twitter:card" content="summary_large_image"> <!-- to have large image post format in Twitter -->\n\n    <!-- Webpage Title -->\n    <title>Intro</title>\n    \n    <!-- Styles -->\n    <link rel="preconnect" href="https://fonts.gstatic.com">\n    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet">\n    <link href="static/css/bootstrap.css" rel="stylesheet">\n    <link href="static/css/fontawesome-all.css" rel="stylesheet">\n    <link href="static/css/swiper.css" rel="stylesheet">\n\t<link href="static/css/magnific-popup.css" rel="stylesheet">\n\t<link href="static/css/styles.css" rel="stylesheet">\n\t\n\t<!-- Favicon  -->\n    <link rel="icon" href="static/images/favicon.png">\n</head>\n<body data-spy="scroll" data-target=".fixed-top">\n    \n    <!-- Navigation -->\n    <nav class="navbar navbar-expand-lg fixed-top navbar-light">\n        <div class="container">\n            \n            <!-- Text Logo - Use this if you don\'t have a graphic logo -->\n            <!-- <a class="navbar-brand logo-text page-scroll" href="index.html">Lomar</a> -->\n\n            <!-- Image Logo -->\n            <a class="navbar-brand logo-image" href="/"><img src="../static/images/download.svg" alt="alternative"></a> \n\n            <button class="navbar-toggler p-0 border-0" type="button" data-toggle="offcanvas">\n                <span class="navbar-toggler-icon"></span>\n            </button>\n\n            <div class="navbar-collapse offcanvas-collapse" id="navbarsExampleDefault">\n                <ul class="navbar-nav ml-auto">\n                    <li class="nav-item">\n                        <a class="nav-link page-scroll" href="/">Home <span class="sr-only">(current)</span></a>\n                    </li>\n                    <li class="nav-item">\n                        <a class="nav-link page-scroll" href="/logon">SignUp</a>\n                    </li>\n                    \n                </ul>\n                <span class="nav-item social-icons">\n                    <span class="fa-stack">\n                        <a href="#your-link">\n                            <i class="fas fa-circle fa-stack-2x"></i>\n                            <i class="fab fa-facebook-f fa-stack-1x"></i>\n                        </a>\n                    </span>\n                    <span class="fa-stack">\n                        <a href="#your-link">\n                            <i class="fas fa-circle fa-stack-2x"></i>\n                            <i class="fab fa-twitter fa-stack-1x"></i>\n                        </a>\n                    </span>\n                </span>\n            </div> <!-- end of navbar-collapse -->\n        </div> <!-- end of container -->\n    </nav> <!-- end of navbar -->\n    <!-- end of navigation -->\n\n\n    <!-- Header -->\n    <header class="ex-header">\n        <div class="container">\n            <div class="row">\n                <div class="col-xl-10 offset-xl-1">\n                    <h1>PHISHING E-MAILS DETECTION</h1>\n                    <br>\n                    <a class="btn-solid-reg mb-5" href="/logon">SignUp</a>\n                </div> <!-- end of col -->\n               \n            </div> <!-- end of row -->\n        </div> <!-- end of container -->\n    </header> <!-- end of ex-header -->\n    <!-- end of header -->\n\n\n    <!-- Basic -->\n    <div class="ex-basic-1 pt-5 pb-5">\n        <div class="container">\n            <div class="row">\n                <div class="col-lg-12">\n                    <img class="img-fluid mt-5 mb-3" src="static/images/1.jpg" width="1110" alt="alternative">\n                </div> <!-- end of col -->\n            </div> <!-- end of row -->\n        </div> <!-- end of container -->\n    </div> <!-- end of ex-basic-1 -->\n    <!-- end of basic -->\n\n\n    \n\n    \n\n\n    <!-- Footer -->\n    <div class="footer">\n        <div class="container">\n             <!-- Copyright -->\n    <div class="copyright">\n        <div class="container">\n            <div class="row">\n                <div class="col-lg-12">\n                    <p class="p-small">Copyright \xc2\xa9 <a href="#your-link">2021</a></p>\n                </div> <!-- end of col -->\n            </div> <!-- enf of row -->\n        </div> <!-- end of container -->\n    </div> <!-- end of copyright --> \n    <!-- end of copyright -->\n        </div> <!-- end of container -->\n    </div> <!-- end of footer -->  \n    <!-- end of footer -->\n\n\n   \n    \n    \t\n    <!-- Scripts -->\n    <script src="static/js/jquery.min.js"></script> <!-- jQuery for Bootstrap\'s JavaScript plugins -->\n    <script src="static/js/bootstrap.min.js"></script> <!-- Bootstrap framework -->\n    <script src="static/js/jquery.easing.min.js"></script> <!-- jQuery Easing for smooth scrolling between anchors -->\n    <script src="static/js/jquery.magnific-popup.js"></script> <!-- Magnific Popup for lightboxes -->\n    <script src="static/js/swiper.min.js"></script> <!-- Swiper for image and text sliders -->\n    <script src="static/js/scripts.js"></script> <!-- Custom scripts -->\n</body>\n</html>'
    
def test_app2():
    response = app.test_client().get('/logon')
    print(response.data)
    assert response.data == b'<!DOCTYPE html>\n<html lang="en">\n\n<head>\n\t<meta charset="utf-8">\n\t<title>Logon</title>\n\n\t<!-- Google Fonts -->\n\t<link href=\'https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700|Lato:400,100,300,700,900\' rel=\'stylesheet\' type=\'text/css\'>\n\n\t<link rel="stylesheet" href="static/css/animate.css">\n\t<!-- Custom Stylesheet -->\n\t<link rel="stylesheet" href="static/css/style.css">\n\n\t<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>\n</head>\n\n<body>\n\t<div class="container">\n\t\t\n\t\t<div class="login-box animated fadeInUp">\n\t\t\t<div class="box-header">\n\t\t\t\t<h2>Register Here</h2>\n\t\t\t</div>\n\t\t\t<form action="/signup" method="GET">\n\t\t\t<label for="username">Username</label>\n\t\t\t<br/>\n\t\t\t<input type="text" name="user" id="username">\n\t\t\t<br/>\n\t\t\t<label for="name">Name</label>\n\t\t\t<br/>\n\t\t\t<input type="text" name="name" id="name">\n\t\t\t<br/>\n\t\t\t<label for="email">Email</label>\n\t\t\t<br/>\n\t\t\t<input type="text" name="email" id="email">\n\t\t\t<br/>\n\t\t\t<label for="mobile">Mobile Number</label>\n\t\t\t<br/>\n\t\t\t<input type="text" name="mobile" id="mobile">\n\t\t\t<br/>\n\t\t\t\n\t\t\t<label for="password">Password</label>\n\t\t\t<br/>\n\t\t\t<input type="password" name="password" id="password">\n\t\t\t<br/>\n\t\t\t<button type="submit">Sign Up</button>\n\t\t</form>\n\t\t\t<br/>\n\t\t\t\n\t\t\t<p style="font-size: smaller;">Login here! <a href="/login">Sign in</a></p>\n\t\t</div>\n\t</div>\n</body>\n\n<script>\n\t$(document).ready(function () {\n    \t$(\'#logo\').addClass(\'animated fadeInDown\');\n    \t$("input:text:visible:first").focus();\n\t});\n\t$(\'#username\').focus(function() {\n\t\t$(\'label[for="username"]\').addClass(\'selected\');\n\t});\n\t$(\'#username\').blur(function() {\n\t\t$(\'label[for="username"]\').removeClass(\'selected\');\n\t});\n\t$(\'#password\').focus(function() {\n\t\t$(\'label[for="password"]\').addClass(\'selected\');\n\t});\n\t$(\'#password\').blur(function() {\n\t\t$(\'label[for="password"]\').removeClass(\'selected\');\n\t});\n</script>\n\n</html>'
     #print(response.data)



def test_predict():
    response = app.test_client().get('/predict')
    print(response.data)
    assert response.status_code == 500
    #assert response.data == b'<!DOCTYPE html>'

def test_signin_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'Email' in response.data
    assert b'Password' in response.data

def test_valid_signin_logout(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login',
                                data=dict(email='patkennedy79@gmail.com', password='FlaskIsAwesome'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for logging in, patkennedy79@gmail.com!' in response.data
    assert b'Flask User Management' in response.data
    assert b'Logout' in response.data
    assert b'Login' not in response.data
    assert b'Register' not in response.data






    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """

'''
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Goodbye!' in response.data
    assert b'Flask User Management' in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data




@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({'TESTING': True, 'DATABASE': db_path})

    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_login_logout(client):
    """Make sure login and logout works."""

    username = flaskr.app.config["USERNAME"]
    password = flaskr.app.config["PASSWORD"]

    rv = login(client, username, password)
    assert b'You were logged in' in rv.data

    rv = logout(client)
    assert b'You were logged out' in rv.data

    rv = login(client, f"{username}x", password)
    assert b'Invalid username' in rv.data

    rv = login(client, username, f'{password}x')
    assert b'Invalid password' in rv.data




def test_signup():
    #response = app.test_client().get('/signup')
    print("anything")

    assert app.test_client().get('/signup').status_code == 200

    response = app.test_client.post("/signup", data={"username": "a", "password": "a"})
    assert "http://localhost/signup" == response.headers["Location"]

    with app.app_context():
        assert (
            get_db().execute("SELECT * FROM user WHERE username = 'a'").fetchone()
            is not None
        )


@pytest.mark.parametrize(
    ("username", "password", "message"),
    (
        ("", "", b"Username is required."),
        ("a", "", b"Password is required."),
        ("test", "test", b"already registered"),
    ),
)
def test_register_validate_input(test_client, username, password, message):
    response = client.post(
        "/auth/register", data={"username": username, "password": password}
    )
    assert message in response.data


################################################################################
def test_hello1():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'hello world!'


def test_hello2():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello World!'
'''
