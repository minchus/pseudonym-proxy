# pseudonym-proxy

## Running Server Locally
`flask run --host 0.0.0.0 --port 5001`

Make a request through the proxy:
`python get.py https://www.something.com out.txt`

The proxy URL defaults to http://localhost:5001.
To use a different proxy URL, set the `PROXY_URL` environment variable.
