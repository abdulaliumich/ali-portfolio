from config import JINJA_ENVIRONMENT
from google.appengine.api import users, memcache
from google.appengine.datastore.datastore_query import Cursor
from google.appengine.ext import ndb
from models import GuestbookMessage
import logging
import webapp2
import time

#Returns a dictionary object of the user's login status (1 for logged in, 0 otherwise),
#and the respective url (login url if user is logged out, logout url if user is logged in)
def loginStatus(path):
    login_status = {'logged_in' : 0, 'log_url': users.create_login_url(path)}

    #Someone is logged in
    if users.get_current_user():
        login_status['logged_in'] = 1
        login_status['log_url'] = users.create_logout_url('/') #Redirect user to home page when they log out

    return login_status


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

        
        login_status = loginStatus(self.request.path)

        self.response.write(template.render({"current_page": current_page, "logged_in": login_status['logged_in'], 
                                             "log_url": login_status['log_url']}))

#This class handles routing to the guestbook page
class GuestbookHandler(webapp2.RequestHandler):
    def get(self):
        logging.info('Guestbook get function')
        template = JINJA_ENVIRONMENT.get_template("templates/guestbook.html")

        #Reference - GAE documentation on Query Cursors

        #Sort the messages by most recent first
        message_query = GuestbookMessage.query().order(-GuestbookMessage.timestamp)
        messages = ''
        more_messages = 0

        message_block = self.request.get('start')
        logging.info('message_block is: ')
        logging.info(message_block)

        #User is on the first page of the guestbook (e.g. just navigated to the guestbook page)
        if not message_block:
            #Get the first ten messages in the guestbook
            messages, next_cursor, more_messages = message_query.fetch_page(10)
            message_block = 0
            memcache_key = 'block10'
            memcache.set(memcache_key, next_cursor)

        #User is not on the first page of the guestbook
        else:
            memcache_key = 'block' + message_block
            curs = memcache.get(memcache_key)
            
            #This should never happen because every time you retrieve the next 10 results,
            #you are setting the cursor to start at the beginning of the next message after that the ones
            #you just retrieved
            if not curs:
                logging.info("Error: curs is invalid")
                self.redirect('/guestbook')
            else:
                messages, next_cursor, more_messages = message_query.fetch_page(10, start_cursor=curs)
                if more_messages:
                    next_block = int(message_block) + 10
                    memcache_key = 'block' + str(next_block)
                    memcache.set(memcache_key, next_cursor)

        login_status = loginStatus(self.request.path)

        self.response.write(template.render({"current_page": "GUESTBOOK", "logged_in": login_status["logged_in"], "log_url": login_status["log_url"],
                                            "messages": messages, "more_messages":more_messages, "message_block" : int(message_block)}))
    def post(self):
        logging.info('Guestbook post function')
        #Reference - GAE Guestbook tutorial
        template = JINJA_ENVIRONMENT.get_template("templates/guestbook.html")
        mes = GuestbookMessage(parent=ndb.Key('Guestbook', 'AliGuestbook'))
        mes.user = users.get_current_user().nickname()
        mes.message = self.request.get('jk')
        mes.put()
        #Add a second to give time for message to be added to the database 
        #and appear with the rest of the messages on redirect (hacky solution for now)
        time.sleep(1)
        self.redirect('/guestbook')


app = webapp2.WSGIApplication([
    ('/guestbook', GuestbookHandler),
    ('/.*', MainHandler)
], debug=True)
