import datetime
from google.appengine.ext import db
from DecimalProperty import DecimalProperty
class stockPrice(db.Model):
  date = db.DateProperty(required=True)
  ticker = db.StringProperty(required=True)
  price = DecimalProperty(required=True)

