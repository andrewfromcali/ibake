# models.py

from google.appengine.ext import db

class Visitor(db.Model):
    ip = db.StringProperty()
    added_on = db.DateTimeProperty(auto_now_add=True)
    
class Poll(db.Model):
    question = db.StringProperty()
    pub_date = db.DateTimeProperty(auto_now_add=True)
    
    def __unicode__(self):
        return self.question

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
        
class Choice(db.Model):
    poll = db.StringProperty(required=True)
    choice = db.StringProperty()
    votes = db.IntegerPropety()
    
    def __unicode__(self):
        return self.choice