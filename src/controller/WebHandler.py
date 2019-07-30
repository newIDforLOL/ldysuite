from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
from services import ScanService


class WebHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        query_path = urlparse(self.path)
        filepath, query = query_path.path, query_path.query
        print(filepath)
        if filepath == "/hello":
            self.router_hello(query)
        elif filepath == "/scan":
            self.router_scan()
        else:
            self.router_default()

    def router_hello(self, query):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.wfile.write(("hello %s" % query).encode("utf-8"))

    def router_scan(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        # get scan result
        scan = ScanService.ScanService()

        content = """
ip1:port1
ip2:port2
ip3:port3
        """
        self.wfile.write(content.encode("utf-8"))

    def router_default(self):
        self.send_response(404)
        self.wfile.write("Page Not Found".encode("utf-8"))
