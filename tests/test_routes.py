from flask import Flask
from flask_restful import Api
import json

from backend.database.db import initialize_db
from backend.resources.routes import initialize_routes


#----------1-----------
def test_base_route(app, client):
    # app = Flask(__name__)
    # api = Api(app, catch_all_404s=True)
    # # Config
    # app.config['MONGODB_SETTINGS'] = {
    #     'host':
    #     'mongodb+srv://cicd-team:ec528@cicd-cluster0.s9vur.gcp.mongodb.net/doubly?retryWrites=true&w=majority'
    # }

    # initialize_db(app)
    # initialize_routes(api)
    # client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.headers[1] == ('Content-Length', '37')
    assert response.status_code == 500


#----------2-----------
def test_None_Existing_route(app, client):
    # app = Flask(__name__)
    # api = Api(app, catch_all_404s=True)
    # # Config
    # app.config['MONGODB_SETTINGS'] = {
    #     'host':
    #     'mongodb+srv://cicd-team:ec528@cicd-cluster0.s9vur.gcp.mongodb.net/doubly?retryWrites=true&w=majority'
    # }

    # initialize_db(app)
    # initialize_routes(api)
    # client = app.test_client()

    url = "/testNonExist"
    response = client.get(url)
    assert response.headers[1] == ("Content-Length", "17")
    # assert response.headers[2] == ('Location', 'https://www.youtube.com/')
    assert response.status_code == 400


#----------3-----------
#post a new test url1   post/get
def test_case1(app, client):
    # app = Flask(__name__)
    # api = Api(app, catch_all_404s=True)
    # # Config
    # app.config['MONGODB_SETTINGS'] = {
    #     'host':
    #     'mongodb+srv://cicd-team:ec528@cicd-cluster0.s9vur.gcp.mongodb.net/doubly?retryWrites=true&w=majority'
    # }

    # initialize_db(app)
    # initialize_routes(api)
    # client = app.test_client()
    url = '/'
    test_data = {
        "original_link": "https://www.UrlUnitTesting1.com/",
        "expire_at": "2020-9-30",
    }
    # post a new test url1
    response = client.post(
        "/", data=json.dumps(test_data), content_type="application/json"
    )

    # data = response.json()
    # (url, data = test_data)
    # assert response['expire_at'] == "2020-9-30"
    # assert response.headers[2] == ('Location', 'https://www.youtube.com/')
    assert response.status_code == 200

    link_id = response.json['link_id']
    response = client.get('/' + link_id)
    assert response.status_code == 302  #redirect response


#----------4-----------
#post a new test url2   post/get/delete
def test_case2(app, client):
    # app = Flask(__name__)
    # api = Api(app, catch_all_404s=True)
    # # Config
    # app.config['MONGODB_SETTINGS'] = {
    #     'host':
    #     'mongodb+srv://cicd-team:ec528@cicd-cluster0.s9vur.gcp.mongodb.net/doubly?retryWrites=true&w=majority'
    # }

    # initialize_db(app)
    # initialize_routes(api)
    # client = app.test_client()
    test_data = {
        "original_link": "https://www.UrlUnitTesting2.com/",
        "expire_at": "2020-10-28",
    }
    # post a new test url1
    response = client.post(
        "/", data=json.dumps(test_data), content_type="application/json"
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


#----------5-----------
#post a new test url3   post/get/delete
def test_case3(app, client):
    # app = Flask(__name__)
    # api = Api(app, catch_all_404s=True)
    # # Config
    # app.config['MONGODB_SETTINGS'] = {
    #     'host':
    #     'mongodb+srv://cicd-team:ec528@cicd-cluster0.s9vur.gcp.mongodb.net/doubly?retryWrites=true&w=majority'
    # }

    # initialize_db(app)
    # initialize_routes(api)
    # client = app.test_client()
    test_data = {
        "original_link": "https://www.UrlUnitTesting3.com/",
        "expire_at": "2020-10-28",
    }
    # post a new test url1
    response = client.post(
        "/", data=json.dumps(test_data), content_type="application/json"
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


#----------6-----------
#delete testing non-exist
def test_delete_nonexisting_case(app, client):
    # app = Flask(__name__)
    # api = Api(app, catch_all_404s=True)
    # # Config
    # app.config['MONGODB_SETTINGS'] = {
    #     'host':
    #     'mongodb+srv://cicd-team:ec528@cicd-cluster0.s9vur.gcp.mongodb.net/doubly?retryWrites=true&w=majority'
    # }

    # initialize_db(app)
    # initialize_routes(api)
>>>>>>> 0067213 (add pytest config file)
    client = app.test_client()
    response = client.delete("/ + " "testNonExist")
    assert response.headers[1] == ("Content-Length", "17")
    assert response.status_code == 400


# delete testing exist
