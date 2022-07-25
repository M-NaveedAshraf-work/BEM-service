import uuid

from flask import Flask, jsonify, request
import json
import pandas as pd
import numpy as np
import time
import openpyxl

from flask_cors import CORS
from main import main
from energystar import runEnergystar
from datetime import datetime
from multi_year_parser import combine
from auto_calibration import auto_calibrate
from zero_order_model import predict

import os
from fontTools.misc.py23 import xrange

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
load = 1
predictedCost = 0
global historicalData
global today
today = str(datetime.now())
historicalData1 = "BEM_Optimization_Input_v2_centergy_BEM_2019.xlsx"
historicalData2 = "BEM_Optimization_Input_v2_centergy_BEM_2019.xlsx"
historicalData, m_index, d_index, h_index = combine(historicalData1, historicalData2)
a = open('./Input/comboFiles.json')
fileData = json.load(a)
b = open('./Input/input.json')
inputData = json.load(b)
e = open('./Input/hourlyXAxis.json')
global hourlyXAxis
hourlyXAxis = json.load(e)
global monthlyXAxis
monthlyXAxis = hourlyXAxis
f = open('./Input/centergy_BEM_2019.json')
data = json.load(f)
d = open('./Input/energystar_input.json')
estarData = json.load(d)
h = open('./Input/UQ_Input.json')
UQData = json.load(h)
j = open('./Input/runUQ_input.json')
global runUQData
runUQData = json.load(j)
k = open('./Input/runZero.json')
global runZeroData
runZeroData = json.load(k)
global build_index
build_index = []
weatherData = "centergy_2019_epw_file.epw"
a = open('./Input/example_calibration.json')
calData = json.load(a)
outputPeriod = [
    {
        "OutputPeriod": "Monthly"
    }
],

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

        global data
        global weatherData
        global historicalData
        global historicalData1
        global historicalData2
        global inputData

        postData = request.get_json('inputData')
        post_json = postData["jsonData"]
        post_weather = postData["weatherData"]
        post_historical1 = postData["historicalData1"]
        post_historical2 = postData["historicalData2"]

        data = post_json

        weatherData = post_weather
        historicalData1 = post_historical1
        historicalData2 = post_historical2

        inputData['jsonData'] = data
        inputData['weatherData'] = weatherData
        inputData['historicalData1'] = historicalData1
        inputData['historicalData2'] = historicalData2

        print(historicalData1)
        print(historicalData2)

        historicalData, m_index, d_index, h_index = combine(historicalData1, historicalData2)

        response_object['inputData'] = inputData
    else:
        historicalData, m_index, d_index, h_index = combine(historicalData1, historicalData2)

        inputData['jsonData'] = data
        inputData['weatherData'] = weatherData
        inputData['historicalData1'] = historicalData1
        inputData['historicalData2'] = historicalData2

        print(historicalData1)
        print(historicalData2)

        response_object['inputData'] = inputData
    return jsonify(response_object)


@app.route('/BEM', methods=['GET'])
def bem_model():
    response_object = {'status': 'success'}
    hourly_delivered_energy, sum_delivered_energy, energy_use_by_fuel= main(mode="simulation", building_name=data, epw_file_name=weatherData,
        original_file_name="centergy_BEM_2019", result_file_name="iteration1")

    historicalData, m_index, d_index, h_index = combine(historicalData1, historicalData2)

    out = np.asarray(hourly_delivered_energy[:, -1]) * data['Zone1']['GrossFloorArea'] / 1000

    if data['OutputPeriod'] == "Monthly":
        plot_data = pd.DataFrame(out, columns=['Delivered'])
        plot_data['Month'] = 'blank'
        plot_data.loc[:743, 'Month'] = 'January'
        plot_data.loc[744:1415, 'Month'] = 'February'
        plot_data.loc[1416:2159, 'Month'] = 'March'
        plot_data.loc[2160:2879, 'Month'] = 'April'
        plot_data.loc[2880:3623, 'Month'] = 'May'
        plot_data.loc[3624:4343, 'Month'] = 'June'
        plot_data.loc[4344:5087, 'Month'] = 'July'
        plot_data.loc[5088:5831, 'Month'] = 'August'
        plot_data.loc[5832:6551, 'Month'] = 'Septemeber'
        plot_data.loc[6552:7295, 'Month'] = 'October'
        plot_data.loc[7296:8015, 'Month'] = 'November'
        plot_data.loc[8016:8759, 'Month'] = 'December'
        grouped = (plot_data.groupby(['Month'], sort=False).sum()).reset_index()

        ofile = grouped.iloc[m_index:]
        nfile = grouped.iloc[:m_index]
        grouped = pd.concat([ofile, nfile])

    elif data['OutputPeriod'] == "Hourly":
        grouped = pd.DataFrame(out, columns=['Delivered'])
        ofile = grouped.iloc[h_index:]
        nfile = grouped.iloc[:h_index]
        grouped = pd.concat([ofile, nfile])

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
    global hourlyXAxis
    global monthlyXAxis
    global load
    if load == 1:
        hourlyXAxis = pd.DataFrame(hourlyXAxis['hourlyXAxis'], columns=['data'])
        ofile = hourlyXAxis.iloc[h_index:]
        nfile = hourlyXAxis.iloc[:h_index]
        hourlyXAxis = pd.concat([ofile, nfile])

        monthlyXAxis = pd.DataFrame(monthlyXAxis['monthlyXAxis'], columns=['month'])
        ofile2 = monthlyXAxis.iloc[m_index:]
        nfile2 = monthlyXAxis.iloc[:m_index]
        monthlyXAxis = pd.concat([ofile2, nfile2])
        load += 1

    subs = subMonthlyTotal.tolist()
    response_object['monthly'] = monthly
    response_object['subs'] = subs
    # response_object['hourlyXAxis'] = hourlyXAxis
    response_object['hourlyXAxis'] = hourlyXAxis['data'].values.tolist()
    response_object['monthlyXAxis'] = monthlyXAxis['month'].values.tolist()

    return jsonify(response_object)

@app.route('/Calibration', methods=['GET'])
def calibration_model():
    response_object = {'status': 'success'}
    # data["OutputPeriod"] == "Monthly"
    calData["type"] = "Calibration"
    historicalData, m_index, d_index, h_index = combine(historicalData1, historicalData2)
    simulated, real, interval, cvRMSE = main(mode="calibration", building_name=data, epw_file_name=weatherData, original_file_name=calData, result_file_name=historicalData)

    if interval == "Monthly":
        ofile = simulated.iloc[m_index:]
        nfile = simulated.iloc[:m_index]
        simulated = pd.concat([ofile, nfile])

        ofile = real.iloc[m_index:]
        nfile = real.iloc[:m_index]
        real = pd.concat([ofile, nfile])

    elif interval == "Daily":
        ofile = simulated.iloc[d_index:]
        nfile = simulated.iloc[:d_index]
        simulated = pd.concat([ofile, nfile])

        ofile = real.iloc[d_index:]
        nfile = real.iloc[:d_index]
        real = pd.concat([ofile, nfile])

    elif interval == "Hourly":
        ofile = simulated.iloc[h_index:]
        nfile = simulated.iloc[:h_index]
        simulated = pd.concat([ofile, nfile])

        ofile = real.iloc[h_index:]
        nfile = real.iloc[:h_index]
        real = pd.concat([ofile, nfile])

    # real.to_numpy()
    # simulated.to_numpy()
    print(real)
    print(simulated)
    print(hourlyXAxis)

    response_object['real'] = real['data'].values.tolist()
    response_object['modeled'] = simulated['data'].values.tolist()
    response_object['hourlyXAxis'] = hourlyXAxis['data'].values.tolist()
    response_object['monthlyXAxis'] = monthlyXAxis['month'].values.tolist()
    response_object['interval'] = interval

    return jsonify(response_object)

@app.route('/auto_calibration', methods=['GET'])
def auto_calibration_model():
    response_object = {'status': 'success'}
    # data["OutputPeriod"] == "Monthly"
    calData["type"] = "Calibration"
    historicalData, m_index, d_index, h_index = combine(historicalData1, historicalData2)
    simulated, real, interval = auto_calibrate(data, calData, historicalData, weatherData)

    if interval == "Monthly":
        ofile = simulated.iloc[m_index:]
        nfile = simulated.iloc[:m_index]
        simulated = pd.concat([ofile, nfile])

        ofile = real.iloc[m_index:]
        nfile = real.iloc[:m_index]
        real = pd.concat([ofile, nfile])

    elif interval == "Daily":
        ofile = simulated.iloc[d_index:]
        nfile = simulated.iloc[:d_index]
        simulated = pd.concat([ofile, nfile])

        ofile = real.iloc[d_index:]
        nfile = real.iloc[:d_index]
        real = pd.concat([ofile, nfile])

    elif interval == "Hourly":
        ofile = simulated.iloc[h_index:]
        nfile = simulated.iloc[:h_index]
        simulated = pd.concat([ofile, nfile])

        ofile = real.iloc[h_index:]
        nfile = real.iloc[:h_index]
        real = pd.concat([ofile, nfile])

    # real.to_numpy()
    # simulated.to_numpy()
    print(real)
    print(simulated)
    print(hourlyXAxis)

    response_object['real'] = real['data'].values.tolist()
    response_object['modeled'] = simulated['data'].values.tolist()
    response_object['hourlyXAxis'] = hourlyXAxis['data'].values.tolist()
    response_object['monthlyXAxis'] = monthlyXAxis['month'].values.tolist()
    response_object['interval'] = interval

    return jsonify(response_object)

@app.route('/Cal', methods = ['GET', 'PUT'])
def calComponents():
    response_object = {'status': 'success'}
    # data["OutputPeriod"] == "Monthly"
    if request.method == 'PUT':
        post_data = request.get_json("calData")
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

@app.route('/Capx', methods = ['GET'])
def capxComponents():
    response_object = {'status': 'success'}
    calData["type"] = "CapX"
    # data["OutputPeriod"] == "Monthly"
    historicalData, m_index, d_index, h_index = combine(historicalData1, historicalData2)
    simulated, real, interval = main(mode="capX", building_name=data, epw_file_name=weatherData,
                                     original_file_name=calData, result_file_name=historicalData)

    if interval == "Monthly":
        ofile = simulated.iloc[m_index:]
        nfile = simulated.iloc[:m_index]
        simulated = pd.concat([ofile, nfile])

        ofile = real.iloc[m_index:]
        nfile = real.iloc[:m_index]
        real = pd.concat([ofile, nfile])
    elif interval == "Daily":
        ofile = simulated.iloc[d_index:]
        nfile = simulated.iloc[:d_index]
        simulated = pd.concat([ofile, nfile])

        ofile = real.iloc[d_index:]
        nfile = real.iloc[:d_index]
        real = pd.concat([ofile, nfile])
    elif interval == "Hourly":
        ofile = simulated.iloc[h_index:]
        nfile = simulated.iloc[:h_index]
        simulated = pd.concat([ofile, nfile])

        ofile = real.iloc[h_index:]
        nfile = real.iloc[:h_index]
        real = pd.concat([ofile, nfile])

    # real.to_numpy()
    # simulated.to_numpy()
    print(real)
    print(simulated)

    response_object['real'] = real['data'].values.tolist()
    response_object['modeled'] = simulated['data'].values.tolist()
    response_object['hourlyXAxis'] = hourlyXAxis['data'].values.tolist()
    response_object['monthlyXAxis'] = monthlyXAxis['month'].values.tolist()
    response_object['interval'] = interval

    return jsonify(response_object)

@app.route('/energystar', methods = ['GET', 'PUT'])
def estarComponents():
    response_object = {'status': 'success'}
    # data["OutputPeriod"] == "Monthly"
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
        response_object['inputData'] = inputData
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
        response_object['inputData'] = inputData
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

@app.route('/loadProject', methods=['GET', 'PUT'])
def loadProject_model():
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json('files')

        global inputData
        global UQData
        global calData
        global estarData

        inputData = post_data['inputFile']
        UQData = post_data['UQFile']
        calData = post_data['calFile']
        estarData = post_data['estarFile']

        response_object['inputData'] = inputData
        response_object['UQData'] = UQData
        response_object['calData'] = calData
        response_object['estarData'] = estarData
    else:
        response_object['inputData'] = inputData
        response_object['UQData'] = UQData
        response_object['calData'] = calData
        response_object['estarData'] = estarData
    return jsonify(response_object)

@app.route('/runZero', methods = ['GET', 'PUT'])
def Zero():
    if request.method == 'PUT':
        print("Zero Order Model Run")
        global runZeroData
        filename = request.get_json("chosenZeroModel")
        runZeroData["chosenZeroModel"] = filename["chosenZeroModel"]
        runZeroData['estimatedCost'], runZeroData['error'] = predict(runZeroData["chosenZeroModel"])
        print(runZeroData)
    else:
        print("Get Zero Data")
        runZeroData = runZeroData
    return jsonify(runZeroData)

# @app.route('/runZero', methods = ['GET'])
# def UQRuns():
#     global runZeroData
#
#     runZeroData['Cost'], runZeroData['Error'] = predict(zeroFilename)
#
#     return jsonify(runZeroData)


if __name__ == '__main__':
    app.run()