# Import flask
from flask import redirect, jsonify, request
from flask_restful import Resource


class ShortLink(Resource):
    # redirect to
    def get(self, link):
        shortLink = link
        # TODO
        # get original URL from DB
        exist = False  # check from DB if the short link exist in DB
        if exist:
            return redirect('https://www.youtube.com/')
            # return {
            # 'longLink': 'original url',
            # }
        return {
            'message': "The short link doesn't exist.",
            'status': 404,
        },
