import logging
import json
from flask import Flask, make_response, request

_logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/", methods=['POST'])
def hello_world():
    print('RUN')
    data = json.loads(request.data.decode('utf-8'))
    print(data)
    print(data["params"])
    # response = make_response({"results": True}, 200)
    response = make_response({"results": False}, 200)
    # response.mimetype = "text/plain"
    return response

#  flask run --host 0.0.0.0 --port 11000
