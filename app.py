"""
Run web app
"""

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask('__main__')
CORS(app, resources={r'/*': {'origins': '*'}})


def init() -> None:
    app.run()


@app.route('/', methods=["POST"])
def testing():
    input_json = request.get_json(force=True)
    dictToReturn = {'text': input_json['text']}
    return jsonify(dictToReturn)
