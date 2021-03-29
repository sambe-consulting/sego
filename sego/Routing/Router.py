# ************************************************************************#
# Title:                    Sego Router                                   #
# Description:              This class handles all routing tasks for sego #
# Author:                   Kabelo Masemola <kn3rdydad@gmail.com>         #
# Original Date:            10 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#

from .Route import Route
from ..Exceptions import *
from parse import parse
from singleton_decorator import singleton
from confo.Confo import Confo
import ctypes


@singleton
class Router:
    def __init__(self):
        self.routes = []
        self.urls = []
        self.configuration_manager = Confo()

    def add_route(self, route: Route):
        route_parameter = route.get_route()
        self.validate(route_parameters=route_parameter)
        self.routes.append(route_parameter)
        self.urls.append(route_parameter["url"].rstrip("/"))

    def validate(self, route_parameters: dict):
        message = "Route with URL: " + route_parameters["url"] + " already exists."
        if route_parameters["url"].rstrip("/") in self.urls: raise RouteAlreadyExistsException(message)
        if route_parameters["name"] in list([r["name"] for r in self.routes]): raise UniqueNameException(
            " Use unique route names, " + route_parameters["name"] + " already exists.")

    def find_route(self, request_path):
        for route in self.routes:
            parse_result = parse(route["url"], request_path)

            if parse_result is not None:
                return route, parse_result.named
            else:
                parse_result = parse(route["url"].rstrip("/"), request_path.rstrip("/"))
                if parse_result is not None:
                    return route, parse_result.named



        return None, None

    def register_routes(self, route_paths):
        self.route_definitions = __import__(route_paths)

    def build_handler(self, route_parameters):
        Controller = route_parameters["controller"]
        action = route_parameters["action"]
        if Controller == "SegoBaseController":
            handler_id = self.configuration_manager.get("dynamic_routes",action)
            handler = ctypes.cast(handler_id, ctypes.py_object).value
            return handler

        controllersPackage = __import__("Controllers." + Controller)
        module = getattr(controllersPackage, Controller)
        _class = getattr(module, Controller)
        return getattr(_class(), action)

    def debug(self):
        return self.routes
