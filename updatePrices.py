from stockPrice import stockPrice
from stockUpdateDate import StockUpdateDate
import datetime
from datetime import *
import webapp2
from google.appengine.api import users
from stockTickerPriceHelper import InvestmentHelper
from decimal import Decimal

# main class for updating historical prices of stocks.
# this will be called by a cron job and updates stockPrice 
# adding data up through the previous day.
class MainPage(webapp2.RequestHandler):
  def get(self):
    stocksLastUpdate = StockUpdateDate.all();
    stocks = stocksLastUpdate.run();
    hasAny = False;
    # find all tickers that we need to update
    for s in stocks:
	    hasAny = True;
	    currDate = s.date;
	    currDate = currDate;
	    # get the closing price data and create map of date to price
	    csvdata = InvestmentHelper.getCSVPriceData(startMonth=currDate.month, startYear=currDate.year, startDay=currDate.day, ticker=s.ticker);
	    dateToPrice = InvestmentHelper.mapDateToClosePrice(csvdata);
	    # for each date, add to stockPrice
	    for d in dateToPrice:
		    if d == date.today():
			    continue;
		    keystr = s.ticker + "_" + str(d.year) + "_" + str(d.month) + "_" + str(d.day);
		    dateprice = stockPrice(ticker=s.ticker, date=d, price=Decimal(dateToPrice[d]), key_name=keystr);
		    dateprice.put();
	    s.date = date.today() - timedelta(days=3);
	    s.put();
    if (not hasAny):
	    obj = StockUpdateDate(ticker="vtsmx", date=date(year=2013,month=1,day=1), key_name="goog");
	    obj.put();
    self.response.out.write("finished");

app = webapp2.WSGIApplication([('/cronUpdatePrices', MainPage)],
                              debug=True)

