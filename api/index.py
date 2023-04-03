from http.server import BaseHTTPRequestHandler
import tiktoken

class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        string = self.path.split('?')[1].split('=')[1]
        encoding_name = self.path.split('?')[2].split('=')[1]

        encoding = tiktoken.get_encoding(encoding_name)
        num_tokens = len(encoding.encode(string))

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(str(num_tokens).encode('utf-8'))
        return
    