from app import create_app

def test_index_returns_200():
    app = create_app({"TESTING": True})
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Welcome" in resp.data
    