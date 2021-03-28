# ************************************************************************#
# Title:                    Sego  API                                     #
# Description:              This class is the main interface into  Sego   #
# Author:                   Sambe Consulting <development@sambe.co.za     #
# Original Date:            10 March 2021                                 #
# Version:                  0.1.0                                         #
# ************************************************************************#

from webob import Request, Response

from .Routing.Router import Router


class Sego:
    def __init__(self):
        self.router = Router()

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handles_request(request)
        return response(environ, start_response)

    def register_routes(self, routes_package):
        self.router.register_routes(routes_package)

    def default_response(self, response):
        response.status_code = 404
        response.text = "Not found."

    def handles_request(self, request):
        response = Response()
        route_parameters, kwargs = self.router.find_route(request_path=request.path)
        if route_parameters is not None:
            handler = self.router.build_handler(route_parameters=route_parameters)
            handler(request, response, **kwargs)
        else:
            self.default_response(response)

        return response
