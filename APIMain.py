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
from functools import wraps

logging.basicConfig(level=logging.DEBUG)

def required_params(required):
    
    def decorator(fn):
        
        @wraps(fn)
        def wrapper(*args, **kwargs):
            _json = request.get_json()
            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',request.get_json())
            missing = [r for r in required.keys()
                       if r not in _json]
            print(missing, _json)
            if missing:
                response = {
                    "status": "error",
                    "message": "Request JSON is missing some required params",
                    "missing": missing
                }
                return jsonify(response), 400
            wrong_types = [r for r in required.keys()
                           if not isinstance(_json[r], required[r])]
            if wrong_types:
                response = {
                    "status": "error",
                    "message": "Data types in the request JSON do not match the required format",
                    "param_types": {k: str(v) for k, v in required.items()}
                }
                return jsonify(response), 400
            return fn(*args, **kwargs)

        return wrapper

    return decorator


def create_app():

    app = Flask(__name__)
    
#     # Future initialisation
#     app.config.from_object('config')
#     api.init_app(app)
#     # initialize SQLAlchemy
#     db.init_app(app)
    
    limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["720 per day", "30 per hour"]
    )
    
    # TODO: Restrict incoming client to only the port:5000 -> ml_img_det_intrfc
    # TODO: Block rate limits
    @app.route('/imginterface/', methods=['POST', 'GET'])
    @required_params({"urls": list})
    # @limiter.limit("40 per minute")
    def respond():
        """
        Test curl:
        curl -v -H "Content-Type: application/json" -X POST -d '{"urls": ["https://www.w3schools.com/howto/img_mountains.jpg", "https://www.oxforduniversityimages.com/images/rotate/Image_Spring_17_4.gif"]}' http://127.0.0.1:5000/imginterface/
        TODO:
        -> add configs
        -> chunk each url in to return to browser to split payload
        helps with timeout
        -> from functools import wraps
        """
        urls = request.get_json()
        urls = valid.validate_url_string(urls["urls"])

        response = {}

        if urls is None or len(urls) == 0:
            response["Error"] = "no urls were provided"
        elif urls is not None:
            mi = MainInterface()
            vl = VectorLoader()
            report = mi.main_process(urls)
            _report = vl.appendB64toJSON(report)
            response["PAYLOAD"] = _report
        print(response)
        return jsonify(response)
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(threaded=True, port=5001, debug=True)
