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
from whitenoise import WhiteNoise
from confo.Confo import Confo
import confo.Backends as BE
from .Exceptions import *
import uuid, os
import inspect



@singleton
class Sego:
    def __init__(self, application_name=None):
        self.router = Router()
        self.configuration_manager = Confo()
        if application_name == None:
            application_name = str(uuid.uuid4())
        self.application_name = application_name
        self.view_environment = None
        self.exception_handlers = {}
        self.app_exception = None
        self.static_file_manager = None

    def __call__(self, environ, start_response):
        return self.static_file_manager(environ, start_response)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def get_application_name(self):
        return self.application_name

    def route(self, route):

        def wrapper(handler):
            try:
                action = str(handler.__name__)
                route.set_action(action=action)
                route.set_controller(controller="SegoBaseController")
                self.configuration_manager.set("dynamic_routes", action, id(handler))
                self.router.add_route(route)
            except Exception as e:
                self.handle_exceptions({}, {}, e)

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

    def handle_request(self, request):
        response = Response()
        route_parameters, kwargs = self.router.find_route(request=request)
        try:
            if route_parameters is not None:
                handler = self.router.build_handler(route_parameters=route_parameters)
                handler(request, response, **kwargs)
            else:
                raise NotFoundException404("Page not found")
        except Exception as e:
            self.handle_exceptions(request, response, e)
        return response

    def add_exception_handler(self, exception, handler, overwrite=False):
        if inspect.isclass(exception):
            exception = exception.__name__

        if exception in self.exception_handlers:
            if overwrite:
                self.exception_handlers[exception] = handler
            else:
                raise Exception("Exception already registered, to force the registration, set 'overwrite' to True")
        else:
            self.exception_handlers[exception] = handler

    def register_exception_handlers(self, exception_path):
        self.app_exception = __import__(exception_path)

    def get_exception_handlers(self):
        return self.exception_handlers

    def handle_exceptions(self, request, response, exception):
        exception_name = exception.__class__.__name__

        if exception_name in self.exception_handlers:
            handler = self.exception_handlers[exception_name]
            handler(request, response, exception)
        else:
            raise exception

    def register_static_files(self,static_dir):
        self.static_file_manager = WhiteNoise(self.wsgi_app, root=static_dir)

    def test_session(self, base_url="http://segotestserver"):
        session = RequestsSession()
        session.mount(prefix=base_url, adapter=RequestsWSGIAdapter(self))
        return session
