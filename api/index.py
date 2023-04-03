from flask import Flask, request
import tiktoken

app = Flask(__name__)

@app.route('/')
def index():
    string = request.args.get('string')
    encoding = request.args.get('encoding')

    if string is None:
        return short_readme()
    
    if encoding is None:
        encoding = 'cl100k_base'  
    
    encoder = tiktoken.get_encoding(encoding)
    num_tokens = len(encoder.encode(string))

    return {
        'string': string,
        'encoding': encoding,
        'num_tokens': num_tokens
    }


def short_readme():
    # return message sayin that a string was not provided
    return """
    <h1> tiktoken counter </h1>
    <p> This API counts the number of tokens in a string using tiktoken. </p>
    
    <h2> Usage </h2>
    <p> To use this API, simply make a GET request to current URL using the following parameters: </p>
    <p> <code> ?string=Hello+World&encoding=cl100k_base </code> </p>
    <p> The <code>string</code> parameter the string to be tokenized. </p>
    <p> The <code>encoding</code> parameter is optional and defaults to <code>cl100k_base</code>. </p>

    <h2> Github </h2>
    <p> For more information, see the <a href="https://github.com/chlouzada/tiktoken-counter">GitHub repository</a>. </p>
    """
