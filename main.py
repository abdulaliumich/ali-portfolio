#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#This class handles all pathnames
class MainHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("GET Request for MainHandler called. Pathname: " + self.request.path)

        current_page = ""
        
        #For now, the only pathnames that will succeed in the try-block are "/about", "/places", "/contact"
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

        self.response.write(template.render({"current_page": current_page}))



app = webapp2.WSGIApplication([
    ('/.*', MainHandler)
], debug=True)
