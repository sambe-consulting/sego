import sys, inspect, os

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
print(parentdir)
import pytest
from sego.sego import Sego
from sego.Routing.Router import Router
from sego.Routing.Route import Route
from sego.Routing.Verb import Verb
import shutil
from sego.Views.Views import Views

from sego.Exceptions import *


@pytest.fixture
def sego():
    os.mkdir("Configs/")
    os.mkdir("Configs/systemA")
    sego = Sego()
    credentials = {"config_path":"Configs"}
    sego.register_configurations(credentials=credentials)
    yield sego
    shutil.rmtree("Configs/")


@pytest.fixture
def route():
    return Route()

@pytest.fixture
def router():
    return Router()

@pytest.fixture
def verb():
    return Verb()

@pytest.fixture
def client(sego):
    return sego.test_session()

@pytest.fixture
def views(sego):
    views = Views(view_path="app/templates/")
    sego.register_views(views)
    return views
