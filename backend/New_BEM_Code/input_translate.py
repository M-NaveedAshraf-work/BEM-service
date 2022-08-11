import json

def translate(input):

    # Read Data
    a = open('./Input/' + input)
    inputData = json.load(a)

    b = open('./Input/input.json')
    outputData = json.load(b)

    # Lighting
    if inputData['lightInstalled'] == "Flourescent":
        outputData['jsonData']['Lighting'] = 12
        # Add more

    # Occupied and Unoccupied Schedule
    if inputData['occupancySensor'] == True:
        start = inputData['occupiedHourOfBuildingOnWeekday'][0]
        end = inputData['occupiedHourOfBuildingOnWeekday'][1]
        for i in range(1, 25, 1):
            if i >= start and i <= end:
                outputData['jsonData']['Zone1_Schedule']["Hour" + str(i)]["Occupancy_Weekday"] = 1
            else:
                outputData['jsonData']['Zone1_Schedule']["Hour" + str(i)]["Occupancy_Weekday"] = 0.1
        start = inputData['occupiedHourOfBuildingOnWeekend'][0]
        end = inputData['occupiedHourOfBuildingOnWeekend'][1]
        for i in range(1, 25, 1):
            if i >= start and i <= end:
                outputData['jsonData']['Zone1_Schedule']["Hour" + str(i)]["Occupancy_Weekend"] = 1
            else:
                outputData['jsonData']['Zone1_Schedule']["Hour" + str(i)]["Occupancy_Weekend"] = 0.05

    # Setpoint Schedule

    # Heating
    if inputData['setPointTemperatureforheating'] == True:
        start = inputData['setPointTemperatureforheatingonWeekday'][0]
        end = inputData['setPointTemperatureforheatingonWeekday'][1]
        for i in range(1, 25, 1):
            if i >= start and i <= end:
                outputData['jsonData']['TemperatureSetPoint']["Hour" + str(i)]["Heating_Weekday"] = (inputData['occHeatSetPointWeekday'] - 32) * (5/9)
            else:
                outputData['jsonData']['TemperatureSetPoint']["Hour" + str(i)]["Heating_Weekday"] = (inputData['unoccHeatSetPointWeekday'] - 32) * (5/9)
        if inputData['setSetTempWeekendHoursHeat'] == True:
            start = inputData['setPointTemperatureforheatingonWeekend'][0]
            end = inputData['setPointTemperatureforheatingonWeekend'][1]
            for i in range(1, 25, 1):
                if i >= start and i <= end:
                    outputData['jsonData']['TemperatureSetPoint']["Hour" + str(i)]["Heating_Weekend"] = (inputData['occHeatSetPointWeekend'] - 32) * (5/9)
                else:
                    outputData['jsonData']['TemperatureSetPoint']["Hour" + str(i)]["Heating_Weekend"] = (inputData['unoccHeatSetPointWeekend'] - 32) * (5/9)
        else:
            for i in range(1, 25, 1):
                outputData['jsonData']['TemperatureSetPoint']["Hour" + str(i)]["Heating_Weekend"] = 74
    else:
        for i in range(1, 25, 1):
            outputData['jsonData']['TemperatureSetPoint']["Hour" + str(i)]["Heating_Weekday"] = 70
            outputData['jsonData']['TemperatureSetPoint']["Hour" + str(i)]["Heating_Weekend"] = 74

    # Cooling
    if inputData['setPointTemperatureforcooling']:
        start = inputData['setPointTemperatureforcoolingonWeekday'][0]
        end = inputData['setPointTemperatureforcoolingonWeekday'][1]
        for i in range(1, 25, 1):
            if i >= start and i <= end:
                outputData['jsonData']['TemperatureSetPoint']["Hour" + str(i)]["Cooling_Weekday"] = (inputData['occCoolSetPointWeekday'] - 32) * (5/9)
            else:
                outputData['jsonData']['TemperatureSetPoint']["Hour" + str(i)]["Cooling_Weekday"] = (inputData['unoccCoolSetPointWeekday'] - 32) * (5/9)
        if inputData['setSetTempWeekendHoursCool'] == True:
            start = inputData['setPointTemperatureforcoolingonWeekend'][0]
            end = inputData['setPointTemperatureforcoolingonWeekend'][1]
            for i in range(1, 25, 1):
                if i >= start and i <= end:
                    outputData['jsonData']['TemperatureSetPoint']["Hour" + str(i)]["Cooling_Weekend"] = (inputData['occCoolSetPointWeekend'] - 32) * (5/9)
                else:
                    outputData['jsonData']['TemperatureSetPoint']["Hour" + str(i)]["Cooling_Weekend"] = (inputData['unoccCoolSetPointWeekend'] - 32) * (5/9)
        else:
            for i in range(1, 25, 1):
                outputData['jsonData']['TemperatureSetPoint']["Hour" + str(i)]["Cooling_Weekend"] = 74
    else:
        for i in range(1, 25, 1):
            outputData['jsonData']['TemperatureSetPoint']["Hour" + str(i)]["Cooling_Weekday"] = 70
            outputData['jsonData']['TemperatureSetPoint']["Hour" + str(i)]["Cooling_Weekend"] = 74

    # Building Parameters
    outputData['jsonData']['Name'] = inputData['buidlingName']
    outputData['jsonData']['TerrainClass'] = inputData['typeOfterrian']
    outputData['jsonData']['Volume'] = inputData['cubicMetre']
    outputData['jsonData']['Height'] = inputData['height']
    outputData['jsonData']['Zone1']['Occupancy'] = inputData['TotalPeopleInBuildingOnWeekday']
    outputData['jsonData']['Envelope']['Opaque1']['Roof']['Area'] = inputData['areaOfRoof']

    # Heating Cooling System
    if inputData['heatingSystem'] == "I don't know":
        # Placeholder
        outputData['jsonData']['HeatingCOP'] = .9
        outputData['jsonData']['CoolingCOP'] = 2.5
    else:
        outputData['jsonData']['HeatingCOP'] = inputData['heatingSystem']
        outputData['jsonData']['CoolingCOP'] = inputData['coolingSystem']

    # Material (Needs Logic || All Placeholder)
    if type(inputData['materialOfRoof']) == str:
        outputData['jsonData']['Material']['Roof1']['UValue'] = 1 / inputData['R_value_roof']
        outputData['jsonData']['Material']['Roof1']['Absorptivity'] = 0.85
        outputData['jsonData']['Material']['Roof1']['Emissivity'] = 0.8
    if type(inputData['materialOfWall']) == str:
        outputData['jsonData']['Material']['Opaque1']['UValue'] = 1 / inputData['R_value_wall']
        outputData['jsonData']['Material']['Opaque1']['Absorptivity'] = 0.7
        outputData['jsonData']['Material']['Opaque1']['Emissivity'] = 0.92
    if type(inputData['materialOfWindow']) == str:
        outputData['jsonData']['Material']['Window1']['UValue'] = 1 / inputData['R_value_window']
        outputData['jsonData']['Material']['Window1']['SolarTrasmittance'] = 0.41
        outputData['jsonData']['Material']['Window1']['Emissivity'] = -0.04

    # Photovoltaic System
    if inputData['photovoltaicSystem'] == True:
        outputData['jsonData']['PVArea'] = inputData['totalAreaOfPhotovoltaic']
        outputData['jsonData']['PVOrientation'] = inputData['orientationOfPhotovoltaic']
        outputData['jsonData']['PVTiltAngle'] = inputData['angleOfPhotovoltaic']
    else:
        outputData['jsonData']['PVArea'] = 0
        outputData['jsonData']['PVOrientation'] = 0
        outputData['jsonData']['PVTiltAngle'] = 0

    # Solar Water Heater
    if inputData['solarWaterHeatingSys'] == True:
        outputData['jsonData']['SHWArea'] = inputData['totalAreaOfSolarWaterHeatingSys']
        outputData['jsonData']['SHWOrientation'] = inputData['orientationOfSolarWaterHeatingSys']
        outputData['jsonData']['SHWTiltAngle'] = inputData['angleOfSolarWaterHeatingSys']
    else:
        outputData['jsonData']['SHWArea'] = 0
        outputData['jsonData']['SHWOrientation'] = 0
        outputData['jsonData']['SHWTiltAngle'] = 0

    # Wind Turbine System
    if inputData['windTurbineSystem'] == True:
        outputData['jsonData']['WindTurbineDiameter'] = inputData['diameterOfTurbine']
        outputData['jsonData']['WindTurbineEfficiency'] = inputData['effeciencyOfTurbine']
        outputData['jsonData']['HeatingEnergySource'] = inputData['primarySourceOfHeating']
        outputData['jsonData']['CoolingEnergySource'] = inputData['primarySourceOfCooling']
        outputData['jsonData']['DHWEnergySource'] = inputData['primarySourceOfHotWater']
    else:
        outputData['jsonData']['WindTurbineDiameter'] = 0
        outputData['jsonData']['WindTurbineEfficiency'] = 0
        outputData['jsonData']['HeatingEnergySource'] = 0
        outputData['jsonData']['CoolingEnergySource'] = 0
        outputData['jsonData']['DHWEnergySource'] = 0

    # Air Flow + Fans + DHW Need Discussion for Logic (Placeholder)
    outputData['jsonData']['AirLeakageLevel'] = inputData['airLeakageLevel']
    outputData['jsonData']['SpecificFanPower'] = inputData['fanPowerLevel']
    outputData['jsonData']['FanControlFactor'] = inputData['fanFlowControlLevel']
    outputData['jsonData']['PumpHeatingControl'] = inputData['pumpControlForHeating']

    outputData['jsonData']['DHWDistrinutionSystem'] = inputData['distanceOfHotWaterComingfrom']
    outputData['jsonData']['DHWGenerationSystem'] = inputData['typeOfGenerationSys']

    outputData['jsonData']['Garage']['Occupancy'] = inputData['parkingSpaces']

    return outputData

if __name__ == '__main__':
    output = translate("json_input_sheet.json")
    print(output)