import os
from typing import Union

from flask import Flask, request, jsonify, Response
from marshmallow import ValidationError

from builder import build_query
from models import RequestSchema

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=["POST"])
def perform_query() -> Union[Response, tuple[Response, int]]:

    data = request.json
    try:
        RequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    file_path = os.path.join(DATA_DIR, data['file_name'])
    if not os.path.exists(file_path):
        return jsonify(f"{data['file_name']} was not found"), 400

    first_result = build_query(cmd=data['cmd1'], value=data['value1'], file_name=file_path, data=None)
    second_result = build_query(cmd=data['cmd2'], value=data['value2'], file_name=file_path, data=first_result)
    return jsonify(second_result)
