from .SegoBaseException import SegoBaseException


class MiddlewareAlreadyRegisteredException(SegoBaseException):
    """
    This class defines an exception that occurs when the same string is used to
    represent multiple entries of middleware into the Router
    """
    message = "A middleware with this name already exist, use a different name"


class MiddlewareNotFound(SegoBaseException):
    """
    This class defines an exception that occurs when a middleware does not exist
    """
    message = "A middleware with this name does not exist,.."


class MiddlewareNameMustBeString(SegoBaseException):
    """
    This class defines an exception that occurs when a type other than 'str' is sent to middleware
    loader as a name
    """

    message = "The 'middleware_name' argument must be of type  'str' "


class MiddlewareOverwriteMustBeBoolean(SegoBaseException):
    """
    This class defines an exception that occurs when
    """
    message = "The 'overwrite' must be of type  'boolean' "


class MiddlewareMustHaveName(SegoBaseException):
    message = "The middleware must have a 'name' key with value of type 'str' "


class MiddlewareMustExtend(SegoBaseException):
    message = "All middleware must extend Sego.Middleware"



