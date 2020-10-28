# Import flask
from flask import redirect, jsonify, request
from flask_restful import Resource
from backend.database.models import Link
from backend.database.db import db

# Import libraries
import string
from datetime import date, datetime, timedelta

# Constants
# WEBSITE_URL = 'http://localhost:5000/'
WEBSITE_URL = "http://buildingcicdforapi-ece-528-building-ci-cd-for-api.k-apps.osh.massopen.cloud/"


class BaseAPI(Resource):
    def get(self):
        return "Link not found", 200


class LinkAPI(Resource):
    # def get(self):
    #     return 'Link not found', 200

    def get(self, link_id):
        if link_id is None:
            return "Link not found", 200
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
            expire_at = request_data["expire_at"].replace("/", "-")
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
        try:
            if "http://" not in original_link and "https://" not in original_link:
                original_link = "http://" + original_link
            link_id = self.short_link_generator(original_link)
            short_link = WEBSITE_URL + link_id
            data = {
                "original_link": original_link,
                "expire_at": expire_at,
                "short_link": short_link,
                "link_id": link_id,
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
