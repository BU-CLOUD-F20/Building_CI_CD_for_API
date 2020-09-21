from app import app
from flask_restful import Resource, Api

api = Api(app)

@app.route("/")
def index():
    return "Welcome to Doubly!"

class ShortLink(Resource):
    def get(self, link):
        shortLink = link
        return {
        'longLink': 'original url'
        }
    def post(self, link):
        longLink = link
        #algo for converting longLInk to ShortLink
        return {
        'shortLink': 'shortLink',
        'expireAt': 'date'
        }
    def delete(self, link):
        shortLink = link
        #algo for deleting ShortLink
        return 'deleted'

api.add_resource(ShortLink, '/<string:link>')
