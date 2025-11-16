from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "Hola sjp0005"
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

if __name__ == "__main__":
    # Servidor escuchando en el puerto 3000
    server = HTTPServer(("0.0.0.0", 3000), SimpleHandler)
    print("Servidor arrancado en http://0.0.0.0:3000")
    server.serve_forever()
