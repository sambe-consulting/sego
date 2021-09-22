# ************************************************************************#
# Title:                    Sego  API                                     #
# Description:              This class is the main interface into  Sego   #
# Author:                   Sambe Consulting <development@sambe.co.za>    #
# Original Date:            10 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#
from requests import Session as RequestsSession
from orator import DatabaseManager,Schema,Model
from singleton_decorator import singleton
from confo.Confo import Confo
from .Routing.Router import *
import confo.Backends as BE
from flask import Flask
import inspect

@singleton
class Sego:

    def __init__(self, application_name=None):
        """
          This is the constructor for the sego object.

        :param application_name:
        """
        self.application_name = application_name
        self.flask_app = None
        self.exception_handlers = {}
        self.middleware = None
        self.templates_dir = None
        self.view_environment = None
        self.static_dir = None
        self.configuration_manager = Confo()
        self.router = Router()

    def register_middleware(self, middleware):
        pass


    def add_exception_handler(self, exception, handler, overwrite=False):
        """
        This method adds custom exception handlers to the Sego system.
        This defines a simple interface to handle and manage exceptions typical
        to the HTTP request handling
        :param exception:
        :param handler:
        :param overwrite:
        :return:
        """
        self.flask_app.register_error_handler(exception,handler)

    def register_exception_handlers(self, exception_handlers):
        """
        This method loads all defined handlers into the current session
        :param exception_handlers:
        :return:
        """
        self.exception_handlers = exception_handlers

    def register_static_files(self, static_dir):
        """
        This method registers a directory where static_files (images,css,js,...) are stored,
        this system allows us to serve static files from Sego
        :param static_dir:
        :return:
        """
        self.static_dir = static_dir

    def register_views(self, views):
        """
        This method loads all defined views/templates into the Sego application
        :param view:
        :return:
        """
        self.view_environment = views
        self.templates_dir = self.view_environment.get_view_path()

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
    def register_database(self):
        config = self.configuration_manager.get('database')
        self.database = DatabaseManager(config)
        self.schema = Schema(self.database)
        Model.set_connection_resolver(self.database)

    def setup_app(self):
        self.flask_app = Flask(self.application_name,
                               static_folder=self.static_dir,
                               static_url_path ="",
                               template_folder=self.templates_dir)
        self.router.load_flask_app(flask_app=self.flask_app)

        self.exception_handlers = __import__(self.exception_handlers)

    def get_app(self):
        """

        :return:
        """
        return self.flask_app

    def dev_run(self, host='0.0.0.0', port=9001, debug=False):
        """

        :param host:
        :param port:
        :param debug:
        :return:
        """
        self.flask_app.run(host=host, port=port, debug=debug)
