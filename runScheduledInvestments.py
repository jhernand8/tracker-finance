import webapp2

class RunScheduledInvestments(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("scheduled");

app = webapp2.WSGIApplication([('/runScheduledInvests', RunScheduledInvestments)], debug=True)
