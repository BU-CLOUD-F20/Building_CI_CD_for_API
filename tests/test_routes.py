import os
from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS
import json

from backend.database.db import initialize_db
from backend.resources.routes import initialize_routes


def create_app():
    # Initialization
    app = Flask(__name__, static_folder="ui/build")
    api = Api(app, catch_all_404s=True)
    cors = CORS(app, resources=r"/*")

    # Config
    app.config["MONGODB_SETTINGS"] = {
        "host": "mongodb+srv://cicd-team:ec528@cicd-cluster0.s9vur.gcp.mongodb.net/doubly?retryWrites=true&w=majority"
    }

    initialize_db(app)
    initialize_routes(api)

    return app


def test_base_route():
    app = create_app()
    client = app.test_client()
    url = "/"

    response = client.get(url)
    assert response.headers[1] == ("Content-Length", "136")
    # assert response.headers[2] == ('Location', 'https://www.youtube.com/')
    assert response.status_code == 404


# import json
def test_None_Existing_route():
    app = create_app()
    client = app.test_client()

    url = "/api/testNonExist"
    response = client.get(url)
    assert response.headers[1] == ("Content-Length", "136")
    # assert response.headers[2] == ('Location', 'https://www.youtube.com/')
    assert response.status_code == 404


# post a new test url1
def test_case1():
    app = create_app()
    client = app.test_client()
    url = "/api/"
    test_data = {
        "original_link": "https://www.UrlUnitTesting1.com/",
        "expire_at": "2020-9-30",
    }
    # post a new test url1
    response = client.post(
        "/api/", data=json.dumps(test_data), content_type="application/json"
    )

    # data = response.json()
    # (url, data = test_data)
    # assert response['expire_at'] == "2020-9-30"
    # assert response.headers[2] == ('Location', 'https://www.youtube.com/')
    assert response.status_code == 200

    link_id = response.json["link_id"]
    response = client.get("/" + link_id)
    assert response.status_code == 302  # redirect response


# post a new test url2
def test_case2():
    app = create_app()
    client = app.test_client()
    test_data = {
        "original_link": "https://www.UrlUnitTesting2.com/",
        "expire_at": "2020-10-28",
    }
    # post a new test url1
    response = client.post(
        "/api/", data=json.dumps(test_data), content_type="application/json"
    )

    # data = response.json()
    # (url, data = test_data)
    # assert response['expire_at'] == "2020-10-28"
    # assert response.headers[2] == ('Location', 'https://www.youtube.com/')
    assert response.status_code == 200

    link_id = response.json["link_id"]
    response = client.get("/" + link_id)
    assert response.status_code == 302

    response = client.delete("/" + link_id)
    assert response.status_code == 200


# post a new test url2
def test_case3():
    app = create_app()
    client = app.test_client()
    test_data = {
        "original_link": "https://www.UrlUnitTesting3.com/",
        "expire_at": "2020-10-28",
    }
    # post a new test url1
    response = client.post(
        "/api/", data=json.dumps(test_data), content_type="application/json"
    )

    # data = response.json()
    # (url, data = test_data)
    # assert response['expire_at'] == "2020-10-28"
    # assert response.headers[2] == ('Location', 'https://www.youtube.com/')
    assert response.status_code == 200

    link_id = response.json["link_id"]
    response = client.get("/" + link_id)
    assert response.status_code == 302

    response = client.delete("/" + link_id)
    assert response.status_code == 200


# ----------6-----------
# delete testing non-exist
def test_delete_nonexisting_case():
    app = create_app()
    client = app.test_client()
    response = client.delete("/ + " "testNonExist")
    assert response.headers[1] == ("Content-Length", "17")
    assert response.status_code == 400


# delete testing exist
