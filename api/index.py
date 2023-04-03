from flask import Flask, request
import tiktoken

app = Flask(__name__)

@app.route('/')
def index():
    string = request.args.get('string')
    encoding = request.args.get('encoding')

    if string is None:
        string = 'Hello World'
    
    if encoding is None:
        encoding = 'cl100k_base'  
    
    encoder = tiktoken.get_encoding(encoding)
    num_tokens = len(encoder.encode(string))

    return {
        'string': string,
        'encoding': encoding,
        'num_tokens': num_tokens
    }

