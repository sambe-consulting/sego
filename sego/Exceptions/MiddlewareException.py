from .SegoBaseException import SegoBaseException


class MiddlewareAlreadyRegisteredException(SegoBaseException):
    """
    This class defines an exception that occurs when the same string is used to
    represent multiple entries of middleware into the Router
    """
    message = "A middleware with this name already exist, use a different name"

class MiddlewareNotFound(SegoBaseException):
    """
    This class defines an exceptipn that occurs when a middleware does not exist
    """
    message = "A middleware with this name does not exist,.."
