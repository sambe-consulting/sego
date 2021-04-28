import sys, inspect, os

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)

import pytest

from sego.sego import Sego
from sego.Routing.Router import Router
from sego.Routing.Route import Route
from sego.Routing.Verb import Verb
from sego.Exceptions import *
from sego.Middlerware import Middleware



def test_basic_route_adding(router):
    router.add_route(Route("test", Verb.HTTP_GET, "TestController", "index", "/test/"))

def test_custom_exception_handler(sego, client):
    def on_exception(req, resp, exc):
        resp.text = "AttributeErrorHappened"

    sego.add_exception_handler(AttributeError,on_exception)

    @sego.route(Route("custom_exception", Verb.HTTP_GET, "", "", "/custom_exception"))
    def index(req, resp):
        raise AttributeError()

    response = client.get("http://segotestserver/custom_exception")
    assert response.text == "AttributeErrorHappened"

def test_template(views,sego, client):
    @sego.route(Route("html", Verb.HTTP_GET, "", "", "/html"))
    def html_handler(req, resp):
        # views = sego.get_view_environment()
        resp.body = views.render_view("tests/index.html", context={"title": "Some Title", "name": "Some Name"}).encode()

    response = client.get("http://segotestserver/html")

    assert "text/html" in response.headers["Content-Type"]
    assert "Some Title" in response.text
    assert "Some Name" in response.text


def test_route_overlap_throws_exception(router):
    router.add_route(Route("home", Verb.HTTP_GET, "HomeController", "index", "/home"))
    with pytest.raises(RouteAlreadyExistsException):
        router.add_route(Route("home", Verb.HTTP_GET, "HomeController", "index", "/home"))


def test_default_404_response(client,exception_handlers):
    response = client.get("http://segotestserver/doesnotexist")

    assert response.status_code == 404
    assert response.text == "Not Found"


def test_client_can_send_requests(sego, client):
    RESPONSE_TEXT = "SEGO IS ALIVE"

    @sego.route(Route(name="client_test", verb=Verb.HTTP_GET, controller="", action="", url="/client_test/"))
    def test_handler(req, resp):
        resp.text = RESPONSE_TEXT

    assert client.get("http://segotestserver/client_test/").text == RESPONSE_TEXT


def test_parameterized_route(sego, client):
    @sego.route(Route("main", Verb.HTTP_GET, "", "", "/{name}"))
    def hello(req, resp, name):
        resp.text = f"hey {name}"

    assert client.get("http://segotestserver/kabelo").text == "hey kabelo"
    assert client.get("http://segotestserver/kgotso").text == "hey kgotso"


# def test_middleware_methods_are_called(sego, client):
#     process_request_called = False
#     process_response_called = False
#
#     class CallMiddlewareMethods(Middleware):
#         def __init__(self, app):
#             super().__init__(app)
#
#         def process_request(self, req):
#             nonlocal process_request_called
#             process_request_called = True
#
#         def process_response(self, req, resp):
#             nonlocal process_response_called
#             process_response_called = True
#
#     sego.add_middleware(CallMiddlewareMethods)
