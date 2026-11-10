"""[房玄龄·2026-11-10] Minimal local/cloud lab HTTP adapter; no durable storage."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from contract import ContractError, summarize

MAX_BODY = 1024 * 1024

class Handler(BaseHTTPRequestHandler):
    def respond(self, status, payload):
        body = json.dumps(payload, allow_nan=False).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        # Exclude request bodies, headers, tokens, and URL parameters from logs.
        print(json.dumps({'severity':'INFO', 'message':'http request completed'}), flush=True)

    def do_GET(self):
        if self.path == '/healthz':
            self.respond(200, {'status':'ok'})
        elif self.path == '/version':
            self.respond(200, {'version':os.getenv('APP_VERSION', 'local-dev')})
        else:
            self.respond(404, {'error':'not found'})

    def do_POST(self):
        if self.path != '/validate':
            self.respond(404, {'error':'not found'})
            return
        if self.headers.get_content_type() != 'application/json':
            self.respond(415, {'error':'Content-Type must be application/json'})
            return
        try:
            length = int(self.headers.get('Content-Length', '-1'))
        except ValueError:
            self.respond(400, {'error':'invalid Content-Length'})
            return
        if not 0 <= length <= MAX_BODY:
            self.respond(413, {'error':'body length outside allowed range'})
            return
        self.connection.settimeout(10)
        try:
            payload = json.loads(self.rfile.read(length))
            result = summarize(payload)
        except (ValueError, UnicodeDecodeError, ContractError):
            self.respond(400, {'error':'invalid JSON or synthetic event contract'})
            return
        except TimeoutError:
            self.respond(408, {'error':'request body timeout'})
            return
        self.respond(200, result)

if __name__ == '__main__':
    # Cloud Run injects PORT. Local use is loopback-only unless HOST is explicit.
    host = os.getenv('HOST', '127.0.0.1')
    server = ThreadingHTTPServer((host, int(os.getenv('PORT', '8080'))), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
