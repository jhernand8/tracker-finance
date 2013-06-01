from google.appengine.ext. import db

# A scheduled investment of some amount each month on the given
# day of the month.
class ScheduledInvestment(db.Model):
	ticker = db.StringProperty(required=True)
	amount = db.IntegerProperty(required=True)
	dayOfMonth = db.IntegerProperty(required=True)
