#!/usr/bin/env python3
'''
Networking script.
'''

import BaseHTTPRequestHandler

class IPHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        

def run(server_class=HTTPServer, handler_class=IPHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
    
