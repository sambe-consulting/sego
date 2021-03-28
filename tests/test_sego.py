import sys, inspect, os

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import pytest

from sego.sego import Sego
from sego.Routing.Router import Router
from sego.Routing.Route import Route
from sego.Routing.Verb import Verb
from sego.Routing.Exceptions import *



def test_basic_route_adding(router):
    router.add_route(Route("test", Verb.HTTP_GET, "TestController", "index", "/test/"))


def test_route_overlap_throws_exception(router):
    router.add_route(Route("home", Verb.HTTP_GET, "HomeController", "index", "/home"))
    with pytest.raises(RouteAlreadyExistsException):
        router.add_route(Route("home", Verb.HTTP_GET, "HomeController", "index", "/home"))

def test_default_404_response(client):
    response = client.get("http://segotestserver/doesnotexist")

    assert response.status_code == 404
    assert response.text == "Not found."

def test_client_can_send_requests(sego, client):
    RESPONSE_TEXT = "SEGO IS ALIVE"

    @sego.route(Route(name="test", verbs=Verb.HTTP_GET, controller="", action="",url= "/client_test/"))
    def test_handler(req, resp):
        resp.text = RESPONSE_TEXT

    assert client.get("http://segotestserver/client_test/").text == RESPONSE_TEXT

def test_parameterized_route(sego, client):
    @sego.route(Route("main", Verb.HTTP_GET, "", "", "/{name}"))
    def hello(req, resp, name):
        resp.text = f"hey {name}"

    assert client.get("http://segotestserver/kabelo").text == "hey kabelo"
    assert client.get("http://segotestserver/kgotso").text == "hey kgotso"

