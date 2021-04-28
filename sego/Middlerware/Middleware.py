# ************************************************************************#
# Title:                    Middleware API                                #
# Description:              This class is the main interface into  Sego's #
#                           middleware system                             #
# Author:                   Sambe Consulting <development@sambe.co.za>    #
# Original Date:            10 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#

from webob import Request, Response


class Middleware:
    PREPROCESS = 1
    POSTPROCESS = 2

    def process_request(self, request: Request):
        """
            This method is meant for processing requests in the middleware layer
            :param request:
            :return: request : webob.Request
        """
        pass

    def process_response(self,  request: Request, response: Response):
       """
        This method is meant for processing responses in the middleware layer
        :param request:
        :param response:
        :return:
       """
       pass
