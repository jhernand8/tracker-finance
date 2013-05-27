import decimal;
from google.appengine.ext import db

# from http://googleappengine.blogspot.com/2009/07/writing-custom-property-classes.html
# Property class to store decimals for which can control precision
# and is exact instead of approximate.
class DecimalProperty(db.Property):
  data_type = decimal.Decimal

  def get_value_for_datastore(self, currModel):
    return str(super(DecimalProperty, self).get_value_for_datastore(currModel))

  def make_value_from_datastore(self, val):
    return decimal.Decimal(val);
