import requests as r


def test_index():
    assert r.get("http://127.0.0.1:8000/").status_code == 200


def test_api():
    assert r.get("http://127.0.0.1:8000/api/").status_code == 200


def test_api_dealers():
    assert r.get("http://127.0.0.1:8000/api/dealers/").status_code == 200
