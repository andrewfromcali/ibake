from google.appengine.ext import db

class StartingPoint(db.Model):
  permalink = db.StringProperty(required=True)
  name = db.StringProperty(required=True)

class Item(db.Model):
  parent_permalink = db.StringProperty(required=True)
  permalink = db.StringProperty(required=True)
  name = db.StringProperty(required=True)
  