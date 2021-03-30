# ************************************************************************#
# Title:                    Sego Route                                    #
# Description:              This class handles definition of routes       #
# Author:                   Kabelo Masemola <kn3rdydad@gmail.com>         #
# Original Date:            10 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#

from .Verb import Verb
from ..Exceptions import *

class Route:
    def __init__(self, name: str = None, verbs: int = None, controller: str = None, action: str = None,
                 url: str = None):
        self.name = name
        self.verbs = verbs
        self.controller = controller
        self.action = action
        self.url = url

    def set_name(self, name):
        self.name = name
        return self

    def get_name(self):
        return self.name

    def set_verb(self, verb):
        self.verbs = list(set(self.verbs.append(verb)))
        return self

    def get_verb(self):
        return self.verbs

    def set_controller(self, controller):
        self.controller = controller
        return self

    def get_controller(self):
        return self.controller

    def set_action(self, action):
        self.action = action
        return self

    def get_action(self):
        return self.action

    def set_url(self, url):
        self.url = url
        return self

    def get_url(self):
        return self.url

    def get_route(self):
        route = {}
        assert isinstance(self.get_name(), str), "Route name must be of type str"
        route["name"] = self.get_name()
        assert isinstance(self.get_verb(), int), "Route HTTP verbs must be defined using Sego.Routing.Verb.HTTP_<verb>"
        assert self.get_verb() in [Verb.HTTP_GET, \
                                   Verb.HTTP_POST, \
                                   Verb.HTTP_PUT, \
                                   Verb.HTTP_DELETE], "Route HTTP verbs must be defined using Sego.Routing.Verb.HTTP_<verb>"
        route["verbs"] = self.get_verb()
        assert isinstance(self.get_controller(), str), "Route controller must be of type str"
        route["controller"] = self.get_controller()
        assert isinstance(self.get_action(), str), "Route action must be of type str"
        route["action"] = self.get_action()
        assert isinstance(self.get_url(), str), "Route url must be of type str"
        route["url"] = self.get_url()

        return route
