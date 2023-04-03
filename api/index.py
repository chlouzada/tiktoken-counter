from http.server import BaseHTTPRequestHandler
import tiktoken

class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        string = "This is a test for token count"
        encoding_name = "cl100k_base"

        encoding = tiktoken.get_encoding(encoding_name)
        num_tokens = len(encoding.encode(string))

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(str(num_tokens).encode('utf-8'))
        return
    