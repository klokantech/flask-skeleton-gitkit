from flask.ext.login import UserMixin

from .base import db


class Account(UserMixin, db.Model):

    __tablename__ = 'account'

    id = db.Column(db.Text, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    email_verified = db.Column(db.Text, default=False, nullable=False)
    name = db.Column(db.Text)
    photo_url = db.Column(db.Text)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
