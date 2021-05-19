from flask import Flask, jsonify, request, Response
from simple_load import simple_load

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    body, mime = simple_load(request.path)
    headers = {}

    # TODO: Put everything but the html on a fake CDN service
    if not mime == 'text/html':
        headers["Cache-Control"] = "max-age=86400" # a day

    if body:
        if mime:
            headers["Content-Type"] = mime
        return body, 200, headers
    else:
        return "Not found", 404

if __name__ == '__main__':
    app.run(host="localhost", port=3002)