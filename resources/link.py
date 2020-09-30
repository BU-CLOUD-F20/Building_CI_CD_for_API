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
            return redirect(original_link)
        except:
            return "Link not found", 400

    def post(self):
        request_data = request.get_json()
        original_link = request_data["original_link"]
        if "expire_at" in request_data:
            # add validation for date format later
            expire_at = request_data["expire_at"]
        else:
            # set default expire_at to 14 days from now
            expire_at = (
                (date.today() + timedelta(days=14))
                .strftime("%Y/%m/%d")
                .replace("/", "-")
            )
        # request looks like this:
        # {
        #     "original_link": "https://www.youtube.com/",
        #     "expire_at" : "2020-09/-30"
        # }
        # find way to validate url
        # original_link = json_data['original_link']
        # checking URL validation
        try:
            if "http://" not in original_link and "https://" not in original_link:
                original_link = "http://" + original_link
            link_id = self.short_link_generator(original_link)
            short_link = WEBSITE_URL + link_id
            data = {
                "original_link": original_link,
                "expire_at": expire_at,
                "short_link": short_link,
                "expire_at": "date",
            }
            Link(**data).save()

            return (
                {
                    "short_link": short_link,
                    "expire_at": expire_at,
                },
                201,
                {"Access-Control-Allow-Origin", "*"},
            )
        except Exception as e:
            print(e)
            return "Oops, something went wrong", 500

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