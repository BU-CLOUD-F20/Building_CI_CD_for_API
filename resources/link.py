# Import flask
from flask import redirect, jsonify, request
from flask_restful import Resource

# Import libraries
import string


class LinkAPI(Resource):
    def get(self, link_id):
        # get original URL from DB
        exist = True  # check from DB if the short link exist in DB
        if exist:
            return redirect('https://www.youtube.com/')
            # return redirect(original_link)
        return {'message': "The short link doesn't exist.", 'status': 404}

    def post(self):
        original_link = request.args.get('original_link')
        expire_date = request.args.get('expire_at')

        json_data = {"original_link": original_link, "expire_at": expire_date}
        # json data looks like this: (to be modified)
        # {
        #     "original_link": "https://www.youtube.com/",
        #     "expire_at" : "2020/9/30"
        # }
        # original_link = json_data['original_link']
        # checking URL validation
        try:
            if 'http://' not in json_data[
                    'original_link'] or 'https://' not in json_data[
                        'original_link']:
                original_link = 'http://' + original_link
                print(original_link)
            if '.com' not in json_data['original_link']:
                original_link = original_link + '.com'
                print(original_link)
            response = request.args.get(original_link)
            print("URL is valid and exists on the internet")
            # call to the short link generator
            short_link = self.short_link_generator()
            # TODO
            # Map short_link and json_data['original_link'] to DB
            return {
                'short_link': short_link,
                'expire_at': 'date',
            }
        except request.ConnectionError as exception:
            return {
                'message': json_data['original_link'] + " is not a valid URL",
                'status': 404,
            },

    def delete(self, link_id):
        # TODO
        # algo for deleting short_link
        return 'deleted'

    def short_link_generator(self):
        # TODO
        # Get INDEX of last url in the database. eg:
        index = 990000099999  # change this index to see what the algo looks like
        # index + 1 => the index of the new upcoming url
        short_link = self.encode(index + 1)  # 62^5 choices
        return short_link
        # exist = False
        # if exist:
        #     return self.short_linkGenerator()
        # return short_link

    def encode(self, index):  # from number to 62 bases eg: 1000000 => 15FTGg
        characters = string.digits + string.ascii_letters
        base = len(characters)
        ret = []
        while index > 0:
            val = index % base
            ret.append(characters[val])
            index = index // base
        return ''.join(ret[::-1])
