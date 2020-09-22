# Import resources
from app import app
from resources.short_link import ShortLink
from resources.long_link import LongLink

# Import flask
from flask_restful import Api

api = Api(app, catch_all_404s=True)


@app.route("/")
def index():
    return "Welcome to Doubly!"


api.add_resource(LongLink, '/long')
api.add_resource(ShortLink, '/short', '/short/<string:link>')
