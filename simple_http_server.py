#!/usr/bin/env python3
"""
Simple HTTP server to test connectivity with Chroma MCP.
This provides a basic health check endpoint.
"""

import http.server
import socketserver
import json

PORT = 8080

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ['/', '/health']:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                'status': 'healthy',
                'message': 'Chroma MCP HTTP server is running'
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                'status': 'error',
                'message': f'Path {self.path} not found'
            }
            self.wfile.write(json.dumps(response).encode())

if __name__ == "__main__":
    print(f"Starting simple HTTP server on port {PORT}")
    with socketserver.TCPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving at 0.0.0.0:{PORT}")
        httpd.serve_forever()