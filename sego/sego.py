# ************************************************************************#
# Title:                    Sego  API                                     #
# Description:              This class is the main interface into  Sego   #
# Author:                   Sambe Consulting <development@sambe.co.za>    #
# Original Date:            10 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#
from wsgiadapter import WSGIAdapter as RequestsWSGIAdapter
from .Response.Response import Response as SegoResponse
from requests import Session as RequestsSession
from orator import DatabaseManager,Schema,Model
from singleton_decorator import singleton
from .Routing.Router import Router
from whitenoise import WhiteNoise
from confo.Confo import Confo
import confo.Backends as BE
from webob import Request
from .Exceptions import *
from .Middleware import *
import uuid, os
import inspect




@singleton
class Sego:
    def __init__(self, application_name=None):
        self.database = None
        self.router = Router()
        self.configuration_manager = Confo()
        if application_name == None:
            application_name = str(uuid.uuid4())
        self.application_name = application_name
        self.view_environment = None
        self.exception_handlers = {}
        self.app_exception = None
        self.static_file_manager = None
        self.middleware_manager = MiddlewareManager()
        self.middleware = None
        self.route_parameters = None
        self.session_kwargs = None

    def __call__(self, environ, start_response):
        """
        This method defines the callable interface into sego
        :param environ:
        :param start_response:
        :return:
        """
        return self.static_file_manager(environ, start_response)

    def wsgi_app(self, environ, start_response) -> Response:
        """
        This method defines an entry point into the WSGI (Web Server Gateway Interface)
        application
        :param environ:
        :param start_response:
        :return: response : webob.Response
        """

        request = Request(environ)
        self.route_parameters, self.session_kwargs = self.router.find_route(request=request)
        if self.route_parameters is not None:
            self.middleware_manager.process_middleware(stage=Middleware.PREPROCESS,\
                                                       route=self.route_parameters,\
                                                       request=request,\
                                                       response=None)

        response = self.handle_request(request)
        if self.route_parameters is not None:
            self.middleware_manager.process_middleware(stage=Middleware.POSTPROCESS,\
                                                   route=self.route_parameters,\
                                                   request=request,\
                                                   response=response)
        return response(environ, start_response)

    def get_application_name(self) -> str:
        """
        This simple getter returns the application name whether generated or set at Sego's instantiation
        :return: application_name
        """
        return self.application_name

    def route(self, route) -> object:
        """
         This wrapper method is used to define a Flask style routing interface.
         Instead of taking in strings like flask we are taking in Route object
        :param route:
        :return: handler : object
        """

        def wrapper(handler):
            """
            To make sure that the Flask style routes are can be executed by the normal router
            the route is dynamically updated by adding 'SegoBaseController' and the name of the wrapped
            method to the route.The we use the configuration manager to store the object ID for later usage
            :param handler:
            :return:
            """
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
        """
        This method loads all defined routes into the Sego application
        :param routes_package:
        :return:
        """
        self.router.register_routes(routes_package)

    def get_router_object(self):
        """
        This method returns the router object
        :return: router : Router
        """
        return self.router

    def register_views(self, view):
        """
        This method loads all defined views/templates into the Sego application
        :param view:
        :return:
        """
        self.view_environment = view

    def get_view_environment(self):
        """
        This method returns the loaded view environment
        :return: view_environment : jinja2.Environment
        """
        return self.view_environment

    def register_configurations(self, credentials, backend_type=BE.FILE_BACKEND):
        """
        This method starts the configuration manager, using confo (https://github.com/sambe-consulting/confo)
        It defaults to FILE_BACKEND but ZOOKEEPER_BACKEND can be used too
        :param credentials:
        :param backend_type:
        :return:
        """
        self.configuration_manager.load_backend(credentials=credentials, name=self.application_name,
                                                backend_type=backend_type)
        self.configuration_manager.activate_backend(backend_name=self.application_name)
        self.configuration_manager.create_namespace(self.application_name)
        self.configuration_manager.use_namespace(self.application_name)

    def handle_request(self, request):
        """
        This method handles all requests, by using the Sego Router object
        :param request:
        :return: webob.Response
        """
        response = SegoResponse()
        route_parameters = self.route_parameters
        kwargs = self.session_kwargs


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
        """
        This method adds custom exception handlers to the Sego system.
        This defines a simple interface to handle and manage exceptions typicall
        to the HTTP request handling
        :param exception:
        :param handler:
        :param overwrite:
        :return:
        """
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
        """
        This method loads all defined handlers into the current session
        :param exception_path:
        :return:
        """
        self.app_exception = __import__(exception_path)

    def get_exception_handlers(self):
        """
        This method returns loaded exception handlers
        :return: exception_handlers : dict
        """
        return self.exception_handlers

    def handle_exceptions(self, request, response, exception):
        """
        This method handles exceptions as they are thrown through out
        the application code base.This system will match a known exception
        to the appropriate handler if a handler is not found then the error
        with be raised again to be handled by the developer
        :param request:
        :param response:
        :param exception:
        :return:
        """
        exception_name = exception.__class__.__name__

        if exception_name in self.exception_handlers:
            handler = self.exception_handlers[exception_name]
            handler(request, response, exception)
        else:
            raise exception

    def register_static_files(self,static_dir):
        """
        This method registers a directory where static_files (images,css,js,...) are stored,
        this system allows us to serve static files from Sego
        :param static_dir:
        :return:
        """
        self.static_file_manager = WhiteNoise(self.wsgi_app, root=static_dir)

    def register_middleware(self,middleware):
        self.middleware = __import__(middleware)

    def register_database(self):
        config = self.configuration_manager.get('database')
        self.database = DatabaseManager(config)
        self.schema = Schema(self.database)
        Model.set_connection_resolver(self.database)

    def test_session(self, base_url="http://segotestserver"):
        """
        This methid defines a dummy session to be used by pytest
        :param base_url:
        :return: session: RequestSession
        """
        session = RequestsSession()
        session.mount(prefix=base_url, adapter=RequestsWSGIAdapter(self))
        return session
