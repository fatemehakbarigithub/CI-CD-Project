from main import app
def testing():
    response = app.test_client().get('/')
    assert response.status_code == 200

