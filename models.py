from peewee import *
from flask.ext.login import UserMixin
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