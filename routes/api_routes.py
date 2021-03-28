from sego.Routing.Route import Route
from sego.Routing.Router import Router
from sego.Routing.Verb import Verb
router = Router()
router.add_route(Route("home",Verb.HTTP_GET,"HomeController","index","/home/{name}"))
router.add_route(Route("homed",Verb.HTTP_GET,"HomeController","index","/hodme"))