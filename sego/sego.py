# ************************************************************************#
# Title:                    Sego  API                                     #
# Description:              This class is the main interface into  Sego   #
# Author:                   Sambe Consulting <development@sambe.co.za     #
# Original Date:            10 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#
from wsgiadapter import WSGIAdapter as RequestsWSGIAdapter
from requests import Session as RequestsSession
from singleton_decorator import singleton
from webob import Request, Response
from .Routing.Router import Router
from confo.Confo import Confo
import confo.Backends as BE
from .Exceptions import *
import uuid, os


@singleton
class Sego:
    def __init__(self, application_name=None):
        self.router = Router()
        self.configuration_manager = Confo()
        if application_name == None:
            application_name = str(uuid.uuid4())
        self.application_name = application_name
        self.view_environment = None

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handles_request(request)
        return response(environ, start_response)

    def get_application_name(self):
        return self.application_name

    def route(self, route):

        def wrapper(handler):
            action = str(handler.__name__)
            route.set_action(action=action)
            route.set_controller(controller="SegoBaseController")
            self.configuration_manager.set("dynamic_routes", action, id(handler))
            self.router.add_route(route)
            return handler

        return wrapper

    def register_routes(self, routes_package):
        self.router.register_routes(routes_package)

    def get_router_object(self):
        return self.router

    def register_views(self, view):
        self.view_environment = view

    def get_view_environment(self):
        return self.view_environment

    def register_configurations(self, credentials, backend_type=BE.FILE_BACKEND):
        self.configuration_manager.load_backend(credentials=credentials, name=self.application_name,
                                                backend_type=backend_type)
        self.configuration_manager.activate_backend(backend_name=self.application_name)
        self.configuration_manager.create_namespace(self.application_name)
        self.configuration_manager.use_namespace(self.application_name)

    def default_response(self, response):
        response.status_code = 404
        response.text = "Not found."

    def handles_request(self, request):
        response = Response()
        route_parameters,kwargs = self.router.find_route(request=request)
        if route_parameters is not None:
            handler = self.router.build_handler(route_parameters=route_parameters)
            handler(request, response, **kwargs)
        else:
            self.default_response(response)

        return response

    def test_session(self, base_url="http://segotestserver"):
        session = RequestsSession()
        session.mount(prefix=base_url, adapter=RequestsWSGIAdapter(self))
        return session
