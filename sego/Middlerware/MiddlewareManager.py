# ************************************************************************#
# Title:                    MiddlewareHandler API                         #
# Description:              This class is the main interface into  Sego's #
#                           middleware system                             #
# Author:                   Sambe Consulting <development@sambe.co.za>    #
# Original Date:            10 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#

from .Middleware import Middleware


class MiddlewareManager(object):

    def add(self, middleware: Middleware, process):
        pass


