from flask import Flask
from flask_restful import Api
import json

from database.db import initialize_db
from resources.routes import initialize_routes


def test_base_route_success():
    app = Flask(__name__)
    api = Api(app, catch_all_404s=True)
    # Config
    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb+srv://cicd-team:ec528@cicd-cluster0.s9vur.gcp.mongodb.net/doubly?retryWrites=true&w=majority'
    }

    initialize_db(app)
    initialize_routes(api)
    client = app.test_client()
    url ='/' + 'aaaa'

    response = client.get(url)
    assert response.headers[2] == ('Location', 'https://www.youtube.com/')
    assert response.status_code == 302 # redirect respond code to 'https://www.youtube.com/'
# import json


# def test_index(app, client):
#     res = client.get('/')
#     assert res.status_code == 200
#     expected = {'hello': 'world'}
#     assert expected == json.loads(res.get_data(as_text=True))