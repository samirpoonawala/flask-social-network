import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('social.db')

class User(UserMixIn, Model):
  username = CharField(unique=True)
  email = CharField(unique=True)
  password = CharField(max_length=100)
  joined_at = DateTimeField(default=datetime.datetime.now)
  is_admin = BooleanField(default=False) # for use if you try to add additional functionality later
  
  class Meta:
    database = DATABASE
    order_by = ('-joined_at',)
  
  @classmethod
  def create_user(cls, username, email, password, admin=False):
    try:
      cls.create(
        username=username,
        email=email,
        password=generate_password_hash
    except IntegrityError:
        # if username or email is not unique
        raise ValueError("User already exists")