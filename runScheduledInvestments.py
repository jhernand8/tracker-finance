import webapp2
from datetime import *
from ScheduledInvestRunDate import ScheduledInvestRunDate
from investmentDate import ScheduledInvestment
from investment import Investment
class RunScheduledInvestments(webapp2.RequestHandler):
	def get(self):
		lastRunDateObj = ScheduledInvestRunDate.all().get();
		if (lastRunDateObj == None):
			lastRunDate = date.today() - timedelta(days=20);
			lastRunDateObj = ScheduledInvestRunDate(lastRunDate=lastRunDate, key_name="last_run_date");
			lastRunDateObj.put();
		lastRunDate = lastRunDateObj.lastRunDate;

		startDate = lastRunDate + timedelta(days=1);
		endDate = date.today() - timedelta(days=3);
		currDate = startDate;
		scheduleQuery = ScheduledInvestment.all();
		for scheduledInvest in scheduleQuery:

			while (True):
				#if currDate.day == scheduledInvest.dayOfMonth:
					#invest = Investment(scheduledInvest.ticker, sched
				currDate = currDate + timedelta(days=1);
				if currDate > endDate:
					break;
		self.response.out.write("scheduled");

app = webapp2.WSGIApplication([('/runScheduledInvests', RunScheduledInvestments)], debug=True)
