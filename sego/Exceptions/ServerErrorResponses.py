from .SegoBaseException import SegoBaseException


class InternalServerErrorException500(SegoBaseException):
    message = '500 Internal Server Error'
    """ The server has
encountered a situation it doesn't know
how to handle. """


class NotImplementedException501(SegoBaseException):
    message = '501 Not Implemented'
    """ The request
method is not supported by the server
and cannot be handled. The only methods
that servers are required to support
(and therefore that must not return this
code) are <code>GET</code> and
<code>HEAD</code> . """


class BadGatewayException502(SegoBaseException):
    message = '502 Bad Gateway'
    """ This error
response means that the server, while
working as a gateway to get a response
needed to handle the request, got an
invalid response. """


class ServiceUnavailableException503(SegoBaseException):
    message = '503 Service Unavailable'
    """ The server is not
ready to handle the request. Common
causes are a server that is down for
maintenance or that is overloaded. Note
that together with this response, a
user-friendly page explaining the
problem should be sent. This responses
should be used for temporary conditions
and the <code>Retry-After:</code> HTTP
header should, if possible, contain the
estimated time before the recovery of
the service. The webmaster must also
take care about the caching-related
headers that are sent along with this
response, as these temporary condition
responses should usually not be cached.
"""


class GatewayTimeoutException504(SegoBaseException):
    message = '504 Gateway Timeout'
    """ This error
response is given when the server is
acting as a gateway and cannot get a
response in time. """


class HTTPVersionNotSupportedException505(SegoBaseException):
    message = '505 HTTP Version Not Supported'
    """ The HTTP version
used in the request is not supported by
the server. """


class VariantAlsoNegotiatesException506(SegoBaseException):
    message = '506 Variant Also Negotiates'
    """ The server has an
internal configuration error: the chosen
variant resource is configured to engage
in transparent content negotiation
itself, and is therefore not a proper
end point in the negotiation process.
"""


class InsufficientStorageException507(SegoBaseException):
    message = '507 Insufficient Storage'
    """ The method could
not be performed on the resource because
the server is unable to store the
representation needed to successfully
complete the request. """


class LoopDetectedException508(SegoBaseException):
    message = '508 Loop Detected'
    """ The server
detected an infinite loop while
processing the request. """


class NotExtendedException510(SegoBaseException):
    message = '510 Not Extended'
    """ Further
extensions to the request are required
for the server to fulfill it. """


class NetworkAuthenticationRequiredException511(SegoBaseException):
    message = '511 Network Authentication Required'
    """ The 511 status
code indicates that the client needs to
authenticate to gain network access. """
