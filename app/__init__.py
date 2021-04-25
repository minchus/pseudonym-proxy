from flask import Flask
from flask import Response
from flask import stream_with_context
import requests

app = Flask(__name__)


@app.route('/<path:url>')
def home(url):
    req = requests.get(url, stream=True)
    print(req.headers)
    content_disposition = req.headers.get('Content-Disposition')
    if content_disposition and "attachment" in content_disposition:
        response = Response(stream_with_context(req.iter_content(chunk_size=1024)),
                            content_type=req.headers['content-type'])
        response.headers["Content-Disposition"] = "attachment; filename=download.txt"
        return response
    else:
        return "Only downloads are proxied"


if __name__ == '__main__':
    app.run()
