from flask import Flask, request
import tiktoken

app = Flask(__name__)

@app.route('/')
def index():
    string = request.args.get('string')
    encoding = request.args.get('encoding')
    
    encoder = tiktoken.get_encoding(encoding)
    num_tokens = len(encoder.encode(string))
    
    return str(num_tokens)

