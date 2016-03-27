from config import JINJA_ENVIRONMENT
from google.appengine.api import users
from models import GuestbookMessage
import logging
import webapp2

#This class handles routing to all pathnames except for guestbook
class MainHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("GET Request for MainHandler called. Pathname: " + self.request.path)

        current_page = ""
        
        #For now, the only pathnames that will succeed in the try-block are "/about", "/places", "/contact", "/guestbook",
        #and "/index".
        #All other pathnames (e.g. "/", "/about.html", "/blhahlsdu") should enter
        #the except-block and be redirected to the index page.
        try:
            if self.request.path.islower() == False:
                raise Exception ('pathname must be all lower case')
            template = JINJA_ENVIRONMENT.get_template("templates/" + self.request.path + ".html")
            #current_page should end up being one of the following four values: "INDEX", "ABOUT", "PLACES", "CONTACT"
            current_page = self.request.path[1:].upper()
        except:
            logging.info("Redirecting to index.html")
            template = JINJA_ENVIRONMENT.get_template("templates/index.html")
            current_page = "INDEX"

        
        #Move to function
        loggedIn = 0
        logUrl = users.create_login_url(self.request.path)
        user = users.get_current_user()

        #Someone is logged in
        if user:
            loggedIn = 1
            logUrl = users.create_logout_url(self.request.path)

        self.response.write(template.render({"current_page": current_page, "loggedIn": loggedIn, "logUrl": logUrl}))

#This class handles routing to the guestbook page
class GuestbookHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/guestbook.html")
        self.response.write(template.render({"current_page": "GUESTBOOK", "loggedIn": 1, "logUrl": users.create_login_url(self.request.path)}))


app = webapp2.WSGIApplication([
    ('/guestbook', GuestbookHandler),
    ('/.*', MainHandler)
], debug=True)
