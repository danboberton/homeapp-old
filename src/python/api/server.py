from spyne import Integer, Unicode, rpc, Iterable, Application, ServiceBase, srpc, String, UnsignedInteger, \
    ResourceNotFoundError
from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from ..server import logic

# class ServerApp(Application):
#
#     def __init__(self, Logger, Config):

class MyApplication(Application):
    def call_wrapper(self, ctx):
        try:
            return super(MyApplication, self).call_wrapper(ctx)

        except KeyError:
            raise ResourceNotFoundError(ctx.in_object)

class LoggingService(ServiceBase):

    def _on_method_call(self, ctx):
        ctx.udc = logic.UserDefinedContext(self.logger, self.config)

    def __init__(self, Logger, Config):
        self.logger = Logger
        self.app = MyApplication([LoggingService], 'spyne.examples.hello.http',
                               in_protocol=Soap11(validator='lxml'),
                               out_protocol=Soap11(),
                               )
        self.app.event_manager.add_listener('method_call', self._on_method_call)
        self.logger.log("Application built", printLog=True)
        self.config = Config

    def runServer(self):
        wsgi_app = WsgiApplication(self.app)
        server = make_server(self.config.serverIP, self.config.serverPort, wsgi_app)
        self.logger.log("Starting Server ... ", printLog=True)
        server.serve_forever()

    @rpc(String, Integer, _returns=Integer)
    def logEvent(ctx, key, value):
        ctx.udc.logEvent(key, value)
        return 0
