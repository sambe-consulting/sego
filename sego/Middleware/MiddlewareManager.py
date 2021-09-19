# ************************************************************************#
# Title:                    MiddlewareHandler API                         #
# Description:              This class is the main interface into  Sego's #
#                           middleware system                             #
# Author:                   Sambe Consulting <development@sambe.co.za>    #
# Original Date:            10 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#

from .Middleware import Middleware
from .Middleware import Middleware as SegoMiddleware
from ..Exceptions.MiddlewareException import *
from singleton_decorator import singleton
from webob import Request, Response
from ..Routing.Route import *

@singleton
class MiddlewareManager(object):

    def __init__(self):
        self.global_middleware = {}
        self.pre_process_middleware = []
        self.post_process_middleware = []

    def load(self, middleware_list):
        """
        This method is used to load middleware into the system
        :param middleware_list:
        :return:
        """
        overwrite = False
        for middleware in middleware_list:
            if "overwrite" in middleware:
                if middleware["overwrite"] in [True, False]:
                    overwrite = middleware["overwrite"]
                else:
                    raise MiddlewareOverwriteMustBeBoolean()

            if "name" in middleware:
                if isinstance(middleware["name"], str):
                    middleware_name = middleware["name"]
                else:
                    raise MiddlewareNameMustBeString()
            else:
                raise MiddlewareMustHaveName()

            if "middleware" in middleware:
                if issubclass(middleware["middleware"], SegoMiddleware):
                    middlewareObject = middleware["middleware"]
                else:
                    raise MiddlewareMustExtend()
            else:
                raise SegoBaseException("All dictionaries must have middleware class ")

            self.add(middleware_name=middleware_name, middleware=middlewareObject, overwrite=overwrite)

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

    def register(self, stage: int, middleware_names: list):
        main_error = "Middleware %s was not loaded into the global middleware registry, use MiddlewareManager.load(self, middleware_list)"

        if stage == Middleware.PREPROCESS:
            for middleware_name in middleware_names:
                if self.validate(middleware_name):
                    if middleware_name not in self.pre_process_middleware:
                        self.pre_process_middleware.append(middleware_name)
                    else:
                        raise SegoBaseException("Middleware %s is registered more than once"% str(middleware_name))
                else:
                    raise SegoBaseException(main_error%middleware_name)

        elif stage == Middleware.POSTPROCESS:
            for middleware_name in middleware_names:
                if self.validate(middleware_name):
                    if middleware_name not in self.post_process_middleware:
                        self.post_process_middleware.append(middleware_name)
                    else:
                        raise SegoBaseException("Middleware %s is registered more than once"% str(middleware_name))
                else:
                    raise SegoBaseException(main_error%middleware_name)

        else:
            raise SegoBaseException("Use 'Middleware.PREPROCESS or Middleware.POSTPROCESS for the stage argument")

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

        for entry in self.global_middleware:
            if middleware_name.strip().lower() == entry.strip().lower():
                exists = True
                break
        return exists

    def diff(self,middleware_list,excluded_middleware_list):
        list_difference = []
        for middleware in middleware_list:
            if middleware not in excluded_middleware_list:
                list_difference.append(middleware)
        return list_difference


    def process_middleware(self,stage :int ,route,request : Request = None,response : Response = None):
        if stage == Middleware.PREPROCESS:
            route_excluded_middleware = route["excluded_middleware"]["pre_process"]
            route_middleware = route["middleware"]["pre_process"]
            self.run(stage=stage,middleware_list=self.diff(self.pre_process_middleware,route_excluded_middleware),request=request,response=response)
            self.run(stage=stage,middleware_list=self.diff(route_middleware,route_excluded_middleware),request=request,response=response)
        elif stage == Middleware.POSTPROCESS:
            route_excluded_middleware = route["excluded_middleware"]["post_process"]
            route_middleware = route["middleware"]["post_process"]
            self.run(stage=stage,middleware_list=self.diff(self.post_process_middleware,route_excluded_middleware),request=request,response=response)
            self.run(stage=stage,middleware_list=self.diff(route_middleware, route_excluded_middleware),request=request,response=response)
        else:
            raise SegoBaseException("Use 'Middleware.PREPROCESS or Middleware.POSTPROCESS for the stage argument")



    def run(self,stage:int, middleware_list: list, request: Request, response: Response):
        """
        This method instantiates each middleware class in list the runs
        :param middleware_list:
        :param request:
        :param response:
        :return:
        """

        for middleware in middleware_list:

            instance = self.global_middleware[middleware]()
            if stage == Middleware.PREPROCESS:
                print("Pre process middleware")
                instance.process_request(request=request)
            elif stage == Middleware.POSTPROCESS:
                print("Post process middleware")
                instance.process_response(request=request, response=response)
