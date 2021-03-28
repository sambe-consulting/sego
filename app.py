

from sego.sego import Sego
from sego.Routing.Route import Route
from sego.Routing.Verb import Verb

app = Sego()
credentials = {"config_path":"Configurations/"}
app.register_configurations(credentials=credentials,)
routes_package_path = "routes"
app.register_routes(routes_package_path)
