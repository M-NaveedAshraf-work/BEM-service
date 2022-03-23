import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import pandas as pd

from flask_cors import CORS
from main import main
from energystar import runEnergystar

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
d = open('./Input/energystar_input.json')
estarData = json.load(d)
build_index = []
weatherData = "centergy_2019_epw_file.epw"
calData = [
    {
        "name": "Heating COP",
        "data": "Float",
        "min": "0.6",
        "max": "1.0",
    }
]
capxData = [
    {
        "name": "Heating COP",
        "data": "Continuous",
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

@app.route('/Calibration', methods=['GET'])
def calibration_model():
    response_object = {'status': 'success'}
    simulated, real, interval = main(mode="calibration", building_name=data, epw_file_name=weatherData, original_file_name="centergy_BEM_2019", result_file_name="iteration1")
    response_object['real'] = real
    response_object['modeled'] = simulated
    response_object['interval'] = interval

    return jsonify(response_object)

@app.route('/Cal', methods = ['GET', 'PUT'])
def calComponents():
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json("calData")
        global calData
        calData = post_data
        response_object['calData'] = calData
        response_object['message'] = "Parameters Updated"
    else:
        response_object['calData'] = calData
    return jsonify(response_object)

@app.route('/Capx', methods = ['GET', 'PUT'])
def capxComponents():
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json("capxData")
        global capxData
        capxData = post_data
        response_object['capxData'] = capxData
        response_object['message'] = "Parameters Updated"
    else:
        response_object['capxData'] = capxData
    return jsonify(response_object)

@app.route('/energystar', methods = ['GET', 'PUT'])
def estarComponents():
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json("estarData")
        global estarData
        global build_index
        estarData = post_data
        build_index = []

        estarData['score']['score'], estarData["score"]["predictEUI"], estarData["score"]["adjustedEUI"], estarData["targetScore"]["usage"], estarData["targetScore"]["targetEUI"], estarData["benchmark"], build_index = runEnergystar(estarData["score"]["grossArea"], estarData["score"]["dataGrossArea"], estarData["score"]["officeGrossArea"], estarData["score"]["weeklyOperation"], estarData["score"]["workers"], estarData["score"]["computers"], estarData["score"]["percentCooled"], estarData["score"]["coolingDays"], estarData["score"]["heatingDays"], estarData["score"]["siteEUI"], estarData["score"]["sourceEUI"], estarData["score"]["siteConsumption"], estarData["score"]["sourceConsumption"], estarData["targetScore"]["target"], estarData["score"]["predictEUI"], estarData["targetScore"]["area"], estarData["targetScore"]["unit"], estarData["targetScore"]["current"], estarData["benchmarkInput"]["minSQFT"], estarData["benchmarkInput"]["maxSQFT"], estarData["benchmarkInput"]["minYear"])

        response_object['estarData'] = estarData
        response_object['build_index'] = build_index

        response_object['message'] = "Parameters Updated"
    else:
        response_object['estarData'] = estarData
        response_object['build_index'] = build_index
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()