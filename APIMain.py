import flask
import sys
import logging
import flask_limiter
import src._Utils.urlValidator as valid
from src._Utils.vectorformatter import VectorLoader
from src.initialise_image_process import MainInterface
from flask import Flask, request, jsonify, session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# session.clear()

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


@app.route('/imginterface/', methods=['POST', 'GET'])
@limiter.limit("40 per minute")
def respond():
    """
    Test curl:
    curl -v -H "Content-Type: application/json" -X POST -d '{"urls": ["https://www.w3schools.com/howto/img_mountains.jpg", "https://www.oxforduniversityimages.com/images/rotate/Image_Spring_17_4.gif"]}' http://127.0.0.1:5000/imginterface/
    TODO:
    -> add configs
    -> chunk each url in to return to browser to split payload
         helps with timeout
    """
    # TODO: Implement graph based authentication system (if Oauth)
    # TODO: Implement rate limiting
    # TODO: Sanitize/validate json package to ensure predefined structure: https://marshmallow.readthedocs.io/en/stable/examples.html 
    urls = request.get_json()
    urls = valid.validate_url_string(urls["urls"])

    response = {}

    if urls is None or len(urls) == 0:
        response["Error"] = "no urls were provided"
    elif urls is not None:
        mi = MainInterface()
        print(id(mi))
        vl = VectorLoader()
        report = mi.main_process(urls)
        report_ = vl.appendB64toJSON(report)
        response["PAYLOAD"] = report_
    return jsonify(response)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
