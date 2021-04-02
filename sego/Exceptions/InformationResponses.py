from .SegoBaseException import SegoBaseException


class ContinueException100(SegoBaseException):
    message = '100 Continue'
    """ This interim
response indicates that everything so
far is OK and that the client should
continue the request, or ignore the
response if the request is already
finished. """


class SwitchingProtocolException101(SegoBaseException):
    message = '101 Switching Protocol'
    """ This code is sent
in response to an <a href="/en-US/docs/W
eb/HTTP/Headers/Upgrade"><code>Upgrade</
code></a> request header from the
client, and indicates the protocol the
server is switching to. """


class ProcessingException102(SegoBaseException):
    message = '102 Processing'
    """ This code
indicates that the server has received
and is processing the request, but no
response is available yet. """


class EarlyHintsException103(SegoBaseException):
    message = '103 Early Hints'
    """ This status code
is primarily intended to be used with
the <a href="/en-US/docs/Web/HTTP/Header
s/Link"><code>Link</code></a> header,
letting the user agent start <a
href="/en-US/docs/Web/HTML/Preloading_co
ntent">preloading</a> resources while
the server prepares a response. """
