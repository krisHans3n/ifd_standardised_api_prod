# import flask
import sys
import logging
from src import initialise_image_process as iip
from flask import Flask, request, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/imginterface/', methods=['POST', 'GET'])
def respond():
    """
    Test curl:
    curl -v -H "Content-Type: application/json" -X POST -d '{"urls": ["https://www.w3schools.com/howto/img_mountains.jpg", "https://www.oxforduniversityimages.com/images/rotate/Image_Spring_17_4.gif"]}' http://127.0.0.1:5000/imginterface/

    TODO:
    -> clean urls / validate
    -> add configs
    -> chunk each url in to return to browser to split payload
         helps with timeout
    """
    # TODO: Sanitize/validate json package to ensure predefined structure: https://marshmallow.readthedocs.io/en/stable/examples.html 
    urls = request.get_json()
    # TODO: validate url strings. Look at: https://www.codespeedy.com/check-if-a-string-is-a-valid-url-or-not-in-python/
    urls = urls["urls"]

    response = {}

    if urls is None or len(urls) == 0:
        response["Error"] = "no urls were provided"
    elif urls is not None:
        report = iip.main_process(urls)
        response["PAYLOAD"] = report

    return jsonify(response)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
