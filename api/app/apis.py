from app import app
from flask import redirect, jsonify, request
from flask_restful import Resource, Api
import string
from random import choices
api = Api(app, catch_all_404s=True)

@app.route("/")
def index():
    return "Welcome to Doubly!"

class ShortLink(Resource):
    #redirect to  
    def get(self, link):
        shortLink = link
        #TODO 
        #get original URL from DB
        exist = False # check from DB if the short link exist in DB
        if exist:
            return redirect('https://www.youtube.com/')
            # return {
            # 'longLink': 'original url',
            # }
        return {
            'message': "The short link doesn't exist.",
            'status': 404,
        },
        

class PostLongLink(Resource):
    def post(self):    
        json_data = request.get_json(force=True) 
        # json data looks like this: (to be modified)
        # {
	    #     "longLink": "https://www.youtube.com/",
	    #     "expireAt" : "2020/9/30"
        # }  
        shortLink = self.shortLinkGenerator() #call to the short link generator 
        #TODO 
        #Map shortLink and json_data['longLink'] to DB
        return {
            'shortLink': shortLink,
            'expireAt': 'date',
            }
    def delete(self, link):
        shortLink = link
        # TODO
        #algo for deleting ShortLink
        return 'deleted'
    def shortLinkGenerator(self):
        #TODO 
        # Get INDEX of last url in the database. eg:
        index = 990000099999 #change this index to see what the algo looks like
        # index + 1 => the index of the new upcoming url 
        shortLink = self.encode(index + 1) #62^5 choices
        return shortLink
        # exist = False
        # if exist:
        #     return self.shortLinkGenerator()
        # return shortLink
    def encode(self, index):    #from number to 62 bases eg: 1000000 => 15FTGg
        characters = string.digits + string.ascii_letters
        base = len(characters)
        ret = []
        while index > 0:
            val = index % base
            ret.append(characters[val])
            index = index // base
        return ''.join(ret[::-1])

api.add_resource(PostLongLink, '/postLongLink')     
api.add_resource(ShortLink, '/<string:link>')
