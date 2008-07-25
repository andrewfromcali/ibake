import wsgiref.handlers

from google.appengine.ext import webapp

import ibake

def main():
    application = webapp.WSGIApplication(
                    [('/*$', ibake.RootHandler),
                     ('/404.html', ibake.NotFoundHandler),
                     ('/site/starting-points', ibake.StartingPointsHandler),
                     ('/site/starting-points/', ibake.StartingPointsHandler),
                     ('/(.*)/(.*)', ibake.ItemHandler),
                     ('/(.*)', ibake.AnythingHandler)], 
                    debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()