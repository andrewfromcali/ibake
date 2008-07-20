from google.appengine.ext import db

class StartingPoint(db.Model):
    permalink = db.StringProperty(required=True)
    name = db.StringProperty(required=True)
