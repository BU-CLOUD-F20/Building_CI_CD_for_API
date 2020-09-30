# Import flask
from flask import redirect, jsonify, request
from flask_restful import Resource
from database.models import Link
from database.db import db

# Import libraries
import string
from datetime import date, datetime, timedelta

# Constants
WEBSITE_URL = "http://localhost:5000/"


class LinkAPI(Resource):
    def get(self, link_id):
        try:
            original_link = Link.objects.get_or_404(link_id=link_id)["original_link"]
            print("original_link", original_link)
            # return redirect(original_link)
            return jsonify(original_link=original_link)
        except:
            return "Link not found", 400
        return {"message": "The short link doesn't exist.", "status": 404}

    def post(self):
        original_link = request.args.get("original_link")
        expire_date = request.args.get("expire_at")

        json_data = {"original_link": original_link, "expire_at": expire_date}
        # json data looks like this: (to be modified)
        # {
        #     "original_link": "https://www.youtube.com/",
        #     "expire_at" : "2020-09/-30"
        # }
        # find way to validate url
        # original_link = json_data['original_link']
        # checking URL validation
        try:
            if (
                "http://" not in json_data["original_link"]
                or "https://" not in json_data["original_link"]
            ):
                original_link = "http://" + original_link
                print(original_link)
            if ".com" not in json_data["original_link"]:
                original_link = original_link + ".com"
                print(original_link)
            response = request.args.get(original_link)
            print("URL is valid and exists on the internet")
            short_link = self.short_link_generator()  # call to the short link generator
            # TODO
            # Map short_link and json_data['original_link'] to DB
            return {
                "short_link": short_link,
                "expire_at": "date",
            }
            Link(**data).save()
            response = jsonify(data)
            response.status_code = 200
            return response
        # except db.errors.DuplicateKeyError:

        except Exception as e:
            try:
                link_id = Link.objects.get_or_404(link_id=link_id)["link_id"]
                short_link = Link.objects.get_or_404(link_id=link_id)["short_link"]
                print("short_link", short_link)
                return (
                    jsonify(short_link=short_link, message="the url alreadt exist"),
                    201,
                )
            finally:
                print(e)
                return jsonify(link_id=link_id, short_link=short_link, message=str(e))
                # return 'Oops, something went wrong', 500

            # print(e)
            # return 'Oops, something went wrong', 500

    def delete(self, link_id):
        try:
            Link.objects.get(link_id=link_id).delete()
            return "Deleted", 200
        except:
            return "Link not found", 400

    def short_link_generator(self, original_link):
        # convert link to bytes then to int, grab only the last ten digits
        link_as_int = int.from_bytes(original_link.encode("utf-8"), byteorder="big") % (
            10 ** 10
        )
        link_id = self.encode(link_as_int)  # 62^5 choices
        return link_id

    def encode(self, index):  # from number to 62 bases eg: 1000000 => 15FTGg
        characters = string.digits + string.ascii_letters
        base = len(characters)
        ret = []
        while index > 0:
            val = index % base
            ret.append(characters[val])
            index = index // base
        return "".join(ret[::-1])
