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
    query = model.StartingPoint.all()
    query.order('permalink')
    render(self, 'views/home/index.html', {'items': query.fetch(1000, 0) })

class StartingPointsHandler(webapp.RequestHandler):
  def get(self):
    values = { 'permalink': self.request.get('p'),
                'error' : self.request.get('error') }
    render(self, 'views/starting-points/starting-points.html', values)
  def post(self):
    name=self.request.get('s').strip()
    
    if len(name) == 0:
      self.redirect('/site/starting-points?error=blank')
      return
    
    permalink=get_friendly_url(name)
    
    query = db.Query(model.StartingPoint)
    query.filter('permalink =', permalink)
    if query.get():
      self.redirect(''.join(['/site/starting-points?error=duplicate&p=', permalink]))
    else:
      sp = model.StartingPoint(name=name,permalink=permalink)
      sp.put()
      self.redirect(''.join(['/site/starting-points?p=', permalink]))
   

class AnythingHandler(webapp.RequestHandler):
  def get(self, path):
    query = db.Query(model.StartingPoint)
    logging.info(self.request.path[1:])
    query.filter('permalink =', self.request.path[1:])
    sp = query.get()
    if sp:
      render(self, 'views/items/item.html', {})   
    else:
      self.error(404)
      render(self, 'views/_shared/404.html', {})    
    
  