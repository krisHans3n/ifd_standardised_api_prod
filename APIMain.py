# import flask
from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/imginterface/', methods=['PUT'])
def respond():
    urls = request.args.get('name')
    response = {}

    if urls is None:
        response["Error"] = "no urls were provided"
    elif urls is not None:
        cnt = len(urls)
        report = f"you selected {cnt} images"
        response["REPORT"] = report

    return jsonify(response)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
