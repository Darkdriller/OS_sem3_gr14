from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading

class Handler(SimpleHTTPRequestHandler):
    pass
    # def do_GET(self):
    #     # f = self.send_head()
    #     # if f:
    #     #     try:
    #     #         self.copyfile(f, self.wfile)
    #     #     finally:
    #     #
    #     self.send_response(200)
    #     self.end_headers()
    #     message =  threading.currentThread().getName()
    #     self.wfile.write(message.encode())
    #     self.wfile.write('\n'.encode())
    #     return
# class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
#     """Handle requests in a separate thread."""
#     pass
if __name__ == '__main__':
    # server = ThreadedHTTPServer(('localhost', 8080), Handler)
    server = HTTPServer(('localhost', 8081), Handler)
    print ('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
