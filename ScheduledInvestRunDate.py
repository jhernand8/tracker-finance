from google.appengine.ext import db

# the last day for which scheduled investments were processed
# by the cron job.
class ScheduledInvestRunDate(db.Model):
	lastRunDate = db.DateProperty(required=True)
