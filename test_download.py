import pytest
from mock_flask_server import mock_file_server



@pytest.fixture
def client():
    app = mock_file_server()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_download_file(client):
	response = client.get('/uploads/hello.txt')
	assert response.status_code == 200
	print(dir(response))
	