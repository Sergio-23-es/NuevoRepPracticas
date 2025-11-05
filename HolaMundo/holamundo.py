from http.server import SimpleHTTPRequestHandler, HTTPServer

# Configurar dirección y puerto
host = "localhost"
port = 4918

# Crear una clase que maneje las peticiones HTTP
class HolaMundoHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Responder a cualquier petición GET con texto HTML
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        mensaje = "<html><body><h1>¡Hola Mundo!</h1></body></html>"
        self.wfile.write(mensaje.encode("utf-8"))

# Crear y ejecutar el servidor
if __name__ == "__main__":
    with HTTPServer((host, port), HolaMundoHandler) as server:
        print(f"Servidor corriendo en http://{host}:{port}")
        server.serve_forever()
