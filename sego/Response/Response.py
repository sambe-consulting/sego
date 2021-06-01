# ************************************************************************#
# Title:                    Sego Response API                             #
# Description:              This class handles response objects           #
# Author:                   Sambe Consulting <development@sambe.co.za>    #
# Original Date:            20 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#

from webob import Response as WebObResponse
import json


class Response:
    def __init__(self):
        """
        Define response types
        """
        self.json = None
        self.html = None
        self.text = None
        self.location = None
        self.content_type = None
        self.body = b''
        self.status_code = 200
        self.cookies = []
        self.delete_cookies = []
        self.unset_cookies = []

    def __call__(self, environ, start_response):
        self.set_body_and_content_type()
        response = WebObResponse(
            body=self.body, content_type=self.content_type, status=self.status_code
        )

        response = self.build_cookies(response=response)
        if self.location is not None:
            response.location = self.location

        return response(environ, start_response)

    def set_body_and_content_type(self):
        if self.json is not None:
            self.body = json.dumps(self.json).encode("UTF-8")
            self.content_type = "application/json"

        if self.html is not None:
            self.body = self.html.encode()
            self.content_type = "text/html"

        if self.text is not None:
            self.body = self.text
            self.content_type = "text/plain"

        if self.location is not None:
           self.status_code = 308

    def set_cookie(self, name, value='', max_age=None,
                   path='/', domain=None, secure=False, httponly=False,
                   comment=None, expires=None, overwrite=False,
                   samesite=None):
        cur_cookie = {
            "name":name,"value":value,"max_age":max_age,"path":path,
            "domain":domain,"secure":secure,"httponly":httponly,"comment":comment,
            "expires":expires,"overwrite":overwrite,"samesite":samesite
        }
        self.cookies.append(cur_cookie)

    def delete_cookie(self,name, path='/', domain=None):
        self.delete_cookies.append({"name":name,"path":path,"domain":domain})

    def unset_cookie(self, name, strict=True):
        self.unset_cookies.append({"name":name,"strict":strict})

    def build_cookies(self,response):
        for cookie in self.cookies:
            response.set_cookie(**cookie)

        for cookie in self.delete_cookies:
            response.delete_cookie(**cookie)

        for cookie in self.unset_cookies:
            response.unset_cookie(**cookie)

        return response
