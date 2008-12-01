from google.appengine.ext import db

class Item(db.Model):
  parent_permalink = db.StringProperty(required=True)
  permalink        = db.StringProperty(required=True)
  name             = db.StringProperty(required=True)
  description      = db.TextProperty
  link             = db.StringProperty