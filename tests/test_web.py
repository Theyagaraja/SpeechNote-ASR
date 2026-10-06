from app.main import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"SpeechNote" in response.data


def test_rejects_missing_upload():
    client = app.test_client()
    response = client.post("/transcribe-upload", data={}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Please select an audio file" in response.data
