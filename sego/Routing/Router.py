# ************************************************************************#
# Title:                    Sego Router                                   #
# Description:              This class handles all routing tasks for sego #
# Author:                   Kabelo Masemola <kn3rdydad@gmail.com>         #
# Original Date:            10 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#

from .Route import Route
from .Verb import Verb
from ..Exceptions import *
from singleton_decorator import singleton
from confo.Confo import Confo
import ctypes


@singleton
class Router:
    def __init__(self):
        """
        This constructor sets up the Router object by instantiating routes,urls and config_manager
        """
        self.routes = []
        self.urls = []
        self.configuration_manager = Confo()
        self.flask_app = None

    def add_route(self, route: Route):
        """
        This method registers a new Route object
        :param route:
        :return:
        """
        route_parameter = route.get_route()
        self.validate(route_parameters=route_parameter)
        self.routes.append(route_parameter)
        self.urls.append(route_parameter["url"].rstrip("/"))

    def validate(self, route_parameters: dict):
        """
        This method is used to validate if a Route object has been given all the correct
        parameters and to enforce uniqueness constraints
        :param route_parameters:
        :return:
        """
        message = "Route with URL: " + route_parameters["url"] + " already exists."
        if route_parameters["url"].rstrip("/") in self.urls: raise RouteAlreadyExistsException(message)
        if route_parameters["name"] in list([r["name"] for r in self.routes]): raise UniqueNameException(
            " Use unique route names, " + route_parameters["name"] + " already exists.")

    def load_flask_app(self,flask_app):
        """
         Load flask app into the routing system
        :param flask_app:
        :return:
        """
        self.flask_app = flask_app
        for route in self.routes:
            self.flask_app.add_url_rule(rule=route['url'],
                                        endpoint=route['name'],
                                        view_func=self.build_handler(route),
                                        methods=[Verb().get_string(route['verb'])])


    def register_routes(self, route_paths):
        """
        This method loads all defined routes by registering the
        relevant modules
        :param route_paths:
        :return:
        """
        self.route_definitions = __import__(route_paths)

    def dynamic_import(self, controller):
        """
        This method is used to dynamically load the relevant controller and action into
        a variable
        :param controller:
        :return: _class : Object
        """
        controller_components = controller.split(".")
        controller_components.insert(0, "Controllers")
        controller_components.insert(0, "app")
        controller_path = '.'.join(controller_components)
        module = __import__(name=controller_path, fromlist=controller_components)
        _class = getattr(module, controller_components[-1])
        return _class

    def build_handler(self, route_parameters):
        """
        This special method is used when using the Flask style routes, it using meta-programming to
        create a controller for the method then links the action, them makes them callable ,the send control
        back to the normal execution path
        :param route_parameters:
        :return:
        """
        Controller = route_parameters["controller"]
        action = route_parameters["action"]
        if Controller == "SegoBaseController":
            handler_id = self.configuration_manager.get("dynamic_routes", action)
            handler = ctypes.cast(handler_id, ctypes.py_object).value
        else:
            _class = self.dynamic_import(Controller)
            handler = getattr(_class(),action)

        return handler

    def get_routes(self):
        """
        This method returns all load routes for debug purposes
        :return: routes
        """
        return self.routes
