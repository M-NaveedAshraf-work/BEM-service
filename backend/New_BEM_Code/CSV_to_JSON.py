import csv
import json

def Mal_Input_Identifier(input_value):
    changed_value=0
    if input_value.strip() in ['', '-']:
        changed_value = '0'
    else:
        try: # replace a number with comman (e.g., '123,4.32')
            float(input_value)
            changed_value = input_value
        except ValueError:
            changed_value = str(float(input_value.replace(',', '')))

    return changed_value

def json_Insance_Generation(building_name):

    # 1. Read BEMP input CSV
    with open(building_name, encoding='utf-8-sig') as csv_file:
        csv_reader  = csv.reader(csv_file, delimiter=',')
        inputs = [row for row in csv.reader(csv_file)]

    # Change the wrong inputs
    # order: zone -> each zone schedule -> envelop -> material -> natural ventilation -> electric battery -> lighting dimmer -> electric vehicle -> retail -> monthly internal heat gain
    #             -> garage -> garage schedule
    start_row    = [9,  19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 49, 63, 49, 73, 80, 60, 61, 73, 65,  9, 61] ####
    end_row      = [16, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 59, 70, 52, 78, 82, 62, 85, 74, 77, 14, 85]
    start_column = [6,  12, 20, 28, 36, 44, 52, 60, 68, 76, 84, 6,  6,  20, 6,  6,  14, 16, 11, 20, 16, 28]
    end_column   = [16, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 17, 10, 21, 7,  7,  15, 18, 12, 23, 17, 32] ####
    
    for i in range(len(start_row)):
        for j in range(start_row[i], end_row[i]):
            for k in range(start_column[i], end_column[i]):
##                print(f"i: {i}, j: {j}, k:{k}")
                inputs[j][k] = Mal_Input_Identifier(inputs[j][k])

    # 2. Generate a BEMP input dictionary
    BEMP_JSON={}
    # Building General
    BEMP_JSON["Name"] = inputs[11][2]                                  # Building Name
    BEMP_JSON["TerrainClass"] = inputs[12][2]                          # Terrain class
    BEMP_JSON["Volume"] = float(inputs[13][2])                         # Building total Ventilated volume [m3]
    BEMP_JSON["Height"] = float(inputs[14][2])                         # Building Height [m]

    # Heat Capacity
    BEMP_JSON["HeatCapacity"] = inputs[17][2]                          # Envelope Heat Capacity (J/K)

    # Building System
    # Lighting
    BEMP_JSON["DaylightingFactor"] = float(inputs[21][2])              # Lighting daylighting factor
    BEMP_JSON["OccupancyFactor"] = float(inputs[22][2])                # Lighting occupancy factor
    BEMP_JSON["LightingControlFactor"] = float(inputs[23][2])          # Lighting constant illumination control factor
    BEMP_JSON["ParasiticLightingEnergy"] = inputs[24][2]               # Is parasitic lighting energy considered?
    BEMP_JSON["ParasiticLightingEnergyAmount"] = float(inputs[25][2])  # Annual parasitic energy for emergency lighting and automatic lighting controls (kWh/m2/yr)

    # Heating and Cooling Plants
    BEMP_JSON["HeatingCOP"] = float(inputs[27][2])                     # Heating System Coefficient of Performance (COP) [KW/KW]
    BEMP_JSON["CoolingCOP"] = float(inputs[28][2])                     # Cooling System Full Load COP [KW/KW]
    BEMP_JSON["COP100"] = float(inputs[29][2])                         # Relative COP100: for Relative Load 100%
    BEMP_JSON["COP75"] = float(inputs[30][2])                          # Partial Load COP75 Relative Load 75%
    BEMP_JSON["COP50"] = float(inputs[31][2])                          # Partial Load COP50 Relative Load 50%
    BEMP_JSON["COP25"] = float(inputs[32][2])                          # Partial Load COP25 Relative Load 25%
    BEMP_JSON["COPWeighting100"] = float(inputs[33][2])                # Weighting of 100% Load
    BEMP_JSON["COPWeighting75"] = float(inputs[34][2])                 # Weighting of 75% Load
    BEMP_JSON["COPWeighting50"] = float(inputs[35][2])                 # Weighting of 50% Load
    BEMP_JSON["COPWeighting25"] = float(inputs[36][2])                 # Weighting of 25% Load

    # HVAC System
    BEMP_JSON["HVACSystemType"] = inputs[38][2]                        # HVAC system type: (System / Heat distrition by / Cold distribution by / room temp. cntrl)
    BEMP_JSON["VentilationCoolingType"] = inputs[39][2]                # Ventilation and Cooling type
    BEMP_JSON["RHThreshold"] = float(inputs[40][2])                    # Relative Humidity threshold for outside air cooling - upper limit (%)
    BEMP_JSON["ExtraVentilation"] = float(inputs[41][2])               # Extra ventilation above fresh air supply (liter/s)
    BEMP_JSON["HeatRecoveryType"] = inputs[42][2]                      # Heat recovery type
    BEMP_JSON["ExhaustAirRecirculation"] = inputs[43][2]               # Exhaust air recirculation percentage
    BEMP_JSON["AirLeakageLevel"] = float(inputs[44][2])                # Building air leakage level (Air flow m3/h per floor area at Q4Pa)
    BEMP_JSON["SpecificFanPower"] = float(inputs[45][2])               # Specifiec fan power [W/(l/s)]
    BEMP_JSON["FanControlFactor"] = float(inputs[46][2])               # Fan flow control factor
    BEMP_JSON["PumpCoolingControl"] = inputs[47][2]                    # Pump control for cooling
    BEMP_JSON["PumpHeatingControl"] = inputs[48][2]                    # Pump control for heating

    # Domestic Hot Water System
    BEMP_JSON["DHWDistrinutionSystem"] = inputs[50][2]                 # DHW Distribution System 
    BEMP_JSON["DHWGenerationSystem"] = inputs[51][2]                   # DHW Generation System

    # Building Energy Management System
    BEMP_JSON["BEMType"] = int(inputs[53][2])                          # Type of BEM system installed

    # Bldg Integrated Energy Generation System
    # Photovoltaic System
    BEMP_JSON["PVArea"] = float(inputs[57][2])                         # PV module Surface Area (m2)
    BEMP_JSON["PVOrientation"] = inputs[58][2]                         # PV Module Orientation
    BEMP_JSON["PVTiltAngle"] = int(inputs[59][2])                      # PV Module Angle (tilt in degrees)
    BEMP_JSON["PVPeakPower"] = float(inputs[60][2])                    # PV panel peak power coefficient (kW/m2)
    BEMP_JSON["PVPerformanceFactor"] = float(inputs[61][2])            # PV system performance factor (level of ventilation)

    # Solar Water Heating System
    BEMP_JSON["SHWArea"] = float(inputs[63][2])                        # Solar Collector Surface Area (m2)
    BEMP_JSON["SHWOrientation"] = inputs[64][2]                        # SHW module orientation
    BEMP_JSON["SHWTiltAngle"] = int(inputs[65][2])                     # SHW module angle (tilt in degrees)
    BEMP_JSON["SHWEfficiency"] = float(inputs[66][2])                  # Solar Collector Efficiency

    # Wind Turbine System
    BEMP_JSON["WindTurbineDiameter"] = float(inputs[68][2])            # Wind Turbine diameter [m]
    BEMP_JSON["WindTurbineEfficiency"] = float(inputs[69][2])          # Wind Turbine efficiency

    # Energy Sources
    BEMP_JSON["HeatingEnergySource"] = inputs[72][2]                   # Primary energy source for Heating
    BEMP_JSON["DHWEnergySource"] = inputs[73][2]                       # Primary energy source for DHW
    BEMP_JSON["CoolingEnergySource"] = inputs[74][2]                   # Primary energy source for Cooling
    
    # Primary and Emission Factor
    BEMP_JSON["Electricity"]={}; BEMP_JSON["NaturalGas"]={}; BEMP_JSON["Fuel"]={}
    BEMP_JSON["Electricity"]["PrimaryEnergyFactor"] = float(inputs[77][2])
    BEMP_JSON["Electricity"]["CO2EmissionCoefficient"] = float(inputs[77][3])

    BEMP_JSON["NaturalGas"]["PrimaryEnergyFactor"] = float(inputs[78][2])
    BEMP_JSON["NaturalGas"]["CO2EmissionCoefficient"] = float(inputs[78][3])

    BEMP_JSON["Fuel"]["PrimaryEnergyFactor"] = float(inputs[79][2])
    BEMP_JSON["Fuel"]["CO2EmissionCoefficient"] = float(inputs[79][3]) 


    # Zone
    i=0
    while 1:
        if inputs[9][i+6] not in  ["0", '']:
            zone_name = "".join(["Zone", str(i+1)])
            BEMP_JSON[zone_name]={}
            BEMP_JSON[zone_name]["SpaceName"] = inputs[8][i+6]             # Space Name
            BEMP_JSON[zone_name]["GrossFloorArea"] = float(inputs[9][i+6]) # Gross Floor Area (m2)
            BEMP_JSON[zone_name]["Occupancy"] = float(inputs[10][i+6])     # Occupancy (m2/person)
            BEMP_JSON[zone_name]["MatabolicRate"] = float(inputs[11][i+6]) # Metabolic rate (W/person)
            BEMP_JSON[zone_name]["Appliance"] = float(inputs[12][i+6])     # Appliance (W/m2)
            BEMP_JSON[zone_name]["Lighting"] = float(inputs[13][i+6])      # Lighting (W/m2)
            BEMP_JSON[zone_name]["OutdoorAir"] = float(inputs[14][i+6])    # Outdoor Air (liter/s/person)
            BEMP_JSON[zone_name]["DHW"] = float(inputs[15][i+6])           # DHW (liter/m2/month)
            i += 1
        else:
            break

    # Building Temperature Set-point Schedule & Zone 1 Schedule
    BEMP_JSON["TemperatureSetPoint"]={}; BEMP_JSON["Zone1_Schedule"]={}
    for i in range(24):
        BEMP_JSON["TemperatureSetPoint"]["".join(["Hour", str(i+1)])]={}
        BEMP_JSON["Zone1_Schedule"]["".join(["Hour", str(i+1)])]={}

    for i in range(24):
        # Set point
        BEMP_JSON["TemperatureSetPoint"]["".join(["Hour", str(i+1)])]["Heating_Weekday"] = float(inputs[i+19][6])
        BEMP_JSON["TemperatureSetPoint"]["".join(["Hour", str(i+1)])]["Heating_Weekend"] = float(inputs[i+19][7])
        BEMP_JSON["TemperatureSetPoint"]["".join(["Hour", str(i+1)])]["Cooling_Weekday"] = float(inputs[i+19][8])
        BEMP_JSON["TemperatureSetPoint"]["".join(["Hour", str(i+1)])]["Cooling_Weekend"] = float(inputs[i+19][9])

        # Zone 1 Schedule
        BEMP_JSON["Zone1_Schedule"]["".join(["Hour", str(i+1)])]["Occupancy_Weekday"] = float(inputs[i+19][12])
        BEMP_JSON["Zone1_Schedule"]["".join(["Hour", str(i+1)])]["Occupancy_Weekend"] = float(inputs[i+19][13])
        BEMP_JSON["Zone1_Schedule"]["".join(["Hour", str(i+1)])]["Appliance_Weekday"] = float(inputs[i+19][14])
        BEMP_JSON["Zone1_Schedule"]["".join(["Hour", str(i+1)])]["Appliance_Weekend"] = float(inputs[i+19][15])
        BEMP_JSON["Zone1_Schedule"]["".join(["Hour", str(i+1)])]["Lighting_Weekday"] = float(inputs[i+19][16])
        BEMP_JSON["Zone1_Schedule"]["".join(["Hour", str(i+1)])]["Lighting_Weekend"] = float(inputs[i+19][17])
        

    # Zone 2-10 Schedule
    zone_schedule_column_index = [20, 28, 36, 44, 52, 60, 68, 76, 84]
    zone_index=2
    for i in zone_schedule_column_index:
##        if inputs[19][i]!=0 and inputs[19][i+1]!='0' and inputs[19][i+2]!='0' and inputs[20][i+3]!='0':
        if inputs[9][zone_index+5] != '0':
            current_zone = "".join(["Zone", str(zone_index),"_Schedule"])
            BEMP_JSON[current_zone]={}
            zone_index += 1
            for j in range(24):
                current_hour = "".join(["Hour", str(j+1)])
                BEMP_JSON[current_zone][current_hour]={}
                BEMP_JSON[current_zone][current_hour]["Occupancy_Weekday"] = float(inputs[j+19][20])
                BEMP_JSON[current_zone][current_hour]["Occupancy_Weekend"] = float(inputs[j+19][21])
                BEMP_JSON[current_zone][current_hour]["Appliance_Weekday"] = float(inputs[j+19][22])
                BEMP_JSON[current_zone][current_hour]["Appliance_Weekend"] = float(inputs[j+19][23])
                BEMP_JSON[current_zone][current_hour]["Lighting_Weekday"] = float(inputs[j+19][24])
                BEMP_JSON[current_zone][current_hour]["Lighting_Weekend"] = float(inputs[j+19][25])
            
   
    # Envelope
    BEMP_JSON["Envelope"]={}; BEMP_JSON["Envelope"]["Opaque1"]={}; BEMP_JSON["Envelope"]["Window1"]={};

    Orientation_container = ["S", "SE", "E", "NE", "N", "NW", "W", "SW", "Roof", "BelowGrade"]
    for i in range(10):
        BEMP_JSON["Envelope"]["Opaque1"][Orientation_container[i]]={}
        BEMP_JSON["Envelope"]["Opaque1"][Orientation_container[i]]["Area"] = float(inputs[i+49][6])

        if i != 10:
            BEMP_JSON["Envelope"]["Window1"][Orientation_container[i]]={}
            BEMP_JSON["Envelope"]["Window1"][Orientation_container[i]]["Area"] = float(inputs[i+49][8])
            BEMP_JSON["Envelope"]["Window1"][Orientation_container[i]]["OverhangAngle"] = int(inputs[i+49][9])
            BEMP_JSON["Envelope"]["Window1"][Orientation_container[i]]["FinAngle"] = int(inputs[i+49][10])
            BEMP_JSON["Envelope"]["Window1"][Orientation_container[i]]["HorizonAngle"] = int(inputs[i+49][11])
            BEMP_JSON["Envelope"]["Window1"][Orientation_container[i]]["SRF"] = float(inputs[i+49][12])
            

    # Check if opaque 2 and window 2 exist
    opqaue2_exist = False; window2_exist = False
    i=0
    while 1: # opaque2 
        if inputs[i+49][7]!="0":
            opqaue2_exist = True
            break
        elif i+49 == 58:
            break
        i += 1 
         
    if opqaue2_exist == True:
        BEMP_JSON["Envelope"]["Opaque2"]={}
        for i in range(10):
            BEMP_JSON["Envelope"]["Opaque2"][Orientation_container[i]]={}
            BEMP_JSON["Envelope"]["Opaque2"][Orientation_container[i]]["Area"] = float(inputs[i+49][7])

            
    i=0
    while 1: # window2
        if inputs[i+49][13]!="0":
            window2_exist = True
            break
        elif i+49 == 57:
            break
        i += 1

    if window2_exist == True:
        BEMP_JSON["Envelope"]["Window2"]={}
        for i in range(9):
            BEMP_JSON["Envelope"]["Window2"][Orientation_container[i]]={}
           
            BEMP_JSON["Envelope"]["Window2"][Orientation_container[i]]["Area"] = float(inputs[i+49][13])
            BEMP_JSON["Envelope"]["Window2"][Orientation_container[i]]["OverhangAngle"] = int(inputs[i+49][14])
            BEMP_JSON["Envelope"]["Window2"][Orientation_container[i]]["FinAngle"] = int(inputs[i+49][15])
            BEMP_JSON["Envelope"]["Window2"][Orientation_container[i]]["HorizonAngle"] = int(inputs[i+49][16])
            BEMP_JSON["Envelope"]["Window2"][Orientation_container[i]]["SRF"] = float(inputs[i+49][17])


    # Material
    BEMP_JSON["Material"]={}
    BEMP_JSON["Material"]["Roof1"]={}; BEMP_JSON["Material"]["Opaque1"]={}; BEMP_JSON["Material"]["Window1"]={};
    
    BEMP_JSON["Material"]["Roof1"]["UValue"]= float(inputs[63][6])
    BEMP_JSON["Material"]["Roof1"]["Absorptivity"]= float(inputs[63][7])
    BEMP_JSON["Material"]["Roof1"]["Emissivity"]= float(inputs[63][8])

    if inputs[64][6]!="0" and inputs[64][7]!="0" and inputs[64][8]!="0": # Roof 2
        BEMP_JSON["Material"]["Roof2"]={}
        
        BEMP_JSON["Material"]["Roof2"]["UValue"]= float(inputs[64][6])
        BEMP_JSON["Material"]["Roof2"]["Absorptivity"]= float(inputs[64][7])
        BEMP_JSON["Material"]["Roof2"]["Emissivity"]= float(inputs[64][8]) 

    BEMP_JSON["Material"]["Opaque1"]["UValue"]= float(inputs[65][6])
    BEMP_JSON["Material"]["Opaque1"]["Absorptivity"]= float(inputs[65][7]) 
    BEMP_JSON["Material"]["Opaque1"]["Emissivity"]= float(inputs[65][8])


    if inputs[66][6]!="0" and inputs[66][7]!="0" and inputs[66][8]!="0": # Opaque 2
        BEMP_JSON["Material"]["Opaque2"]={}
        
        BEMP_JSON["Material"]["Opaque2"]["UValue"]= float(inputs[66][6])
        BEMP_JSON["Material"]["Opaque2"]["Absorptivity"]= float(inputs[66][7])
        BEMP_JSON["Material"]["Opaque2"]["Emissivity"]= float(inputs[66][8])
        

    BEMP_JSON["Material"]["Window1"]["UValue"]= float(inputs[67][6])
    BEMP_JSON["Material"]["Window1"]["Emissivity"]= float(inputs[67][8]) 
    BEMP_JSON["Material"]["Window1"]["SolarTrasmittance"]= float(inputs[67][9])

    if inputs[68][6]!="0" and inputs[68][7]!="0" and inputs[68][8]!="0": # Window 2
        BEMP_JSON["Material"]["Window2"]["UValue"]= float(inputs[67][6])
        BEMP_JSON["Material"]["Window2"]["Emissivity"]= float(inputs[67][8]) 
        BEMP_JSON["Material"]["Window2"]["SolarTrasmittance"]= float(inputs[67][9])

    # start date
    BEMP_JSON["StartDay"] = {}
    BEMP_JSON["StartDay"] = inputs[70][6]

    # natural ventilation
    BEMP_JSON["NaturalVentilation"]={}
    BEMP_JSON["NaturalVentilation"]["Width"] = float(inputs[49][20])
    BEMP_JSON["NaturalVentilation"]["Height"] = float(inputs[50][20])
    BEMP_JSON["NaturalVentilation"]["EffectiveAngle"] = float(inputs[51][20])

    # electric battery
    BEMP_JSON["ElectricBattery"]={}
    BEMP_JSON["ElectricBattery"]["Capacity"]              = float(inputs[73][6])
    BEMP_JSON["ElectricBattery"]["ChargingEfficiency"]    = float(inputs[74][6])
    BEMP_JSON["ElectricBattery"]["DischargingEfficiency"] = float(inputs[75][6])
    BEMP_JSON["ElectricBattery"]["ChargingPowerLimit"]    = float(inputs[76][6])
    BEMP_JSON["ElectricBattery"]["DischargingPowerLimit"] = float(inputs[77][6])

    # lighting dimmer
    BEMP_JSON["LightingDimmer"]={}
    BEMP_JSON["LightingDimmer"]["DimmerSaving_WD"] = float(inputs[80][6])
    BEMP_JSON["LightingDimmer"]["DimmerSaving_WE"] = float(inputs[81][6])

    # electric vehicle
    BEMP_JSON["ElectricVehicle"]={}
    BEMP_JSON["ElectricVehicle"]["No_EVCharger"]  = float(inputs[60][14])
    BEMP_JSON["ElectricVehicle"]["ChargingPower"] = float(inputs[61][14])

    for i in range(24):
        BEMP_JSON["ElectricVehicle"]["".join(["Hour", str(i+1)])]={}

    for i in range(24):
        tempo_time = "".join(["Hour", str(i+1)])
        tempo_row = i+61
        BEMP_JSON["ElectricVehicle"][tempo_time]["EV_Weekday"] = float(inputs[tempo_row][16])
        BEMP_JSON["ElectricVehicle"][tempo_time]["EV_Weekend"] = float(inputs[tempo_row][17])

    # retail
    BEMP_JSON["RetailRefrig"]={}
    BEMP_JSON["RetailRefrig"]["Capacity"] = float(inputs[73][11])
    BEMP_JSON["RetailRefrig"]["Zone"]     = str(inputs[74][11].strip())

    # monthly internal heat gain
    if inputs[6][6] == "Monthly":
        month_name = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        BEMP_JSON["Monthly_InternalHeatGain"]={}
        BEMP_JSON["Monthly_InternalHeatGain"]["Occupancy"]={}
        BEMP_JSON["Monthly_InternalHeatGain"]["Appliance"]={}
        BEMP_JSON["Monthly_InternalHeatGain"]["Lighting"] ={}

        for i in range(12):
            BEMP_JSON["Monthly_InternalHeatGain"]["Occupancy"][month_name[i]] = float(inputs[i+65][20])
            BEMP_JSON["Monthly_InternalHeatGain"]["Appliance"][month_name[i]] = float(inputs[i+65][21])
            BEMP_JSON["Monthly_InternalHeatGain"]["Lighting"][month_name[i]]  = float(inputs[i+65][22])
  
    # garage
    BEMP_JSON["Garage"]={}
    BEMP_JSON["Garage"]["SpaceName"]= inputs[8][16]
    BEMP_JSON["Garage"]["Occupancy"]= float(inputs[9][16])
    BEMP_JSON["Garage"]["Appliance"]= float(inputs[12][16])
    BEMP_JSON["Garage"]["Lighting"] = float(inputs[13][16])

    BEMP_JSON["Garage_Schedule"]={}
    for i in range(24):
        tempo_hour = "".join(["Hour", str(i+1)])
        BEMP_JSON["Garage_Schedule"][tempo_hour]={}

    for i in range(24):
        tempo_hour = "".join(["Hour", str(i+1)])
        BEMP_JSON["Garage_Schedule"][tempo_hour]["Appliance_Weekday"] = float(inputs[i+61][28])
        BEMP_JSON["Garage_Schedule"][tempo_hour]["Appliance_Weekend"] = float(inputs[i+61][29])
        BEMP_JSON["Garage_Schedule"][tempo_hour]["Lighting_Weekday"]  = float(inputs[i+61][30])
        BEMP_JSON["Garage_Schedule"][tempo_hour]["Lighting_Weekend"]  = float(inputs[i+61][31])
                   
              
    # 3. Generate JSON intance
    with open("".join([building_name[:-4],'.json']), 'w', encoding='utf-8') as f:
        json.dump(BEMP_JSON, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    print("Please execute the 'main.py' script.")
