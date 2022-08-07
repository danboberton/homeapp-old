from spyne import Integer, Unicode, rpc, Iterable, Application, ServiceBase, srpc, String, UnsignedInteger
from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class LoggingService(ServiceBase):

    def __init__(self):
        self.app = Application([LoggingService], 'spyne.examples.hello.http',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11(),
                          )

    def runServer(self):
        wsgi_app = WsgiApplication(self.app)
        server = make_server('0.0.0.0', 8000, wsgi_app)
        server.serve_forever()


    @srpc(String, UnsignedInteger, _returns=Iterable(String))
    def say_hello(name, times):
        for i in range(times):
            yield 'Hello, %s' % name

    @srpc(String, _returns=Integer)
    def logEvent(name):
        for i in range(times):
            yield 'Hello, %s' % name



