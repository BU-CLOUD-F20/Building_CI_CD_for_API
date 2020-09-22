# Import flask
from flask import redirect, jsonify, request
from flask_restful import Resource


# Import libraries
import string


class ShortLink(Resource):
    # redirect to
    def get(self, link):
        shortLink = link
        # TODO
        # get original URL from DB
        exist = True  # check from DB if the short link exist in DB
        if exist:
            return redirect('https://www.youtube.com/')
            # return {
            # 'longLink': 'original url',
            # }
        return {
            'message': "The short link doesn't exist.",
            'status': 404,
        },


class LongLink(Resource):
    def get(self):
        return "Long Link"

    def post(self):
        json_data = request.get_json(force=True)
        # json data looks like this: (to be modified)
        # {
        #     "longLink": "https://www.youtube.com/",
        #     "expireAt" : "2020/9/30"
        # }
        longLink = json_data['longLink']
        # checking URL validation
        try:
            if 'http://' not in json_data['longLink'] or 'https://' not in json_data['longLink']:
                longLink = 'http://' + longLink
                print(longLink)
            if '.com' not in json_data['longLink']:
                longLink = longLink + '.com'
                print(longLink)
            response = request.get(longLink)
            print("URL is valid and exists on the internet")
            shortLink = self.shortLinkGenerator()  # call to the short link generator
            # TODO
            # Map shortLink and json_data['longLink'] to DB
            return {
                'shortLink': shortLink,
                'expireAt': 'date',
            }
        except request.ConnectionError as exception:
            return {
                'message': json_data['longLink'] + " is not a valid URL",
                'status': 404,
            },

    def delete(self, link):
        shortLink = link
        # TODO
        # algo for deleting ShortLink
        return 'deleted'

    def shortLinkGenerator(self):
        # TODO
        # Get INDEX of last url in the database. eg:
        index = 990000099999  # change this index to see what the algo looks like
        # index + 1 => the index of the new upcoming url
        shortLink = self.encode(index + 1)  # 62^5 choices
        return shortLink
        # exist = False
        # if exist:
        #     return self.shortLinkGenerator()
        # return shortLink

    def encode(self, index):  # from number to 62 bases eg: 1000000 => 15FTGg
        characters = string.digits + string.ascii_letters
        base = len(characters)
        ret = []
        while index > 0:
            val = index % base
            ret.append(characters[val])
            index = index // base
        return ''.join(ret[::-1])
