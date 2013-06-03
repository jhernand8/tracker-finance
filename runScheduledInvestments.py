import webapp2
from datetime import *
from ScheduledInvestRunDate import ScheduledInvestRunDate
from investmentDate import ScheduledInvestment
from investment import Investment
from stockPrice import stockPrice
from decimal import *
from google.appengine.ext import db
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
        if currDate.day == scheduledInvest.dayOfMonth:
          sharePrice = self.get_share_price(currDate, scheduledInvest.ticker);
          invest = Investment(ticker=scheduledInvest.ticker,
                              amount=scheduledInvest.amount,
                              date=currDate,
                              sharePrice=sharePrice,
                              shares=self.num_shares(scheduledInvest.amount, sharePrice));
          invest.put();
        currDate = currDate + timedelta(days=1);
        if currDate > endDate:
          break;
    lastRunDateObj.lastRunDate = endDate;
    lastRunDateObj.put();
    self.response.out.write("scheduled");
  def num_shares(self, amount, sharePrice):
    amountDec = Decimal(amount);
    getcontext().prec = 3;
    shares = amountDec / sharePrice;
    return shares;
  def get_share_price(self, date, ticker):
    q = db.Query(stockPrice).filter("ticker", ticker).filter("date", date);
    sPrice = q.get();
    return sPrice.price;

app = webapp2.WSGIApplication([('/runScheduledInvests', RunScheduledInvestments)], debug=True)
