from google.appengine.ext import db

class StartingPoint(db.Model):
  permalink = db.StringProperty(required=True)
  name      = db.StringProperty(required=True)

class Item(db.Model):
  parent_permalink = db.StringProperty(required=True)
  permalink        = db.StringProperty(required=True)
  name             = db.StringProperty(required=True)
  description      = db.TextProperty
  link             = db.StringProperty

class ItemToItem(db.Model):
  parent_permalink1 = db.StringProperty(required=True)
  permalink1        = db.StringProperty(required=True)
  parent_permalink2 = db.StringProperty(required=True)
  permalink2        = db.StringProperty(required=True)
  description       = db.TextProperty
  link              = db.StringProperty

