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
import shutil
from sego.Views.Views import Views

from sego.Exceptions.ClientErrorResponses import NotFoundException404
from sego.Views.Views import Views


@pytest.fixture(scope="function")
def sego():
    os.mkdir("Configs/")
    os.mkdir("Configs/systemA")
    os.mkdir("public")
    sego = Sego()
    credentials = {"config_path":"Configs"}
    sego.register_configurations(credentials=credentials)
    static_files_dir = "public"
    sego.register_static_files(static_dir=static_files_dir)
    yield sego
    shutil.rmtree("Configs/")
    shutil.rmtree("public")

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
    markup = """
    <html>
         <header>
             <title>{{ title }}</title>
         </header>
         <body>
         <h1>The name of the framework is {{ name }}</h1>
         </body>
    </html>
    """
    os.mkdir("app")
    os.mkdir("app/templates")
    os.mkdir("app/templates/tests")
    with open("app/templates/tests/index.html","w+") as f:
        f.write(markup)
    views = Views(view_path="app/templates/")
    sego.register_views(views)
    yield views
    shutil.rmtree("app/")


@pytest.fixture
def exception_handlers(sego):
    def NotFoundHandler(request, response, exception):
        views = sego.get_view_environment()
        response.status_code = 404
        response.text = "Not Found"
    sego.add_exception_handler(NotFoundException404, NotFoundHandler)

