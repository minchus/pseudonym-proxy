from flask import Flask
from flask import Response
from flask import stream_with_context
from itertools import chain
import requests

app = Flask(__name__)


@app.route('/healthcheck')
def healthcheck():
    return 'ok'


@app.route('/<path:url>')
def home(url):
    req = requests.get(url, stream=True)
    # print(req.headers)

    generator = chain([b"\xff\xfe"], req.iter_content(chunk_size=1024))
    response = Response(stream_with_context(generator), content_type='text/html')
    response.headers["Content-Disposition"] = "attachment; filename=download.txt"
    return response


if __name__ == '__main__':
    app.run()
