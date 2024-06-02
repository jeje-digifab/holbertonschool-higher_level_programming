#!/usr/bin/python3
"""Module compiled with python3"""

import http.server
import json
import socketserver


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """
        Handle GET requests
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(response).encode())
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "status": "OK"
            }
            self.wfile.write(json.dumps(response).encode())
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404, "Not Found")
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=http.server.HTTPServer,
        handler_class=SimpleHTTPRequestHandler):
    """
    Set up and start the server on port 8000
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Serving on port 8000")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
