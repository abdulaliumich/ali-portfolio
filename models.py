from google.appengine.ext import ndb

class GuestbookMessage(ndb.Model):
    author = ndb.StringProperty(indexed=False)
    message = ndb.StringProperty(indexed=False)
    timestamp = ndb.DateTimeProperty(auto_now_add=True) #automatically add timestamp when a user submits a post


#entity model for all photos that appear on the Places page
class Photo(ndb.Model):
    url = ndb.StringProperty(indexed=False) #the URL of the photo
    author = ndb.StringProperty(indexed=False) #the owner of the photo (for now, all the photos belong to me)

#TODO: add photo comment table?