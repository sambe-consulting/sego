from .SegoBaseException import SegoBaseException


class OKException200(SegoBaseException):
    message = '200 OK'
    """ The request has
succeeded. The meaning of the success
depends on the HTTP method: <ul>
<li><code>GET</code>: The resource has
been fetched and is transmitted in the
message body.</li>
<li><code>HEAD</code>: The entity
headers are in the message body.</li>
<li><code>PUT</code> or
<code>POST</code>: The resource
describing the result of the action is
transmitted in the message body.</li>
<li><code>TRACE</code>: The message body
contains the request message as received
by the server.</li> </ul> """


class CreatedException201(SegoBaseException):
    message = '201 Created'
    """ The request has
succeeded and a new resource has been
created as a result. This is typically
the response sent after
<code>POST</code> requests, or some
<code>PUT</code> requests. """


class AcceptedException202(SegoBaseException):
    message = '202 Accepted'
    """ The request has
been received but not yet acted upon. It
is noncommittal, since there is no way
in HTTP to later send an asynchronous
response indicating the outcome of the
request. It is intended for cases where
another process or server handles the
request, or for batch processing. """


class NonAuthoritativeInformationException203(SegoBaseException):
    message = '203 Non-Authoritative Information'
    """ This response
code means the returned meta-information
is not exactly the same as is available
from the origin server, but is collected
from a local or a third-party copy. This
is mostly used for mirrors or backups of
another resource. Except for that
specific case, the "200 OK" response is
preferred to this status. """


class NoContentException204(SegoBaseException):
    message = '204 No Content'
    """ There is no
content to send for this request, but
the headers may be useful. The user-
agent may update its cached headers for
this resource with the new ones. """


class ResetContentException205(SegoBaseException):
    message = '205 Reset Content'
    """ Tells the user-
agent to reset the document which sent
this request. """


class PartialContentException206(SegoBaseException):
    message = '206 Partial Content'
    """ This response
code is used when the <a href="/en-US/do
cs/Web/HTTP/Headers/Range"><code>Range</
code></a> header is sent from the client
to request only part of a resource. """


class MultiStatusException207(SegoBaseException):
    message = '207 Multi-Status'
    """ Conveys
information about multiple resources,
for situations where multiple status
codes might be appropriate. """


class AlreadyReportedException208(SegoBaseException):
    message = '208 Already Reported'
    """ Used inside a
<code>&lt;dav:propstat&gt;</code>
response element to avoid repeatedly
enumerating the internal members of
multiple bindings to the same
collection. """


class IMUsedException226(SegoBaseException):
    message = '226 IM Used'
    """ The server has
fulfilled a <code>GET</code> request for
the resource, and the response is a
representation of the result of one or
more instance-manipulations applied to
the current instance. """
