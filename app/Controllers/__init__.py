from sego.sego import Sego


class BaseController:
    Sego   = Sego()
    Views  = Sego.get_view_environment()
    Router = Sego.get_router_object()

