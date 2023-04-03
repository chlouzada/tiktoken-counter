# tiktoken-counter

Count the number of token in a given string using [tiktoken](https://github.com/openai/tiktoken).


## Usage

To count the number of tokens in a string, make a GET request to the following endpoint:
 
```
https://tiktoken-counter.vercel.app/?string=<string>&encoding=<encoding>
```

## Parameters

|  Parameter | Description  |
|---|---|
| string  | 	The string to count the number of tokens. |
| encoding  | 	The encoding to use. This parameter is optional and defaults to cl100k_base. See the table below for a list of available encodings.  |

|  Encoding | OpenAI Models  | 
|---|---|
| cl100k_base (default)  |gpt-4, gpt-3.5-turbo, text-embedding-ada-002  |
| p50k_base  |  Codex models, text-davinci-002, text-davinci-003 |
|  r50k_base (or gpt2) | davinci  |


## Example

For example, to count the number of tokens in the string "Hello, world!" using the r50k_base encoding, make a GET request to the following URL:

```
https://tiktoken-counter.vercel.app/?string=Hello,%20world!&encoding=r50k_base
```

## Response

```json
{
  "encoding": <encoding>,
  "num_tokens": <num_tokens>,
  "string": <string>
}
```