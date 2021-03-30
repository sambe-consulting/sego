from . import SegoBaseException


class UnknownHTTPMethodException(SegoBaseException):
    message = "HTTP accepts only these verbs: GET, POST,PUT and DELETE"
