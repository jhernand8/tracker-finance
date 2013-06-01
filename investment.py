from google.appengine.ext import db
from DecimalProperty import DecimalProperty

# an investment in a particular stock/fund on a given date
# amount is the amount spent.
class Investment(db.Model):
	ticker = db.StringProperty(required=True)
	shares = DecimalProperty(required=True)
	sharePrice = DecimalProperty(required=True)
	amount = db.IntegerProperty(required=True)
	date = db.DateProperty(required=True)
