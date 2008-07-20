import datetime
import string
import re
import os

import logging

from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.webapp import template

class NotFoundHandler(webapp.RequestHandler):
  def get(self):
    self.error(404)
    print '404'

class RootHandler(webapp.RequestHandler):
  def get(self):
    template_values = {
     'greetings': 'test',
     'url': 'test',
    }

    path = os.path.join(os.path.dirname(__file__), 'views/home/index.html')
    self.response.out.write(template.render(path, template_values))

class AnythingHandler(webapp.RequestHandler):
  def get(self, path):
    print 'anything'