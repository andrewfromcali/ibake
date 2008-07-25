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
    
    if len(name) == 0 or len(name) > 80:
      self.redirect('/site/starting-points?error=size_too_big_or_too_small')
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
   
class ItemHandler(webapp.RequestHandler):
  def get(self, parent, permalink):
    query = db.Query(model.Item)
    query.filter('parent_permalink =', parent)
    query.filter('permalink =', permalink)
    item = query.get()
    if item:
      render(self, 'views/items/details.html', {'item': item})   
    else:
      self.error(404)
      render(self, 'views/_shared/404.html', {})
  def post(self, parent, permalink):
    query = db.Query(model.Item)
    query.filter('parent_permalink =', parent)
    query.filter('permalink =', permalink)
    item = query.get()
    
    link=self.request.get('l').strip()
     

class AnythingHandler(webapp.RequestHandler):
  def get(self, path):
    query = db.Query(model.StartingPoint)
    query.filter('permalink =', path)
    sp = query.get()
    if sp:
      query = model.Item.all()
      query.filter('parent_permalink =', path)
      query.order('permalink')
      render(self, 'views/items/item.html', {'sp': sp, 'items': query.fetch(1000, 0)})   
    else:
      self.error(404)
      render(self, 'views/_shared/404.html', {})    
  def post(self, path):
    name=self.request.get('s').strip()
    query = db.Query(model.StartingPoint)
    query.filter('permalink =', path)
    sp = query.get()
    
    if len(name) == 0 or len(name) > 80:
      self.redirect(''.join([self.request.path, '?error=size_too_big_or_too_small']))
      return
      
    permalink=get_friendly_url(name)
    
    query = db.Query(model.Item)
    query.filter('parent_permalink =', path)
    query.filter('permalink =', permalink)
    if query.get():
      self.redirect(''.join([self.request.path, '?error=duplicate']))
    else:
      item = model.Item(name=name,permalink=permalink,parent_permalink=path)
      item.put()
      self.redirect(self.request.path)
  