import datetime
import string
import re
import os

import logging

from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.webapp import template

def render(handler, path, values):
  path = os.path.join(os.path.dirname(__file__), path)
  handler.response.out.write(template.render(path, values))    


class NotFoundHandler(webapp.RequestHandler):
  def get(self):
    self.error(404)
    render(self, 'views/_shared/404.html', {})

class RootHandler(webapp.RequestHandler):
  def get(self):
    render(self, 'views/home/index.html', {})


class AnythingHandler(webapp.RequestHandler):
  def get(self, path):
    print 'anything'
    
  