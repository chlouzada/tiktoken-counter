from flask import Flask, request
import tiktoken

app = Flask(__name__)

@app.route('/')
def index():
    

    string = "This is a test for token count"
    encoding_name = "cl100k_base"

    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return str(num_tokens).encode('utf-8')

