# ************************************************************************#
# Title:                    Sego Route                                    #
# Description:              This class handles definition of routes       #
# Author:                   Kabelo Masemola <kn3rdydad@gmail.com>         #
# Original Date:            10 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#

from .Verb import Verb
from ..Exceptions import *
from ..Middleware import Middleware,MiddlewareManager

class Route:
    def __init__(self, name: str = None, verb: int = None, controller: str = None, action: str = None,
                 url: str = None):
        self.name = name
        self.verb = verb
        self.controller = controller
        self.action = action
        self.url = url
        self.middleware = {"pre_process": [], "post_process": []}
        self.middleware_manager = MiddlewareManager()
        self.excluded_middleware = {"pre_process":[],"post_process":[]}

    def set_name(self, name) -> object:
        """
        This method sets the name of the route object
        :param name:
        :return: self / Route
        """
        self.name = name
        return self

    def get_name(self) -> str:
        """
        This method returns the name of the route object
        :return: name
        """
        return self.name

    def set_verb(self, verb) -> object:
        """
        This method sets the http verbs used by the route
        :param verb:
        :return: self / Route
        """
        self.verbs = verb
        return self

    def get_verb(self) -> int:
        """
        This method returns the http verbs used by the current route
        :return: verbs
        """
        return self.verb

    def set_controller(self, controller) -> object:
        """
        This method sets the controller which defines the action for this route
        :param controller:
        :return: self / Route
        """
        self.controller = controller
        return self

    def get_controller(self) -> str:
        """
        This method returns the controller for this route
        :return: controller
        """
        return self.controller

    def set_action(self, action) -> object:
        """
        This method sets the action to execute for this route
        :param action:
        :return: self / Route
        """
        self.action = action
        return self

    def get_action(self) -> str:
        """
        This method returns the action for this route
        :return: action
        """
        return self.action

    def set_middleware(self,stage:int ,middleware_list : list) -> object:
       """
        This method sets the list of middleware to be executed before and after the http request
        is handled by the controller
       :param stage:
       :param middleware_list:
       :return: self / Route
       """
       if stage == Middleware.PREPROCESS:
           self.middleware["pre_process"] = self.middleware["pre_process"]+middleware_list
       elif stage == Middleware.POSTPROCESS:
           self.middleware["post_process"] = self.middleware["post_process"]+ middleware_list
       return self

    def get_middleware(self) -> dict:
        """
        This method returns middleware
        :return:  middleware
        """
        return self.middleware

    def unset_middleware(self,stage:int,middleware_list:list) -> object:
        """
        This method allows for unsetting global middleware for the particular route
        :param stage:
        :param middleware_list:
        :return:
        """
        if stage == Middleware.PREPROCESS:
            self.excluded_middleware["pre_process"] = self.excluded_middleware["pre_process"]+middleware_list
        elif stage == Middleware.POSTPROCESS:
            self.excluded_middleware["pre_process"] = self.excluded_middleware["pre_process"]+middleware_list
        return self

    def get_excluded_middleware(self) -> dict:
        """
        This method returns a dictionary of excluded middleware
        :return: exclude_middleware
        """
        return self.excluded_middleware

    def set_url(self, url) -> object:
        """
        This method sets the URL associated with this route
        :param url:
        :return: self / Route
        """
        self.url = url
        return self

    def get_url(self) -> str:
        """
        This method returns the URL for the route
        :return: url
        """
        return self.url

    def get_route(self) -> dict:
        """
        This method returns a dictionary representation of the route, this allows external
        code to pull the internal state of the route for routing purposes
        :return: route : dict
        """
        route = {}
        assert isinstance(self.get_name(), str), "Route name must be of type str"
        route["name"] = self.get_name()
        assert isinstance(self.get_verb(), int), "Route HTTP verbs must be defined using Sego.Routing.Verb.HTTP_<verb>"
        assert self.get_verb() in [Verb.HTTP_GET, \
                                   Verb.HTTP_POST, \
                                   Verb.HTTP_PUT, \
                                   Verb.HTTP_DELETE], "Route HTTP verbs must be defined using Sego.Routing.Verb.HTTP_<verb>"
        route["verb"] = self.get_verb()
        assert isinstance(self.get_controller(), str), "Route controller must be of type str"
        route["controller"] = self.get_controller()
        assert isinstance(self.get_action(), str), "Route action must be of type str"
        route["action"] = self.get_action()
        assert isinstance(self.get_url(), str), "Route url must be of type str"
        route["url"] = self.get_url()
        assert  isinstance(self.get_middleware(),dict)," Middleware must be of type dict"
        route["middleware"] = self.get_middleware()
        assert isinstance(self.get_excluded_middleware(),dict),"Excluded middleware must be stored in a dict"
        route["excluded_middleware"] = self.get_excluded_middleware()

        return route
