from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all_blogs():
    response = client.get("/blog/all")
    assert response.status_code == 200


def test_auth_error():
    response = client.post("/token", data={"username": "", "password": ""})
    access_token = response.json().get("access_token")
    assert access_token == None
    message = response.json().get("detail")
    assert message == "Invalid credentials"


def test_auth_success():
    response = client.post("/token", data={"username": "vim", "password": "vim"})
    access_token = response.json().get("access_token")
    assert access_token

    response = client.post(
        "/article",
        json={
            "title": "test",
            "content": "test",
            "published": True,
            "creater_id": 2,
        },
        headers={"Authorization": "Bearer" + access_token},
    )
    # print(response.json())
    # Not working need to be fixed
    # assert response.status_code == 200
    # assert response.json().get("title") == "test"
