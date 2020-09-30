from .db import db
from flask_mongoengine.wtf import model_form

class Link(db.Document):
    link_id = db.StringField(required=True, unique=True)
    short_link = db.StringField(required=True, unique=True)
    original_link = db.StringField(required=True)
    expire_at = db.DateTimeField()
