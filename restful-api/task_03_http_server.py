#!/usr/bin/python3
"""
This script starts a simple HTTP server and provides API endpoints
for serving basic data and information in JSON format.
"""

import http.server
import json

PORT = 8000
json_r = {"name": "John", "age": 30, "city": "New York"}
json_i = {"version": "1.0",
          "description": "A simple API built with http.server"}


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    A custom HTTP request handler that responds to GET requests.

    Endpoints:
        - '/': Returns a simple greeting message.
        - '/data': Returns a JSON object with name, age, and city.
        - '/info': Returns a JSON object with version and description.
        - Any other path: Returns a 404 response indicating that
        the endpoint is not found.

    Methods:
        do_GET():
            Handles the GET requests by serving different
            content depending on the path.
    """

    def do_GET(self):
        """
        Handles GET requests sent to the server.

        Depending on the path, it returns different responses:
        - '/' serves a welcome message in plain text.
        - '/data' serves a JSON object with user data.
        - '/info' serves a JSON object with API info.
        - For any other path, returns a 404 response.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(json_r, indent=4).encode("utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(json_i, indent=4).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


httpd = http.server.HTTPServer(('', PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
