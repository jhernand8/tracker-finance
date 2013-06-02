from StockUpdateDate import StockUpdateDate
import datetime
from datetime import date
class UpdateStockPrices():

  def get(self):
    q = StockUpdateDate.all();

    results = q.run();
    hasResults = False;
    for res in results:
      hasResults = True;

    if not hasResults:
      m = StockUpdateDate(ticker="aepgx", date=date(year=2011,month=1,day=1));
      m.put();
