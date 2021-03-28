from sego.sego import Sego

app = Sego()
routes_package_path = "routes"
app.register_routes(routes_package_path)
