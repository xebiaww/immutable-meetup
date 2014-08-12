#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer


class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            return self.wfile.write("Hello World!")
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 8000), Handler)

server.serve_forever()