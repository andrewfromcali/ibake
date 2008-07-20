import datetime
import string
import re
import os

import logging

from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.webapp import template

import model

def render(handler, path, values):
  path = os.path.join(os.path.dirname(__file__), path)
  handler.response.out.write(template.render(path, values))    

def get_friendly_url(title):
    return re.sub('-+', '-', 
                  re.sub('[^\w-]', '', 
                         re.sub('\s+', '-', title.strip().lower())))

class NotFoundHandler(webapp.RequestHandler):
  def get(self):
    self.error(404)
    render(self, 'views/_shared/404.html', {})

class RootHandler(webapp.RequestHandler):
  def get(self):
    render(self, 'views/home/index.html', {})

class StartingPointsHandler(webapp.RequestHandler):
  def get(self):
    render(self, 'views/starting-points/starting-points.html', {})
  def post(self):
    name=self.request.get('s').strip()
    permalink=get_friendly_url(name)
    
    query = db.Query(model.StartingPoint)
    query.filter('permalink =', permalink)
    if query.get():
      logging.info('there');
    else:
      sp = model.StartingPoint(name=name,permalink=permalink)
      sp.put()
      logging.info('no there');
   
    self.redirect('/')

class AnythingHandler(webapp.RequestHandler):
  def get(self, path):
    print 'anything'
    
  