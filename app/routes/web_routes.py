from sego.Routing.Route import Route
from sego.Routing.Router import Router
from sego.Routing.Verb import Verb
from sego.sego import Sego
sego = Sego()

router = Router()  # route object

# EXAMPLE route

route_name = "homepage"  # The string name for this route instance
http_method = Verb.HTTP_GET  # The HTTP verb we are expecting
controller = "HomeController"  # The controller, to handle custom routing logic
action = "index"  # The specific action the controller will execute
url = "/"  # The path we are expecting

# A route is defined
homepage_route = Route(name=route_name, \
              verbs=http_method, \
              controller=controller, \
              action=action, \
              url=url)

#add the route to the router
router.add_route(homepage_route)

# @sego.route(Route("html", Verb.HTTP_GET, "", "", "/html"))
# def html_handler(req, resp):
#     views = sego.get_view_environment()
#     resp.body = views.render_view("tests/index.html", context={"title": "Some Title", "name": "Some Name"}).encode()
