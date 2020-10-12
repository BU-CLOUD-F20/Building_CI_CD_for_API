from flask import Flask
import json


# ----------1----------
def test_base_route(app, client):
    url = "/"
    response = client.get(url)
    # assert response.headers[1] == ('Content-Length', '17')
    assert response.status_code == 200


# ----------2-----------
def test_None_Existing_route(app, client):

    url = "/api/testNonExist"
    response = client.get(url)
    # assert response.headers[1] == ('Content-Length', '136')
    # redirect back to base route
    assert response.status_code == 200


# ----------3-----------
# post a new test url1   post/get
def test_case1(app, client):
    url = "/"
    test_data = {
        "original_link": "https://www.UrlUnitTesting1.com/",
        "expire_at": "2020-9-30",
    }
    # post a new test url1
    response = client.post(
        "/api/", data=json.dumps(test_data), content_type="application/json"
    )

    assert response.status_code == 200

    link_id = response.json["link_id"]
    response = client.get("/" + link_id)
    assert response.status_code == 302  # redirect response


# ----------4-----------
# post a new test url2   post/get/delete
def test_case2(app, client):
    test_data = {
        "original_link": "https://www.UrlUnitTesting2.com/",
        "expire_at": "2020-10-28",
    }
    # post a new test url1
    response = client.post(
        "/api/", data=json.dumps(test_data), content_type="application/json"
    )

    assert response.status_code == 200

    link_id = response.json["link_id"]
    response = client.get("/" + link_id)
    assert response.status_code == 302

    response = client.delete("/" + link_id)
    assert response.status_code == 200


# ----------5-----------
# post a new test url3   post/get/delete
def test_case3(app, client):
    test_data = {
        "original_link": "https://www.UrlUnitTesting3.com/",
        "expire_at": "2020-10-28",
    }
    # post a new test url1
    response = client.post(
        "/api/", data=json.dumps(test_data), content_type="application/json"
    )

    assert response.status_code == 200

    link_id = response.json["link_id"]
    response = client.get("/" + link_id)
    assert response.status_code == 302

    response = client.delete("/" + link_id)
    assert response.status_code == 200


# ----------6-----------
# delete testing non-exist
def test_delete_nonexisting_case(app, client):

    client = app.test_client()
    response = client.delete("/ + " "testNonExist")
    assert response.headers[1] == ("Content-Length", "17")
    assert response.status_code == 400
