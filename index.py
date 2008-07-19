import cgi
import wsgiref.handlers
import os

from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.ext import webapp

class MainPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'greetings': 'test',
      }

    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))


def main():
  application = webapp.WSGIApplication(
                                       [('/', MainPage)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()