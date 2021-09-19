# ************************************************************************#
# Title:                    Sego  API                                     #
# Description:              This class is the main interface into  Sego   #
# Author:                   Sambe Consulting <development@sambe.co.za>    #
# Original Date:            10 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#

from singleton_decorator import singleton

@singleton
class Sego:

    def __init__(self,application_name=None):
        """
          This is the constructor for the sego object.

        :param application_name:
        """
        self.application_name = application_name
        self.flask_app =None
        self.exception_handlers = None
        self.middleware = None
        self.templates = None
        self.static_dir = None
        self.configuration_manager = None
        # self.


    def register_middleware(self,middleware):
        pass

    def register_exception_handlers(self,exception_handlers):
        pass

    def register_static_files(self,static_dir):
        pass

    def register_views(self,views):
        pass

    def register_configurations(self,confo_credentials):
        pass

    def register_routes(self,routes_package_path):
        pass

    def register_database(self):
        pass

    def setup_app(self):
        pass

    def run(self,host,port,debug=False):
        pass
