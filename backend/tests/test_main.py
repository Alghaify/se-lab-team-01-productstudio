from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'


def test_rejects_unsupported_upload():
    response = client.post(
        '/api/images/upload',
        files={'file': ('notes.txt', b'not an image', 'text/plain')},
    )
    assert response.status_code == 400
