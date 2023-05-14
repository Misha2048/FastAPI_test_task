# Test FastAPI Task

## Task

Write a service that parses given url's and return html.

There must be 1 API route: POST /parse that contains urls as a list of strings (no more than 50 in one request).

### Response example

```
{
   "example.com": "<html>...",
   "example2.com": "...",
   ...
}
```

Parsed results must be saved in MongoDB and used as a cache to use collected data in case of repeated requests.

### Requirements

- async FastAPI
- threading/async tasks
- motor
- docker