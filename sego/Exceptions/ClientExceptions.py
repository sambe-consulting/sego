from . import SegoBaseException


class BadRequestException400(SegoBaseException):
    message = "400 Bad Request"


class UnauthorizedException402(SegoBaseException):
    message = "401 Unauthorized"


class ForbiddenException403(SegoBaseException):
    message = "403 Forbidden"


class NotFoundException404(SegoBaseException):
    message = "404 Not Found"


class MethodNotAllowedException405(SegoBaseException):
    message = "405 Method Not Allowed"


class NotAcceptableException406(SegoBaseException):
    message = "406 Not Acceptable"

class ProxyAuthenticationRequiredException407(SegoBaseException):
    message = "407 Proxy Authentication Required"


class ContinueException100:

    message = '100 Continue'
    """ This interim response indicates
    that everything so far is OK and that
    the client should continue the
    request, or ignore the response if
    the request is already finished. """



