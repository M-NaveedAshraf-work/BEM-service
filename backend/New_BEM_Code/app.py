import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import pandas as pd
import numpy as np
import time

from flask_cors import CORS
from main import main
from energystar import runEnergystar
from processing import processing

import os
from fontTools.misc.py23 import xrange

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
e = open('./Input/hourlyXAxis.json')
hourlyXAxis = json.load(e)
f = open('./Input/centergy_BEM_2019.json')
data = json.load(f)
d = open('./Input/energystar_input.json')
estarData = json.load(d)
h = open('./Input/UQ_Input.json')
UQData = json.load(h)
j = open('./Input/runUQ_input.json')
global runUQData
runUQData = json.load(j)
global build_index
build_index = []
weatherData = "centergy_2019_epw_file.epw"
a = open('./Input/example_calibration.json')
calData = json.load(a)

capxData = [
    {
        "name": "Heating COP",
        "data": "Continuous",
    }
]
HeatData = [
    {
        "param": "HeatingCOP",
        "month": "Jan"
    }
]
global real
real = []
global simulated
simulated = []
global interval
interval = []
global monthly
monthly = []
global subs
subs = []



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

    subDeliveredEnergy = np.zeros((12, 11))
    for i in range(11):
        subDeliveredEnergy[0, i] = np.sum(hourly_delivered_energy[0:744, i])
        subDeliveredEnergy[1, i] = np.sum(hourly_delivered_energy[744:1416, i])
        subDeliveredEnergy[2, i] = np.sum(hourly_delivered_energy[0:744, i])
        subDeliveredEnergy[3, i] = np.sum(hourly_delivered_energy[1416:2159, i])
        subDeliveredEnergy[4, i] = np.sum(hourly_delivered_energy[2159:2880, i])
        subDeliveredEnergy[5, i] = np.sum(hourly_delivered_energy[2880:3624, i])
        subDeliveredEnergy[6, i] = np.sum(hourly_delivered_energy[3624:4344, i])
        subDeliveredEnergy[7, i] = np.sum(hourly_delivered_energy[4344:5088, i])
        subDeliveredEnergy[8, i] = np.sum(hourly_delivered_energy[5088:5832, i])
        subDeliveredEnergy[9, i] = np.sum(hourly_delivered_energy[5832:6552, i])
        subDeliveredEnergy[10, i] = np.sum(hourly_delivered_energy[6552:7296, i])
        subDeliveredEnergy[11, i] = np.sum(hourly_delivered_energy[8016:8760, i])

    subMonthlyTotal = np.zeros((12, 1))
    subMonthlyTotal[0, 0] = np.sum(subDeliveredEnergy[:, 0])
    subMonthlyTotal[1, 0] = np.sum(subDeliveredEnergy[:, 1])
    subMonthlyTotal[2, 0] = np.sum(subDeliveredEnergy[:, 2])
    subMonthlyTotal[3, 0] = np.sum(subDeliveredEnergy[:, 3])
    subMonthlyTotal[4, 0] = np.sum(subDeliveredEnergy[:, 4])
    subMonthlyTotal[5, 0] = np.sum(subDeliveredEnergy[:, 5])
    subMonthlyTotal[6, 0] = np.sum(subDeliveredEnergy[:, 6])
    subMonthlyTotal[7, 0] = np.sum(subDeliveredEnergy[:, 7])
    subMonthlyTotal[8, 0] = np.sum(subDeliveredEnergy[:, 8])
    subMonthlyTotal[9, 0] = np.sum(subDeliveredEnergy[:, 9])
    subMonthlyTotal[10, 0] = np.sum(subDeliveredEnergy[:, 10])
    global monthly
    monthly = grouped.Delivered.tolist()
    global subs
    subs = subMonthlyTotal.tolist()
    response_object['monthly'] = monthly
    response_object['subs'] = subs
    response_object['hourlyXAxis'] = hourlyXAxis

    return jsonify(response_object)

@app.route('/Calibration', methods=['GET'])
def calibration_model():
    response_object = {'status': 'success'}
    data["OutputPeriod"] == "Monthly"
    simulated, real, interval = main(mode="calibration", building_name=data, epw_file_name=weatherData, original_file_name=calData, result_file_name="iteration1")
    response_object['real'] = real
    response_object['modeled'] = simulated
    response_object['interval'] = interval

    return jsonify(response_object)

@app.route('/Cal', methods = ['GET', 'PUT'])
def calComponents():
    response_object = {'status': 'success'}
    data["OutputPeriod"] == "Monthly"
    if request.method == 'PUT':
        post_data = request.get_json("calData")
        print(post_data)
        global calData
        calData = post_data
        response_object['calData'] = calData
        response_object['message'] = "Parameters Updated"
    else:
        response_object['calData'] = calData
    return jsonify(response_object)

@app.route('/UQ', methods = ['GET', 'PUT'])
def UQComponents():
    response_object = {'status': 'success'}
    data["OutputPeriod"] == "Monthly"
    if request.method == 'PUT':
        post_data = request.get_json("UQData")
        global UQData
        UQData = post_data
        response_object['UQData'] = UQData
        response_object['message'] = "Parameters Updated"
    else:
        print(UQData)
        response_object['UQData'] = UQData

    return jsonify(response_object)

@app.route('/runUQ', methods = ['GET'])
def UQRuns():
    response_object = {'status': 'success'}
    time.sleep(3)
    data["OutputPeriod"] == "Monthly"
    global runUQData
    response_object = runUQData
    firstGraphNames, firstGraphData, secondGraphNames, secondGraphData = main(mode="UQ", building_name=data,
                                                                              epw_file_name=weatherData,
                                                                              original_file_name=UQData,
                                                                              result_file_name="iteration1")
    if UQData['UQInputs']['UQMode'] == "Sensitivity Analysis":
        response_object['firstGraphNamesSA'] = firstGraphNames.tolist()
        response_object['firstGraphDataSA'] = firstGraphData.tolist()
        response_object['secondGraphNamesSA'] = secondGraphNames.tolist()
        response_object['secondGraphDataSA'] = secondGraphData
    elif UQData['UQInputs']['UQMode'] == "Uncertainty Analysis":
        response_object['firstGraphNamesUA'] = firstGraphNames
        response_object['firstGraphDataUA'] = firstGraphData
        response_object['secondGraphNamesUA'] = secondGraphNames
        response_object['secondGraphDataUA'] = secondGraphData.tolist()

    runUQData = response_object

    return jsonify(response_object)

@app.route('/Capx', methods = ['GET', 'PUT'])
def capxComponents():
    response_object = {'status': 'success'}
    data["OutputPeriod"] == "Monthly"
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
    data["OutputPeriod"] == "Monthly"
    if request.method == 'PUT':
        post_data = request.get_json("estarData")
        global estarData
        global build_index
        estarData = post_data
        build_index = []

        estarData['score']['score'], estarData["score"]["predictEUI"], estarData["score"]["adjustedEUI"], estarData["targetScore"]["usage"], estarData["targetScore"]["targetEUI"], estarData["benchmark"], build_index = runEnergystar(estarData["score"]["grossArea"], estarData["score"]["dataGrossArea"], estarData["score"]["officeGrossArea"], estarData["score"]["weeklyOperation"], estarData["score"]["workers"], estarData["score"]["computers"], estarData["score"]["percentCooled"], estarData["score"]["coolingDays"], estarData["score"]["heatingDays"], estarData["score"]["siteEUI"], estarData["score"]["sourceEUI"], estarData["score"]["siteConsumption"], estarData["score"]["sourceConsumption"], estarData["targetScore"]["target"], estarData["score"]["predictEUI"], estarData["targetScore"]["area"], estarData["targetScore"]["unit"], estarData["targetScore"]["current"], estarData["benchmarkInput"]["minSQFT"], estarData["benchmarkInput"]["maxSQFT"], estarData["benchmarkInput"]["minYear"])
        # eui, end_use, consumption, benchmark = processing(data, 'park_center_2019_epw_file.epw', estarData["benchmarkInput"]["minSQFT"], estarData["benchmarkInput"]["maxSQFT"], estarData["benchmarkInput"]["minYear"] )
        # print(eui, end_use, consumption, benchmark)
        response_object['estarData'] = estarData
        response_object['build_index'] = build_index

        response_object['message'] = "Parameters Updated"
    else:
        response_object['estarData'] = estarData
        response_object['build_index'] = build_index
    return jsonify(response_object)

@app.route('/graph', methods = ['GET', 'PUT'])
def graphComponents():
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        response_object['UQData'] = UQData
        response_object['estarData'] = estarData
        response_object['build_index'] = build_index
        response_object['capxData'] = capxData
        response_object['calData'] = calData
        response_object['real'] = real
        response_object['modeled'] = simulated
        response_object['interval'] = interval
        response_object['runUQData'] = runUQData
        response_object['monthly'] = monthly
        response_object['subs'] = subs
    else:
        response_object['UQData'] = UQData
        response_object['estarData'] = estarData
        response_object['build_index'] = build_index
        response_object['capxData'] = capxData
        response_object['calData'] = calData
        response_object['real'] = real
        response_object['modeled'] = simulated
        response_object['interval'] = interval
        response_object['runUQData'] = runUQData
        response_object['monthly'] = monthly
        response_object['subs'] = subs
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()