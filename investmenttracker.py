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
from investment import investment
from stockPrice import stockPrice
from collections import namedtuple

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
  def get(self):
    invs = investment.all();
    sps = stockPrice.all();
    self.response.out.write("done");

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
