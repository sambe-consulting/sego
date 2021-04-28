# ************************************************************************#
# Title:                    MiddlewareHandler API                         #
# Description:              This class is the main interface into  Sego's #
#                           middleware system                             #
# Author:                   Sambe Consulting <development@sambe.co.za>    #
# Original Date:            10 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#

from .Middleware import Middleware
from ..Exceptions.MiddlewareException import *
from singleton_decorator import singleton
from webob import Request, Response


@singleton
class MiddlewareManager(object):

    def __init__(self):
        self.global_middleware = {}

    def add(self, middleware_name: str, middleware: Middleware, overwrite=False):
        """
        This method registers a new middleware to be used in the platform
        :param middleware_name:
        :param middleware:
        :param overwrite:
        :return:
        """

        if overwrite == True:
            self.global_middleware[middleware_name] = middleware
        else:
            if middleware_name not in self.global_middleware:
                self.global_middleware[middleware_name] = middleware
            else:
                raise MiddlewareAlreadyRegisteredException()

    def get(self, middleware_name):
        """
        This method returns a middleware associated with the 'middleware_name' :parameter
        if the name does not exist a MiddlewareNotFound exception is raised
        :param middleware_name:
        :return: middleware : Sego.Middleware.Middleware
        """
        if middleware_name in self.global_middleware:
            return self.global_middleware[middleware_name]
        else:
            raise MiddlewareNotFound()

    def get_all(self):
        """
        This method returns all registered middleware
        :return: global_middleware : dict
        """
        return self.global_middleware

    def validate(self, middleware_name):
        """
        This method is a lightweight version of get, because it does not return the middleware
        object only a TRUE/FALSE whether it exists or not
        :param middleware_name:
        :return: TRUE/FALSE
        """
        exists = False
        if middleware_name in self.global_middleware:
            exists = True
        return exists

    def run(self, middleware_list: list, request: Request, response: Response):
        """
        This method instantiates each middleware class in list the runs
        :param middleware_list:
        :param request:
        :param response:
        :return:
        """
        for middleware_tuple in middleware_list:
            middleware = middleware_tuple[1]
            middleware_class = self.global_middleware[middleware]
            middleware_instance = middleware_class()
            middleware_instance.process_request(request)
            middleware_instance.process_respone(response)
