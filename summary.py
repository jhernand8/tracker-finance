import webapp2
from google.appengine.api import users
import jinja2
import os
import email, getpass, imaplib, os
from time import mktime
from datetime import datetime
from datetime import timedelta
import time
from string import Template
from stockPrice import stockPrice
from collections import namedtuple
from decimal import *
from StockUpdateDate import StockUpdateDate
from investment import Investment;
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class SummaryData:
  currPrice = Decimal("0");
  ticker = "";
  shares = Decimal("0");
  amount = 0;
  value = Decimal("0");
  percentage = Decimal("0");
# Page class for viewing summary info about investments
class SummaryPage(webapp2.RequestHandler):
  def get(self):
    tickers = StockUpdateDate.all();
    summaryDataArr = [];
    for stockUpDate in tickers:
      ticker = stockUpDate.ticker;
      summData = self.getSummData(ticker);
      summaryDataArr.append(summData);
    template = jinja_environment.get_template("Summary.html");
    templateValues = { 'summaryData': summaryDataArr};

    self.response.out.write(template.render(templateValues));
    self.response.out.write("done");

  def getSummData(self, ticker):
    invs = Investment.all().filter("ticker", ticker);
    data = SummaryData();
    data.ticker = ticker;
    for inv in invs:
      data.amount = data.amount + inv.amount;
      data.shares = data.shares + inv.shares;
    latestPriceQ = stockPrice.all().filter("ticker", ticker).order("-date");
    latestPrice = latestPriceQ.get().price;
    data.currPrice = latestPrice;

    data.value = data.currPrice * data.shares;
    if data.amount > 0:
      data.percentage = data.value / Decimal(data.amount) - Decimal("1.0");
    return data;

app = webapp2.WSGIApplication([('/summary', SummaryPage)],
                              debug=True)
