from main import main
from multi_year_parser import combine
import json
import pandas as pd

def auto_calibrate(data, calData, historicalData, weatherData):

    # Read in the Auto Calibration Input File
    UQData = json.load(open('./Input/Auto_UQ_Input.json'))

    # Run SA to get 5 top results
    firstGraphNames, firstGraphData, secondGraphNames, secondGraphData = main(mode="UQ", building_name=data,
                                                                              epw_file_name=weatherData,
                                                                              original_file_name=UQData,
                                                                              result_file_name="iteration1")

    # Combine top calibration parameters with standard parameters
    factors = firstGraphNames.tolist()

    topFactors = []
    constParams = [{"Factor": "HeatingCOP"}, {"Factor": "CoolingCOP"}, {"Factor": "Occupancy"}, {"Factor": "Appliance"}, {"Factor": "Lighting"}, {"Factor": "Opaque UValue"},
                   {"Factor": "Window UValue"}]
    for i in range(len(factors)-1, len(factors)-7, -1):
        topFactors.append({'Factor': factors[i]})
    for param in constParams:
        topFactors.append(param)

    # Translate between UQ and Calibration Parameter Names while assigning data type and min + max values
    UQ2Cal = {'UQ': ["HeatingCOP", "CoolingCOP", "AirLeakageLevel", "SpecificFanPower", "FanControlFactor", "Occupancy",
                    "Appliance", "Lighting", "OutdoorAir", "Roof UValue", "Roof Absorption Coefficient", "Roof Emissivity",
                    "Opaque UValue", "Opaque Absorption Coefficient", "Opaque Emissivity", "Window UValue", "Window Emissivity",
                     "Window SolarTrasmittance", "Retail Refri Capacity", "EV Charger Power", "Garage Appliance",
                    "Garage Lighting", "Lighting Dimmer Weekday", "Lighting Dimmer Weekend"],
              "Cal": ['Heating COP', 'Cooling COP', 'Building air leakage level', 'Specific Fan Power', 'Fan Control Factor', 'Occupancy',
                    'Appliance', 'Lighting', 'Outdoor Air', 'Roof1 Uvalue', 'Roof1 Absorption coefficient', 'Roof1 Emissivity',
                    'Opaque1 Uvalue', 'Opaque1 Absorption coefficient', 'Opaque1 Emissivity', 'Window1 Uvalue', 'Window1 Emissivity',
                    'Window1 Solar transmittance', 'Retail Refri Capacity', 'EV Charger Power', 'Garage Appliance', 'Garage Lighting',
                    'Lighting Dimmer Weekday', 'Lighting Dimmer Weekend'],
              "Data": ["Float", "Float", "Float", "Float", "Float", "Float", "Float", "Float", "Float", "Float", "Float", "Float",
                       "Float", "Float", "Float", "Float", "Float", "Float", "Float", "Float", "Float", "Float", "Float", "Float"],
              "Tolerance": [0.1, 1.5, 1.0, 1.0, 0.5, 5, 3.0, 3.0, 0.3, 0.05, 0.05, 0.03, 0.05, 0.05, 0.03, 0.05, 0.05, 0.03, .01, 1.0, 1.0, 1.0, 1, 1]}

    # Read initial values from input sheet in order to set baseline for min and max values
    inputValues = {
        "HeatingCOP": data["HeatingCOP"],
        "CoolingCOP": data["CoolingCOP"],
        "AirLeakageLevel": data["AirLeakageLevel"],
        "SpecificFanPower": data["SpecificFanPower"],
        "FanControlFactor": data["FanControlFactor"],
        "Occupancy": data['Zone1']["Occupancy"],
        "Appliance": data['Zone1']["Appliance"],
        "Lighting": data['Zone1']["Lighting"],
        "OutdoorAir": data['Zone1']["OutdoorAir"],
        "Roof UValue": data["Material"]["Roof1"]["UValue"],
        "Roof Absorption Coefficient": data["Material"]["Roof1"]["Absorptivity"],
        "Roof Emissivity": data["Material"]["Roof1"]["Emissivity"],
        "Opaque UValue": data["Material"]["Opaque1"]["UValue"],
        "Opaque Absorption Coefficient": data["Material"]["Opaque1"]["Absorptivity"],
        "Opaque Emissivity": data["Material"]["Opaque1"]["Emissivity"],
        "Window UValue": data["Material"]["Window1"]["UValue"],
        "Window Emissivity": data["Material"]["Window1"]["Emissivity"],
        "Window SolarTrasmittance": data["Material"]["Window1"]["SolarTrasmittance"],
        "Retail Refri Capacity": data["RetailRefrig"]["Capacity"],
        "EV Charger Power": data["ElectricVehicle"]["ChargingPower"],
        "Garage Appliance": data["Garage"]["Appliance"],
        "Garage Lighting": data["Garage"]["Lighting"],
        "Lighting Dimmer Weekday": data["LightingDimmer"]["DimmerSaving_WD"],
        "Lighting Dimmer Weekend": data["LightingDimmer"]["DimmerSaving_WE"]
    }

    # Format Parameters to be fed into Calibration function
    topFactors = pd.DataFrame(topFactors)
    UQ2Cal = pd.DataFrame(UQ2Cal)
    calInputForm = {"data": "", "max": "", "min": "", "name": ""}
    calInput = []

    for factor in topFactors['Factor']:
        for i in range(0, len(UQ2Cal['UQ']), 1):
            if factor == UQ2Cal['UQ'][i]:
                calInputForm["data"] = UQ2Cal["Data"][i]
                calInputForm["name"] = UQ2Cal["Cal"][i]
                if factor == "HeatingCOP":
                    calInputForm["min"] = data['HeatingCOP'] - UQ2Cal["Tolerance"][i]
                    calInputForm["max"] = data['HeatingCOP'] + UQ2Cal["Tolerance"][i]
                    if UQ2Cal["Tolerance"][i] < 1 and calInputForm["max"] >= 1:
                        calInputForm["max"] = 0.99
                else:
                    calInputForm["min"] = inputValues[UQ2Cal['UQ'][i]] - UQ2Cal["Tolerance"][i]
                    calInputForm["max"] = inputValues[UQ2Cal['UQ'][i]] + UQ2Cal["Tolerance"][i]
                if calInputForm["data"] == "integer":
                    calInputForm["min"] = int(calInputForm["min"])
                    calInputForm["max"] = int(calInputForm["max"])
                calInput.append(calInputForm.copy())
                break

    # Create 5 Calibration GA settings
    # gaSettings = {"crossover_rate": [0.9, 0.8, 0.7, 0.85, 0.95],
    #               "max_time": [30, 30, 30, 30, 30],
    #               "mutation_rate": [0.2, 0.3, 0.4, 0.4, 0.4],
    #               "population_size": [100, 100, 100, 100, 100],
    #               "random_seed": ["None", "None", "None", "None", "None"],
    #               "top_percentage": [10, 15, 20, 15, 10]
    #               }

    gaSettings = {"crossover_rate": [0.9, 0.8, 0.7, 0.85, 0.95],
                  "max_time": [1, 1, 1, 1, 1],
                  "mutation_rate": [0.2, 0.3, 0.4, 0.4, 0.4],
                  "population_size": [100, 100, 100, 100, 100],
                  "random_seed": ["None", "None", "None", "None", "None"],
                  "top_percentage": [10, 15, 20, 15, 10]
                  }

    gaSettingForm = {"crossover_rate": "", "max_time": "", "mutation_rate": "", "population_size": "", "random_seed": "", "top_percentage": ""}
    resultForm = {"simulated": "", "real": "", "interval": "", "cvRMSE": "", "ROI": "", "Payback": ""}
    results = []
    for k in range(0, 5, 1):
        gaSettingForm["crossover_rate"] = gaSettings["crossover_rate"][k]
        gaSettingForm["max_time"] = gaSettings["max_time"][k]
        gaSettingForm["mutation_rate"] = gaSettings["mutation_rate"][k]
        gaSettingForm["population_size"] = gaSettings["population_size"][k]
        gaSettingForm["random_seed"] = gaSettings["random_seed"][k]
        gaSettingForm["top_percentage"] = gaSettings["top_percentage"][k]

        calData['ga_settings'] = gaSettingForm
        calData['calibration_parameters'] = calInput

        simulated, real, interval, cvRMSE, ROI, Payback = main(mode="auto calibration", building_name=data, epw_file_name=weatherData, original_file_name=calData,
             result_file_name=historicalData)

        resultForm['simulated'] = simulated
        resultForm['real'] = real
        resultForm['interval'] = interval
        resultForm['cvRMSE'] = cvRMSE
        resultForm['ROI'] = ROI
        resultForm['Payback'] = Payback

        results.append(resultForm.copy())

    bestIndex = 0
    for j in range(1, 5, 1):
        if results[j]['cvRMSE'] < results[bestIndex]['cvRMSE']:
            bestIndex = j

    return results[bestIndex]['simulated'], results[bestIndex]['real'], results[bestIndex]['interval'], results[bestIndex]['cvRMSE'], results[bestIndex]['ROI'], results[bestIndex]['Payback']




if __name__ == '__main__':

    data = json.load(open('./Input/centergy_BEM_2019.json'))
    calData = json.load(open('./Input/example_calibration.json'))
    historicalData1 = "BEM_Optimization_Input_v2_centergy_BEM_2019.xlsx"
    historicalData2 = "BEM_Optimization_Input_v2_centergy_BEM_2019.xlsx"
    historicalData, m_index, d_index, h_index = combine(historicalData1, historicalData2)

    simulated, real, interval = auto_calibrate(data, calData, historicalData, "centergy_2019_epw_file.epw")
    print("")
    print("----------------------------------------------------------------")
    print("")
    print(simulated, real, interval)