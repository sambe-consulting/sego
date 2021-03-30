from . import SegoBaseException


class ConfigurationNotLoadedException(SegoBaseException):
    message = "Configuration has not been loaded"
