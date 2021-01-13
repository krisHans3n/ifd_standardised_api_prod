# import flask
import sys
import logging
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/imginterface/', methods=['POST', 'GET'])
def respond():
    """
    Test curl:
    curl -v -H "Content-Type: application/json" -X POST -d '{"urls": ["ver", "sdf", "df"]}' http://127.0.0.1:5000/imginterface/
    """
    urls = request.get_json()
    urls = urls["urls"]

    response = {}

    if urls is None:
        response["Error"] = "no urls were provided"
    elif urls is not None:
        cnt = len(urls)
        report = f"you selected {cnt} {urls} images"
        response["REPORT"] = report

    return jsonify(response)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
