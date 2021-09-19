from .SegoBaseException import SegoBaseException


class BadRequestException400(SegoBaseException):
    message = '400 Bad Request'
    """ The server could
not understand the request due to
invalid syntax. """


class UnauthorizedException401(SegoBaseException):
    message = '401 Unauthorized'
    """ Although the HTTP
standard specifies "unauthorized",
semantically this response means
"unauthenticated". That is, the client
must authenticate itself to get the
requested response. """


class PaymentRequiredException402(SegoBaseException):
    message = '402 Payment Required'
    """ This response
code is reserved for future use. The
initial aim for creating this code was
using it for digital payment systems,
however this status code is used very
rarely and no standard convention
exists. """


class ForbiddenException403(SegoBaseException):
    message = '403 Forbidden'
    """ The client does
not have access rights to the content;
that is, it is unauthorized, so the
server is refusing to give the requested
resource. Unlike 401, the client's
identity is known to the server. """


class NotFoundException404(SegoBaseException):
    message = '404 Not Found'
    """ The server can
not find the requested resource. In the
browser, this means the URL is not
recognized. In an API, this can also
mean that the endpoint is valid but the
resource itself does not exist. Servers
may also send this response instead of
403 to hide the existence of a resource
from an unauthorized client. This
response code is probably the most
famous one due to its frequent
occurrence on the web. """


class MethodNotAllowedException405(SegoBaseException):
    message = '405 Method Not Allowed'
    """ The request
method is known by the server but has
been disabled and cannot be used. For
example, an API may forbid DELETE-ing a
resource. The two mandatory methods,
<code>GET</code> and <code>HEAD</code> ,
must never be disabled and should not
return this error code. """


class NotAcceptableException406(SegoBaseException):
    message = '406 Not Acceptable'
    """ This response is
sent when the web server, after
performing <a href="/en-US/docs/Web/HTTP
/Content_negotiation#server-
driven_negotiation">server-driven
content negotiation</a> , doesn't find
any content that conforms to the
criteria given by the user agent. """


class ProxyAuthenticationRequiredException407(SegoBaseException):
    message = '407 Proxy Authentication Required'
    """ This is similar
to 401 but authentication is needed to
be done by a proxy. """


class RequestTimeoutException408(SegoBaseException):
    message = '408 Request Timeout'
    """ This response is
sent on an idle connection by some
servers, even without any previous
request by the client. It means that the
server would like to shut down this
unused connection. This response is used
much more since some browsers, like
Chrome, Firefox 27+, or IE9, use HTTP
pre-connection mechanisms to speed up
surfing. Also note that some servers
merely shut down the connection without
sending this message. """


class ConflictException409(SegoBaseException):
    message = '409 Conflict'
    """ This response is
sent when a request conflicts with the
current state of the server. """


class GoneException410(SegoBaseException):
    message = '410 Gone'
    """ This response is
sent when the requested content has been
permanently deleted from server, with no
forwarding address. Clients are expected
to remove their caches and links to the
resource. The HTTP specification intends
this status code to be used for
"limited-time, promotional services".
APIs should not feel compelled to
indicate resources that have been
deleted with this status code. """


class LengthRequiredException411(SegoBaseException):
    message = '411 Length Required'
    """ Server rejected
the request because the <code>Content-
Length</code> header field is not
defined and the server requires it. """


class PreconditionFailedException412(SegoBaseException):
    message = '412 Precondition Failed'
    """ The client has
indicated preconditions in its headers
which the server does not meet. """


class PayloadTooLargeException413(SegoBaseException):
    message = '413 Payload Too Large'
    """ Request entity is
larger than limits defined by server;
the server might close the connection or
return an <code>Retry-After</code>
header field. """


class URITooLongException414(SegoBaseException):
    message = '414 URI Too Long'
    """ The URI requested
by the client is longer than the server
is willing to interpret. """


class UnsupportedMediaTypeException415(SegoBaseException):
    message = '415 Unsupported Media Type'
    """ The media format
of the requested data is not supported
by the server, so the server is
rejecting the request. """


class RangeNotSatisfiableException416(SegoBaseException):
    message = '416 Range Not Satisfiable'
    """ The range
specified by the <code>Range</code>
header field in the request can't be
fulfilled; it's possible that the range
is outside the size of the target URI's
data. """


class ExpectationFailedException417(SegoBaseException):
    message = '417 Expectation Failed'
    """ This response
code means the expectation indicated by
the <code>Expect</code> request header
field can't be met by the server. """


class ImateapotException418(SegoBaseException):
    message = '418 Im a teapot'
    """ The server
refuses the attempt to brew coffee with
a teapot. """


class MisdirectedRequestException421(SegoBaseException):
    message = '421 Misdirected Request'
    """ The request was
directed at a server that is not able to
produce a response. This can be sent by
a server that is not configured to
produce responses for the combination of
scheme and authority that are included
in the request URI. """


class UnprocessableEntityException422(SegoBaseException):
    message = '422 Unprocessable Entity'
    """ The request was
well-formed but was unable to be
followed due to semantic errors. """


class LockedException423(SegoBaseException):
    message = '423 Locked'
    """ The resource that
is being accessed is locked. """


class FailedDependencyException424(SegoBaseException):
    message = '424 Failed Dependency'
    """ The request
failed due to failure of a previous
request. """


class TooEarlyException425(SegoBaseException):
    message = '425 Too Early'
    """ Indicates that
the server is unwilling to risk
processing a request that might be
replayed. """


class UpgradeRequiredException426(SegoBaseException):
    message = '426 Upgrade Required'
    """ The server
refuses to perform the request using the
current protocol but might be willing to
do so after the client upgrades to a
different protocol. The server sends an
<a href="/en-US/docs/Web/HTTP/Headers/Up
grade"><code>Upgrade</code></a> header
in a 426 response to indicate the
required protocol(s). """


class PreconditionRequiredException428(SegoBaseException):
    message = '428 Precondition Required'
    """ The origin server
requires the request to be conditional.
This response is intended to prevent the
'lost update' problem, where a client
GETs a resource's state, modifies it,
and PUTs it back to the server, when
meanwhile a third party has modified the
state on the server, leading to a
conflict. """


class TooManyRequestsException429(SegoBaseException):
    message = '429 Too Many Requests'
    """ The user has sent
too many requests in a given amount of
time ("rate limiting"). """


class RequestHeaderFieldsTooLargeException431(SegoBaseException):
    message = '431 Request Header Fields Too Large'
    """ The server is
unwilling to process the request because
its header fields are too large. The
request may be resubmitted after
reducing the size of the request header
fields. """


class UnavailableForLegalReasonsException451(SegoBaseException):
    message = '451 Unavailable For Legal Reasons'
    """ The user-agent
requested a resource that cannot legally
be provided, such as a web page censored
by a government. """
