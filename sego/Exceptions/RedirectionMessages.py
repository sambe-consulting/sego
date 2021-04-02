from .SegoBaseException import SegoBaseException


class MultipleChoiceException300(SegoBaseException):
    message = '300 Multiple Choice'
    """ The request has
more than one possible response. The
user-agent or user should choose one of
them. (There is no standardized way of
choosing one of the responses, but HTML
links to the possibilities are
recommended so the user can pick.) """


class MovedPermanentlyException301(SegoBaseException):
    message = '301 Moved Permanently'
    """ The URL of the
requested resource has been changed
permanently. The new URL is given in the
response. """


class FoundException302(SegoBaseException):
    message = '302 Found'
    """ This response
code means that the URI of requested
resource has been changed
<em>temporarily</em> . Further changes
in the URI might be made in the future.
Therefore, this same URI should be used
by the client in future requests. """


class SeeOtherException303(SegoBaseException):
    message = '303 See Other'
    """ The server sent
this response to direct the client to
get the requested resource at another
URI with a GET request. """


class NotModifiedException304(SegoBaseException):
    message = '304 Not Modified'
    """ This is used for
caching purposes. It tells the client
that the response has not been modified,
so the client can continue to use the
same cached version of the response. """


class UseProxyException305(SegoBaseException):
    message = '305 Use Proxy'
    """ Defined in a
previous version of the HTTP
specification to indicate that a
requested response must be accessed by a
proxy. It has been deprecated due to
security concerns regarding in-band
configuration of a proxy. """


class unusedException306(SegoBaseException):
    message = '306 unused'
    """ This response
code is no longer used; it is just
reserved. It was used in a previous
version of the HTTP/1.1 specification.
"""


class TemporaryRedirectException307(SegoBaseException):
    message = '307 Temporary Redirect'
    """ The server sends
this response to direct the client to
get the requested resource at another
URI with same method that was used in
the prior request. This has the same
semantics as the <code>302 Found</code>
HTTP response code, with the exception
that the user agent <em>must not</em>
change the HTTP method used: If a
<code>POST</code> was used in the first
request, a <code>POST</code> must be
used in the second request. """


class PermanentRedirectException308(SegoBaseException):
    message = '308 Permanent Redirect'
    """ This means that
the resource is now permanently located
at another URI, specified by the
<code>Location:</code> HTTP Response
header. This has the same semantics as
the <code>301 Moved Permanently</code>
HTTP response code, with the exception
that the user agent <em>must not</em>
change the HTTP method used: If a
<code>POST</code> was used in the first
request, a <code>POST</code> must be
used in the second request. """
