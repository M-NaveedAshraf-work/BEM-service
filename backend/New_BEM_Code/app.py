import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import pandas as pd

from flask_cors import CORS
from main import main
from BEMP import Hourly_BEM_JSON

import os
from fontTools.misc.py23 import xrange

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

f = open('./Input/centergy_BEM_2019.json')
data = json.load(f)
weatherData = "centergy_2019_epw_file.epw"
calData = [
    {
        "name": "Heating COP",
        "data": "Float",
        "min": "0.6",
        "max": "1.0",
    }
]


# Hosting the JSON File that can be Read by Scripts and Edited by Vue frontend
@app.route('/input', methods=['GET', 'PUT'])
def json_data():
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json("jsonData")
        global data
        global weatherData
        data = post_data
        response_object['jsonData'] = data
        response_object['weatherData'] = weatherData
    else:
        response_object['jsonData'] = data
        response_object['weatherData'] = weatherData
    return jsonify(response_object)


@app.route('/BEM', methods=['GET'])
def bem_model():
    response_object = {'status': 'success'}
    hourly_delivered_energy, sum_delivered_energy, energy_use_by_fuel, grouped = main(mode="simulation", building_name=data, epw_file_name=weatherData,
        original_file_name="centergy_BEM_2019", result_file_name="iteration1")

    response_object['monthly'] = grouped.Delivered.tolist()

    return jsonify(response_object)

@app.route('/Cal', methods = ['GET', 'PUT'])
def calComponents():
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json("calData")
        global calData
        calData = post_data
        response_object['calData'] = data
        response_object['message'] = "Parameters Updated"
    else:
        response_object['calData'] = calData
    return jsonify(response_object)

# @app.route('/Cal/<cal_id>', methods=['PUT'])
# def single_cal(cal_id):
#     response_object = {'status': 'success'}
#     if request.method == 'PUT':
#         post_data = request.get_json()
#         remove_param(cal_id)
#         calData.append({
#             'id': uuid.uuid4().hex,
#             "name": post_data.get('name'),
#             "data": post_data.get('data'),
#             "min": post_data.get('min'),
#             "max": post_data.get('max'),
#         })
#         response_object['message'] = 'Cal updated!'
#     return jsonify(response_object)
#
# def remove_param(cal_id):
#     for cal in calData:
#         if cal['id'] == cal_id:
#             calData.remove(cal)
#             return True
#         return False

if __name__ == '__main__':
    app.run()