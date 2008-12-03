from google.appengine.ext import db
import re

class Callable:
    def __init__(self, anycallable):
        self.__call__ = anycallable
        
class Item(db.Model):
  parent_permalink = db.StringProperty(required=True)
  permalink        = db.StringProperty(required=True)
  name             = db.StringProperty(required=True)
  description      = db.TextProperty
  link             = db.StringProperty
  
  def get_friendly_url(title):
    return re.sub('-+', '-', 
             re.sub('[^\w-]', '', 
               re.sub('\s+', '-', title.strip().lower())))
  get_friendly_url = Callable(get_friendly_url)