# ************************************************************************#
# Title:                    Sego Router Verbs                             #
# Description:              Constants for HTTP verbs                      #
# Author:                   Kabelo Masemola <kn3rdydad@gmail.com>         #
# Original Date:            10 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#
from .. import Routing
from ..Exceptions.HTTPVerbException import UnknownHTTPMethodException
class Verb:
    HTTP_GET = 1
    HTTP_POST = 2
    HTTP_PUT = 3
    HTTP_DELETE = 4

    def validate(self,str_method):
        str_method = str_method.lower().strip()
        if str_method == 'get':
            return self.HTTP_GET
        elif str_method == 'post':
            return self.HTTP_POST
        elif str_method == 'put':
            return self.HTTP_PUT
        elif str_method == 'delete':
            return self.HTTP_DELETE
        else:
            raise UnknownHTTPMethodException()

    def get_string(self,verb):
        if verb == self.HTTP_GET:
            return 'GET'
        elif verb == self.HTTP_POST:
            return 'POST'
        elif verb == self.HTTP_PUT:
            return 'PUT'
        elif verb == self.HTTP_DELETE:
            return 'DELETE'
        else:
            raise UnknownHTTPMethodException()



