

from sego.sego import Sego
from sego.Views.Views import Views

views = Views(view_path="templates/")
app = Sego()
credentials = {"config_path":"Configurations/"}
app.register_configurations(credentials=credentials,)
routes_package_path = "routes"
app.register_routes(routes_package_path)
app.register_views(views)
