from http.server import HTTPServer
from common.settings import settings
from controller import WebHandler

LISTEN_PORT = settings.LISTEN_PORT


class Application(object):

    @staticmethod
    def listen():
        port = LISTEN_PORT
        print('starting server, port', port)

        # Server settings
        server_address = ('', port)
        httpd = HTTPServer(server_address, WebHandler.WebHandler)
        print('running server...')
        httpd.serve_forever()
