import datetime
from google.appengine.ext import db

class StockUpdateDate(db.Model):
  date = db.DateProperty(required=True)
  ticker = db.StringProperty(required=True)

