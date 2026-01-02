import http.server
import socketserver
import os

PORT = 8765
WORKSPACE = os.getcwd()

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"SuperBrain workspace: {WORKSPACE}".encode())

if __name__ == "__main__":
    print(f"Starting noizy server at http://127.0.0.1:{PORT} (workspace: {WORKSPACE})")
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()
