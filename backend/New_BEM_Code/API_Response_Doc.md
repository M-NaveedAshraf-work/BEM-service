# /input
## methods=['GET 'PUT'])
**Purpose**: Stores BEMP.py input parameters needed to run a simulation

**Response**:
```
{
  "inputData": {
    "historicalData1": "BEM_Optimization_Input_v2_centergy_BEM_2019.xlsx",
    "historicalData2": "BEM_Optimization_Input_v2_centergy_BEM_2019.xlsx",
    "jsonData": {
      "AirLeakageLevel": 2.0,
      "BEMType": 2,
      "COP100": 1.0,
      "COP25": 0.5,
      "COP50": 0.82,
      "COP75": 0.9,
      "COPWeighting100": 0.01,
      "COPWeighting25": 0.12,
      "COPWeighting50": 0.45,
      "COPWeighting75": 0.42,
      "CoolingCOP": 4.6836437236367265,
      "CoolingEnergySource": "Electricity",
      "DHWDistrinutionSystem": "Taps More Than 3m from Heat Generation",
      "DHWEnergySource": "Electricity",
      "DHWGenerationSystem": "Electric (0.75)",
      "DaylightingFactor": 1.0,
      "ElectricBattery": {
        "Capacity": 0.0,
        "ChargingEfficiency": 0.0,
        "ChargingPowerLimit": 0.0,
        "DischargingEfficiency": 0.0,
        "DischargingPowerLimit": 0.0
      },
      "ElectricVehicle": {
        "ChargingPower": 0.0,
        "Hour1": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour10": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour11": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour12": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour13": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour14": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour15": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour16": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour17": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour18": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour19": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour2": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour20": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour21": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour22": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour23": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour24": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour3": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour4": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour5": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour6": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour7": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour8": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "Hour9": {
          "EV_Weekday": 0.0,
          "EV_Weekend": 0.0
        },
        "No_EVCharger": 0.0
      },
      "Electricity": {
        "CO2EmissionCoefficient": 744.0,
        "PrimaryEnergyFactor": 3.39
      },
      "Envelope": {
        "Opaque1": {
          "BelowGrade": {
            "Area": 3077.89
          },
          "E": {
            "Area": 1969.91
          },
          "N": {
            "Area": 2671.02
          },
          "NE": {
            "Area": 0.0
          },
          "NW": {
            "Area": 0.0
          },
          "Roof": {
            "Area": 5852.89
          },
          "S": {
            "Area": 2671.02
          },
          "SE": {
            "Area": 0.0
          },
          "SW": {
            "Area": 0.0
          },
          "W": {
            "Area": 1872.91
          }
        },
        "Window1": {
          "BelowGrade": {
            "Area": 0.0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 0.0
          },
          "E": {
            "Area": 1456.0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 0.4905
          },
          "N": {
            "Area": 1975.7,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 0.4905
          },
          "NE": {
            "Area": 0.0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 1.0
          },
          "NW": {
            "Area": 0.0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 1.0
          },
          "Roof": {
            "Area": 0.0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 1.0
          },
          "S": {
            "Area": 1975.7,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 0.4905
          },
          "SE": {
            "Area": 0.0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 1.0
          },
          "SW": {
            "Area": 0.0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 1.0
          },
          "W": {
            "Area": 1378.0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 0.4905
          }
        }
      },
      "ExhaustAirRecirculation": "Exhaust air recirculation  60%",
      "ExtraVentilation": 0.0,
      "FanControlFactor": 0.65,
      "Fuel": {
        "CO2EmissionCoefficient": 330.0,
        "PrimaryEnergyFactor": 1.19
      },
      "Garage": {
        "Appliance": 2.0,
        "Lighting": 8.0,
        "Occupancy": 0.0,
        "SpaceName": ""
      },
      "Garage_Schedule": {
        "Hour1": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour10": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour11": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour12": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour13": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour14": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour15": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour16": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour17": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour18": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour19": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour2": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour20": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour21": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour22": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour23": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour24": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour3": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour4": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour5": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour6": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour7": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour8": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        },
        "Hour9": {
          "Appliance_Weekday": 0.0,
          "Appliance_Weekend": 0.0,
          "Lighting_Weekday": 0.0,
          "Lighting_Weekend": 0.0
        }
      },
      "HVACSystemType": "22. Variable air volume / Water or Water&Air / Water / Yes",
      "HeatCapacity": "Heavy: 260,000 * Af",
      "HeatRecoveryType": "Slowly rotating or intermittent heat exchangers (0.7)",
      "HeatingCOP": 0.7452668159525578,
      "HeatingEnergySource": "Electricity",
      "Height": 52.0,
      "LightingControlFactor": 1.0,
      "LightingDimmer": {
        "DimmerSaving_WD": 0.0,
        "DimmerSaving_WE": 0.0
      },
      "Material": {
        "Opaque1": {
          "Absorptivity": 0.7,
          "Emissivity": 0.92,
          "UValue": 0.37840367791539986
        },
        "Roof1": {
          "Absorptivity": 0.85,
          "Emissivity": 0.7929518053345709,
          "UValue": 0.21
        },
        "Window1": {
          "Emissivity": -0.036142153396077986,
          "SolarTrasmittance": 0.41,
          "UValue": 0.2935935299380026
        }
      },
      "Name": "Building_Name",
      "NaturalGas": {
        "CO2EmissionCoefficient": 277.0,
        "PrimaryEnergyFactor": 1.09
      },
      "NaturalVentilation": {
        "EffectiveAngle": 0.0,
        "Height": 0.0,
        "Width": 0.0
      },
      "OccupancyFactor": 1.0,
      "OutputPeriod": "Monthly",
      "PVArea": 0.0,
      "PVOrientation": "S",
      "PVPeakPower": 0.15,
      "PVPerformanceFactor": 0.7,
      "PVTiltAngle": 30,
      "ParasiticLightingEnergy": "Yes",
      "ParasiticLightingEnergyAmount": 6.0,
      "PumpCoolingControl": "All other cases",
      "PumpHeatingControl": "All other cases",
      "RHThreshold": 75.0,
      "RetailRefrig": {
        "Capacity": 0.0,
        "Zone": ""
      },
      "SHWArea": 0.0,
      "SHWEfficiency": 0.5,
      "SHWOrientation": "S",
      "SHWTiltAngle": 30,
      "SpecificFanPower": 2.5,
      "StartDay": "Tuesday",
      "TemperatureSetPoint": {
        "Hour1": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour10": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour11": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour12": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour13": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour14": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour15": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour16": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour17": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour18": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour19": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour2": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour20": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour21": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour22": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour23": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour24": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour3": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour4": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour5": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour6": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour7": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour8": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour9": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        }
      },
      "TerrainClass": "Urban / City",
      "VentilationCoolingType": "1. Mechanical system only; no provision for natural ventilation",
      "Volume": 198218.0,
      "WindTurbineDiameter": 0.0,
      "WindTurbineEfficiency": 0.4,
      "Zone1": {
        "Appliance": 13.099276456946004,
        "DHW": 4.1,
        "GrossFloorArea": 43213.11,
        "Lighting": 10.27254555831506,
        "MatabolicRate": 105.0,
        "Occupancy": 30.91,
        "OutdoorAir": 8.33,
        "SpaceName": "Space_Nm"
      },
      "Zone1_Schedule": {
        "Hour1": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour10": {
          "Appliance_Weekday": 1.0,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1.0,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 1.0,
          "Occupancy_Weekend": 0.3
        },
        "Hour11": {
          "Appliance_Weekday": 1.0,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1.0,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 1.0,
          "Occupancy_Weekend": 0.3
        },
        "Hour12": {
          "Appliance_Weekday": 1.0,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1.0,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 1.0,
          "Occupancy_Weekend": 0.3
        },
        "Hour13": {
          "Appliance_Weekday": 1.0,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1.0,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 1.0,
          "Occupancy_Weekend": 0.3
        },
        "Hour14": {
          "Appliance_Weekday": 1.0,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1.0,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 1.0,
          "Occupancy_Weekend": 0.3
        },
        "Hour15": {
          "Appliance_Weekday": 1.0,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1.0,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 1.0,
          "Occupancy_Weekend": 0.3
        },
        "Hour16": {
          "Appliance_Weekday": 1.0,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1.0,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 1.0,
          "Occupancy_Weekend": 0.3
        },
        "Hour17": {
          "Appliance_Weekday": 1.0,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1.0,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 1.0,
          "Occupancy_Weekend": 0.3
        },
        "Hour18": {
          "Appliance_Weekday": 1.0,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1.0,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 1.0,
          "Occupancy_Weekend": 0.3
        },
        "Hour19": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour2": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour20": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour21": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour22": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour23": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour24": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour3": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour4": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour5": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour6": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour7": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour8": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour9": {
          "Appliance_Weekday": 1.0,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1.0,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 1.0,
          "Occupancy_Weekend": 0.3
        }
      }
    },
    "weatherData": "centergy_2019_epw_file.epw"
  },
  "status": "success"
}
```

# /BEM
## methods=['GET'])
**Purpose**: Runs BEMP.py and return simulation output data. 

**Response**:

Note: The "monthly" response will return hourly data if an hourly simulation is specified

```
{
  "hourlyXAxis": [
    "8/12/19 3:00 AM",
    "8/12/19 4:00 AM",
    "8/12/19 5:00 AM",
    "8/12/19 6:00 AM",
    "8/12/19 7:00 AM",
    "8/12/19 8:00 AM",
    "8/12/19 9:00 AM",
    "8/12/19 10:00 AM",
    "8/12/19 11:00 AM",
    "8/12/19 12:00 PM",
    "8/12/19 1:00 PM",
    ... Continues For a Year
 ],
 "monthly": [
    597461.3710946427,
    554394.9932013091,
    464793.168906857,
    512953.3581184808,
    616330.3467880326,
    468564.30711223895,
    510833.1881238521,
    524711.9364277617,
    584663.0103323687,
    555621.0517085561,
    627265.3002421116,
    629105.7039985397
  ],
  "monthlyXAxis": [
    "September",
    "October",
    "November",
    "December",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August"
  ],
  "status": "success",
  "subs": [
    [
      13893.54349969737
    ],
    [
      23396.786201826802
    ],
    [
      39475.18596198799
    ],
    [
      16837.50610090771
    ],
    [
      4478.0823731956025
    ],
    [
      54441.11692612588
    ],
    [
      4796.585981989138
    ],
    [
      0.0
    ],
    [
      0.0
    ],
    [
      0.0
    ],
    [
      157318.80704573047
    ],
    [
      0.0
    ]
  ]
}
```

# /Calibration + /auto_calibration
## methods=['GET'])
**Purpose**: Runs Genetic_Algorithm.py in Calibration Mode. Return a real and simulated calibration output to be graphed. When running the auto_calibration version the Genetic_Algorithm.py parameters will update themselfs for 5 different runs. The calibration run with the lowest error will be selected and output as a response. 

Note: If interval is "hourly" response will return hourly data

**Response**:

```
{
  "hourlyXAxis": [
    "8/12/19 3:00 AM",
    "8/12/19 4:00 AM",
    "8/12/19 5:00 AM",
    "8/12/19 6:00 AM",
    "8/12/19 7:00 AM",
    "8/12/19 8:00 AM",
    "8/12/19 9:00 AM",
    "8/12/19 10:00 AM",
    "8/12/19 11:00 AM",
    "8/12/19 12:00 PM",
    "8/12/19 1:00 PM",
    "8/12/19 2:00 PM",
    "8/12/19 3:00 PM",
    continues for year ...
],
 "interval": "Monthly",
  "modeled": [
    687418.2947309079,
    617630.608161584,
    487639.2395495796,
    534515.5007375103,
    640129.8626984872,
    496458.2001997975,
    541809.3291950568,
    577012.401212008,
    660400.8549700814,
    629503.674883664,
    719363.1635057091,
    721880.0012061171
  ],
  "monthlyXAxis": [
    "September",
    "October",
    "November",
    "December",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August"
  ],
  "real": [
    10772.041426895401,
    9415.851044915007,
    8480.132187024046,
    9041.204757297042,
    10391.020232654811,
    8804.338318624397,
    9242.81829752331,
    9305.11136580192,
    11426.745691240745,
    12383.488733500866,
    12644.654785147552,
    13421.939149278702
  ],
  "status": "success"
}
```

# /Cal
## methods=['GET' 'PUT'])
**Purpose**: Stores Inputs to run Genetic_Algorithm.py in both Calibration and CapX Modes.

**Response**:

```
{
  "calData": {
    "actualGraphData": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "calGraphData": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "calibration_parameters": [
      {
        "data": "Float",
        "max": ".95",
        "min": ".7",
        "name": "Heating COP"
      },
      {
        "data": "Float",
        "max": "4.5",
        "min": "2.5",
        "name": "Cooling COP"
      }
    ],
    "calibration_settings": {
      "convergence_diff": 1e-06,
      "cvrmse_criterion": 2,
      "data_interval": "Monthly",
      "electricity_data": "Yes",
      "n_times_converge": 15,
      "natural_gas_data": "No"
    },
    "capxGraphData": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "capxParameterValues": {
      "DHWGenerationSystem": {
        "VRBoiler": {
          "cost": "43409 -1088 MBH",
          "param1": 0.61
        },
        "coGeneration": {
          "cost": "50000 -b",
          "param1": 0.9
        },
        "districtHeating": {
          "cost": "50000 -b",
          "param1": 0.9
        },
        "electric": {
          "cost": "33734 -1010 MBH",
          "param1": 0.75
        },
        "gasBoiler": {
          "cost": "43409 -1088 MBH",
          "param1": 0.75
        },
        "heatPump": {
          "cost": "52100 -50 ton",
          "param1": 2
        },
        "steam": {
          "cost": "43509 -1023 MBH",
          "param1": 0.61
        }
      },
      "FinE": {
        "fin1": {
          "cost": 0,
          "param1": 0
        },
        "fin2": {
          "cost": 2500,
          "param1": 30
        },
        "fin3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "FinN": {
        "fin1": {
          "cost": 0,
          "param1": 11
        },
        "fin2": {
          "cost": 2500,
          "param1": 8
        },
        "fin3": {
          "cost": 2500,
          "param1": 9
        }
      },
      "FinNE": {
        "fin1": {
          "cost": 0,
          "param1": 0
        },
        "fin2": {
          "cost": 2500,
          "param1": 30
        },
        "fin3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "FinNW": {
        "fin1": {
          "cost": 0,
          "param1": 0
        },
        "fin2": {
          "cost": 2500,
          "param1": 30
        },
        "fin3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "FinS": {
        "fin1": {
          "cost": 0,
          "param1": 11
        },
        "fin2": {
          "cost": 2500,
          "param1": 8
        },
        "fin3": {
          "cost": 2500,
          "param1": 9
        }
      },
      "FinSE": {
        "fin1": {
          "cost": 0,
          "param1": 0
        },
        "fin2": {
          "cost": 2500,
          "param1": 30
        },
        "fin3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "FinSW": {
        "fin1": {
          "cost": 0,
          "param1": 0
        },
        "fin2": {
          "cost": 2500,
          "param1": 30
        },
        "fin3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "FinW": {
        "fin1": {
          "cost": 0,
          "param1": 11
        },
        "fin2": {
          "cost": 2500,
          "param1": 8
        },
        "fin3": {
          "cost": 2500,
          "param1": 9
        }
      },
      "PVModule": {
        "maximum": {
          "cost": 43056,
          "param1": 500
        },
        "minimum": {
          "cost": 0,
          "param1": 0
        }
      },
      "airLeakage": {
        "maximum": {
          "cost": 0,
          "param1": 0
        },
        "minimum": {
          "cost": 0,
          "param1": 0
        }
      },
      "appliance": {
        "eStarBaseline": {
          "cost": 0,
          "param1": 12
        },
        "eStarTop10": {
          "cost": 1350,
          "param1": 20
        },
        "eStarTop5": {
          "cost": 2120,
          "param1": 25
        }
      },
      "coolingEfficiency": {
        "absorptionWaterChiller": {
          "cost": "240300 -148 ton",
          "param1": 1.9
        },
        "centrifugalWaterChiller": {
          "cost": "164300 -400 ton",
          "param1": 7.1
        },
        "reciprocatingAirChiller": {
          "cost": "121600 -150 ton",
          "param1": 2.8
        },
        "reciprocatingWaterChiller": {
          "cost": "106200 -155 ton",
          "param1": 5
        }
      },
      "electricBattery": {
        "baseline": {
          "cost": 0,
          "param1": 150,
          "param2": 0.98,
          "param3": 0.98
        },
        "improve1": {
          "cost": 3460,
          "param1": 200,
          "param2": 0.98,
          "param3": 0.95
        },
        "improve2": {
          "cost": 6840,
          "param1": 250,
          "param2": 0.96,
          "param3": 0.96
        }
      },
      "heatRecovery": {
        "None": {
          "cost": "0 -O GPM",
          "param1": 0
        },
        "heatExchangePipes": {
          "cost": "3550 -1700 CFM",
          "param1": 0.6
        },
        "heatExchangePlates": {
          "cost": "64625 -800 GPM",
          "param1": 0.9
        },
        "rotation": {
          "cost": "2000 -",
          "param1": 0.75
        },
        "twoElement": {
          "cost": "25800 -152 GPM",
          "param1": 0.65
        }
      },
      "heatingCoolingEfficiency": {
        "heatPumpAA": {
          "cost": "11900 -10 ton",
          "param1": 2.05,
          "param2": 2.8
        },
        "heatPumpWA": {
          "cost": "11650 -10 ton",
          "param1": 2.28,
          "param2": 3.21
        }
      },
      "heatingEfficiency": {
        "electricSteamBoiler": {
          "cost": "43509 -1023 MBH",
          "param1": 0.61
        },
        "electricWaterBoiler": {
          "cost": "33734 -1010 MBH",
          "param1": 0.99
        },
        "gasSteamBoiler": {
          "cost": "49109 -1275 MBH",
          "param1": 0.61
        },
        "gasWaterBoiler": {
          "cost": "43409 -1088 MBH",
          "param1": 0.93
        },
        "oilSteamBoiler": {
          "cost": "53409 -1360 MBH",
          "param1": 0.61
        },
        "oilWaterBoiler": {
          "cost": "53309 -1168 MBH",
          "param1": 0.93
        }
      },
      "lighting": {
        "LED": {
          "cost": 14000,
          "fixtures": 100,
          "param1": 25
        },
        "LEDCFL": {
          "cost": 7000,
          "fixtures": 100,
          "param1": 29
        },
        "allCFL": {
          "cost": 0,
          "fixtures": 100,
          "param1": 33
        }
      },
      "lightingDimmer": {
        "maximumDimmer": {
          "cost": 8000,
          "param1": 30
        },
        "minimumDimmer": {
          "cost": 0,
          "param1": 0
        }
      },
      "naturalVentilation": {
        "baseline": {
          "cost": 0,
          "param1": 1,
          "param2": 1,
          "param3": 270
        },
        "improve1": {
          "cost": 3460,
          "param1": 2,
          "param2": 1,
          "param3": 270
        },
        "improve2": {
          "cost": 6840,
          "param1": 1,
          "param2": 3,
          "param3": 270
        }
      },
      "opaque1": {
        "baseline": {
          "cost": 0,
          "param1": 0.42,
          "param2": 0.7,
          "param3": 0.6
        },
        "improvement1": {
          "cost": 3460,
          "param1": 0.38,
          "param2": 0.6,
          "param3": 0.7
        },
        "improvement2": {
          "cost": 6840,
          "param1": 0.26,
          "param2": 0.6,
          "param3": 0.8
        }
      },
      "overhangE": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangN": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangNE": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangNW": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangS": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangSE": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangSW": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangW": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "roof1": {
        "baseline": {
          "cost": 0,
          "param1": 0.24,
          "param2": 0.7,
          "param3": 0.6
        },
        "improvement1": {
          "cost": 600,
          "param1": 0.18,
          "param2": 0.6,
          "param3": 0.6
        },
        "improvement2": {
          "cost": 2700,
          "param1": 0.12,
          "param2": 0.5,
          "param3": 0.7
        }
      },
      "solarCollector": {
        "maximum": {
          "cost": 30900,
          "param1": 216
        },
        "minimum": {
          "cost": 9025,
          "param1": 40
        }
      },
      "specificFanPower": {
        "axial": {
          "CFM": 3400,
          "cost": "1470 -3400 CFM",
          "kw": 1000,
          "param1": 623
        },
        "blower": {
          "CFM": 3400,
          "cost": "2305 -3600 CFM",
          "kw": 1000,
          "param1": 623
        },
        "inlineCentrifugal": {
          "CFM": 3400,
          "cost": "1470 -3400 CFM",
          "kw": 1000,
          "param1": 623
        }
      },
      "windTurbine": {
        "maximumDiameter": {
          "cost": 260000,
          "param1": 500
        },
        "minimumDiameter": {
          "cost": 0,
          "param1": 0
        }
      },
      "window1": {
        "baseline": {
          "cost": 0,
          "param1": 2.5,
          "param2": 0.7,
          "param3": 0.5
        },
        "improvement1": {
          "cost": 2140,
          "param1": 1.53,
          "param2": 0.16,
          "param3": 0.2
        },
        "improvement2": {
          "cost": 8700,
          "param1": 1.2,
          "param2": 0.24,
          "param3": 0.2
        }
      },
      "windowSRF_E": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_N": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_NE": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_NW": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_Roof": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_S": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_SE": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_SW": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_W": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      }
    },
    "capxParameters": [
      {
        "data": "Discrete",
        "name": "Heating COP"
      },
      {
        "data": "Discrete",
        "name": "Cooling COP"
      }
    ],
    "capxSettings": {
      "discount_rate": 0.02,
      "electricity_cost": 0.12,
      "energy_del_restriction": 1600,
      "energy_eff_budget": 1000000000000,
      "natural_gas_cost": 0.1,
      "period_analysis": 15
    },
    "ga_settings": {
      "crossover_rate": 0.9,
      "max_time": "1",
      "mutation_rate": 0.2,
      "population_size": "10",
      "random_seed": "None",
      "top_percentage": 10
    },
    "monthly_internal": [],
    "schedule_parameters": [],
    "type": "Calibration"
  },
  "status": "success"
}
```

# /UQ
## methods=['GET' 'PUT'])
**Purpose**: Stores Inputs to run Uncertainty_Analysis.py

**Response**:
```
{
  "UQData": {
    "UQInputs": {
      "UQMode": "Uncertainty Analysis",
      "confidenceLevel": 0.95,
      "energyOutput": "Delivered Energy",
      "numLevels": 4,
      "status": "success",
      "totalSamples": 5
    },
    "UQParams": [],
    "heatParams": []
  },
  "status": "success"
}
```

# /Capx
## methods=['GET'])
**Purpose**: Runs the Capx version of Genetic_Algorithm.py. Return results for graphing.

**Response**:

```
{
  "hourlyXAxis": [
    "8/12/19 4:00 AM",
    "8/12/19 5:00 AM",
    "8/12/19 6:00 AM",
    "8/12/19 7:00 AM",
    "8/12/19 8:00 AM",
    "8/12/19 9:00 AM",
    "8/12/19 10:00 AM",
    "8/12/19 11:00 AM",
    "8/12/19 12:00 PM",
    "8/12/19 1:00 PM",
    "8/12/19 2:00 PM",
    "8/12/19 3:00 PM",
    "8/12/19 4:00 PM",
    "8/12/19 5:00 PM",
    "8/12/19 6:00 PM",
    continues for year ...
  ],
  "interval": "Monthly",
  "modeled": [
    548279.833470471,
    519391.4632677015,
    438379.62687647593,
    480778.0367373598,
    562255.2678830351,
    442707.16008739127,
    481828.6268304521,
    494449.3757052746,
    543255.3731538815,
    515227.70715453895,
    576913.2612426542,
    578383.8428650948
  ],
  "monthlyXAxis": [
    "September",
    "October",
    "November",
    "December",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August"
  ],
  "real": [
    10772.041426895401,
    9415.851044915007,
    8480.132187024046,
    9041.204757297042,
    10391.020232654811,
    8804.338318624397,
    9242.81829752331,
    9305.11136580192,
    11426.745691240745,
    12383.488733500866,
    12644.654785147552,
    13421.939149278702
  ],
  "status": "success"
}
```

# /energystar
## methods=['GET' 'PUT'])
**Purpose**: Runs the Energystar code energystar.py, returns results, and stores the values that are input to run this script. 

**Response**:

```
{
  "build_index": [],
  "estarData": {
    "benchmark": [
      [
        0
      ],
      [
        1
      ]
    ],
    "benchmarkInput": {
      "maxSQFT": 507979,
      "minSQFT": 50000,
      "minYear": 2014
    },
    "score": {
      "adjustedEUI": 0,
      "computers": 2055,
      "coolingDays": 65,
      "dataGrossArea": 37156,
      "grossArea": 507979,
      "heatingDays": 300,
      "officeGrossArea": 470823,
      "percentCooled": 50,
      "predictEUI": 0,
      "score": 0,
      "siteConsumption": 32433503.7,
      "siteEUI": 63.9,
      "sourceConsumption": 90813810.4,
      "sourceEUI": 178.9,
      "weeklyOperation": 61,
      "workers": 546
    },
    "targetScore": {
      "area": 507979,
      "current": 69,
      "target": 72,
      "targetEUI": 0,
      "unit": "kWh",
      "usage": 0
    }
  },
  "status": "success"
}
```

# /graph
## methods=['GET' 'PUT'])
**Purpose**: Returns the outputs from all past runs so that all graphs can be displayed on a single page. 

**Response**:

```
{
  "UQData": {
    "UQInputs": {
      "UQMode": "Uncertainty Analysis",
      "confidenceLevel": 0.95,
      "energyOutput": "Delivered Energy",
      "numLevels": 4,
      "status": "success",
      "totalSamples": 5
    },
    "UQParams": [],
    "heatParams": []
  },
  "build_index": [],
  "calData": {
    "actualGraphData": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "calGraphData": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "calibration_parameters": [],
    "calibration_settings": {
      "convergence_diff": 1e-06,
      "cvrmse_criterion": 2,
      "data_interval": "Monthly",
      "electricity_data": "Yes",
      "n_times_converge": 15,
      "natural_gas_data": "No"
    },
    "capxGraphData": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "capxParameterValues": {
      "DHWGenerationSystem": {
        "VRBoiler": {
          "cost": "43409 -1088 MBH",
          "param1": 0.61
        },
        "coGeneration": {
          "cost": "50000 -b",
          "param1": 0.9
        },
        "districtHeating": {
          "cost": "50000 -b",
          "param1": 0.9
        },
        "electric": {
          "cost": "33734 -1010 MBH",
          "param1": 0.75
        },
        "gasBoiler": {
          "cost": "43409 -1088 MBH",
          "param1": 0.75
        },
        "heatPump": {
          "cost": "52100 -50 ton",
          "param1": 2
        },
        "steam": {
          "cost": "43509 -1023 MBH",
          "param1": 0.61
        }
      },
      "FinE": {
        "fin1": {
          "cost": 0,
          "param1": 0
        },
        "fin2": {
          "cost": 2500,
          "param1": 30
        },
        "fin3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "FinN": {
        "fin1": {
          "cost": 0,
          "param1": 11
        },
        "fin2": {
          "cost": 2500,
          "param1": 8
        },
        "fin3": {
          "cost": 2500,
          "param1": 9
        }
      },
      "FinNE": {
        "fin1": {
          "cost": 0,
          "param1": 0
        },
        "fin2": {
          "cost": 2500,
          "param1": 30
        },
        "fin3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "FinNW": {
        "fin1": {
          "cost": 0,
          "param1": 0
        },
        "fin2": {
          "cost": 2500,
          "param1": 30
        },
        "fin3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "FinS": {
        "fin1": {
          "cost": 0,
          "param1": 11
        },
        "fin2": {
          "cost": 2500,
          "param1": 8
        },
        "fin3": {
          "cost": 2500,
          "param1": 9
        }
      },
      "FinSE": {
        "fin1": {
          "cost": 0,
          "param1": 0
        },
        "fin2": {
          "cost": 2500,
          "param1": 30
        },
        "fin3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "FinSW": {
        "fin1": {
          "cost": 0,
          "param1": 0
        },
        "fin2": {
          "cost": 2500,
          "param1": 30
        },
        "fin3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "FinW": {
        "fin1": {
          "cost": 0,
          "param1": 11
        },
        "fin2": {
          "cost": 2500,
          "param1": 8
        },
        "fin3": {
          "cost": 2500,
          "param1": 9
        }
      },
      "PVModule": {
        "maximum": {
          "cost": 43056,
          "param1": 500
        },
        "minimum": {
          "cost": 0,
          "param1": 0
        }
      },
      "airLeakage": {
        "maximum": {
          "cost": 0,
          "param1": 0
        },
        "minimum": {
          "cost": 0,
          "param1": 0
        }
      },
      "appliance": {
        "eStarBaseline": {
          "cost": 0,
          "param1": 12
        },
        "eStarTop10": {
          "cost": 1350,
          "param1": 20
        },
        "eStarTop5": {
          "cost": 2120,
          "param1": 25
        }
      },
      "coolingEfficiency": {
        "absorptionWaterChiller": {
          "cost": "240300 -148 ton",
          "param1": 1.9
        },
        "centrifugalWaterChiller": {
          "cost": "164300 -400 ton",
          "param1": 7.1
        },
        "reciprocatingAirChiller": {
          "cost": "121600 -150 ton",
          "param1": 2.8
        },
        "reciprocatingWaterChiller": {
          "cost": "106200 -155 ton",
          "param1": 5
        }
      },
      "electricBattery": {
        "baseline": {
          "cost": 0,
          "param1": 150,
          "param2": 0.98,
          "param3": 0.98
        },
        "improve1": {
          "cost": 3460,
          "param1": 200,
          "param2": 0.98,
          "param3": 0.95
        },
        "improve2": {
          "cost": 6840,
          "param1": 250,
          "param2": 0.96,
          "param3": 0.96
        }
      },
      "heatRecovery": {
        "None": {
          "cost": "0 -O GPM",
          "param1": 0
        },
        "heatExchangePipes": {
          "cost": "3550 -1700 CFM",
          "param1": 0.6
        },
        "heatExchangePlates": {
          "cost": "64625 -800 GPM",
          "param1": 0.9
        },
        "rotation": {
          "cost": "2000 -",
          "param1": 0.75
        },
        "twoElement": {
          "cost": "25800 -152 GPM",
          "param1": 0.65
        }
      },
      "heatingCoolingEfficiency": {
        "heatPumpAA": {
          "cost": "11900 -10 ton",
          "param1": 2.05,
          "param2": 2.8
        },
        "heatPumpWA": {
          "cost": "11650 -10 ton",
          "param1": 2.28,
          "param2": 3.21
        }
      },
      "heatingEfficiency": {
        "electricSteamBoiler": {
          "cost": "43509 -1023 MBH",
          "param1": 0.61
        },
        "electricWaterBoiler": {
          "cost": "33734 -1010 MBH",
          "param1": 0.99
        },
        "gasSteamBoiler": {
          "cost": "49109 -1275 MBH",
          "param1": 0.61
        },
        "gasWaterBoiler": {
          "cost": "43409 -1088 MBH",
          "param1": 0.93
        },
        "oilSteamBoiler": {
          "cost": "53409 -1360 MBH",
          "param1": 0.61
        },
        "oilWaterBoiler": {
          "cost": "53309 -1168 MBH",
          "param1": 0.93
        }
      },
      "lighting": {
        "LED": {
          "cost": 14000,
          "fixtures": 100,
          "param1": 25
        },
        "LEDCFL": {
          "cost": 7000,
          "fixtures": 100,
          "param1": 29
        },
        "allCFL": {
          "cost": 0,
          "fixtures": 100,
          "param1": 33
        }
      },
      "lightingDimmer": {
        "maximumDimmer": {
          "cost": 8000,
          "param1": 30
        },
        "minimumDimmer": {
          "cost": 0,
          "param1": 0
        }
      },
      "naturalVentilation": {
        "baseline": {
          "cost": 0,
          "param1": 1,
          "param2": 1,
          "param3": 270
        },
        "improve1": {
          "cost": 3460,
          "param1": 2,
          "param2": 1,
          "param3": 270
        },
        "improve2": {
          "cost": 6840,
          "param1": 1,
          "param2": 3,
          "param3": 270
        }
      },
      "opaque1": {
        "baseline": {
          "cost": 0,
          "param1": 0.42,
          "param2": 0.7,
          "param3": 0.6
        },
        "improvement1": {
          "cost": 3460,
          "param1": 0.38,
          "param2": 0.6,
          "param3": 0.7
        },
        "improvement2": {
          "cost": 6840,
          "param1": 0.26,
          "param2": 0.6,
          "param3": 0.8
        }
      },
      "overhangE": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangN": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangNE": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangNW": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangS": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangSE": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangSW": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangW": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "roof1": {
        "baseline": {
          "cost": 0,
          "param1": 0.24,
          "param2": 0.7,
          "param3": 0.6
        },
        "improvement1": {
          "cost": 600,
          "param1": 0.18,
          "param2": 0.6,
          "param3": 0.6
        },
        "improvement2": {
          "cost": 2700,
          "param1": 0.12,
          "param2": 0.5,
          "param3": 0.7
        }
      },
      "solarCollector": {
        "maximum": {
          "cost": 30900,
          "param1": 216
        },
        "minimum": {
          "cost": 9025,
          "param1": 40
        }
      },
      "specificFanPower": {
        "axial": {
          "CFM": 3400,
          "cost": "1470 -3400 CFM",
          "kw": 1000,
          "param1": 623
        },
        "blower": {
          "CFM": 3400,
          "cost": "2305 -3600 CFM",
          "kw": 1000,
          "param1": 623
        },
        "inlineCentrifugal": {
          "CFM": 3400,
          "cost": "1470 -3400 CFM",
          "kw": 1000,
          "param1": 623
        }
      },
      "windTurbine": {
        "maximumDiameter": {
          "cost": 260000,
          "param1": 500
        },
        "minimumDiameter": {
          "cost": 0,
          "param1": 0
        }
      },
      "window1": {
        "baseline": {
          "cost": 0,
          "param1": 2.5,
          "param2": 0.7,
          "param3": 0.5
        },
        "improvement1": {
          "cost": 2140,
          "param1": 1.53,
          "param2": 0.16,
          "param3": 0.2
        },
        "improvement2": {
          "cost": 8700,
          "param1": 1.2,
          "param2": 0.24,
          "param3": 0.2
        }
      },
      "windowSRF_E": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_N": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_NE": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_NW": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_Roof": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_S": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_SE": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_SW": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_W": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      }
    },
    "capxParameters": [
      {
        "data": "Discrete",
        "name": "Heating COP"
      },
      {
        "data": "Discrete",
        "name": "Cooling COP"
      }
    ],
    "capxSettings": {
      "discount_rate": 0.02,
      "electricity_cost": 0.12,
      "energy_del_restriction": 1600,
      "energy_eff_budget": 1000000000000,
      "natural_gas_cost": 0.1,
      "period_analysis": 15
    },
    "ga_settings": {
      "crossover_rate": 0.9,
      "max_time": "1",
      "mutation_rate": 0.2,
      "population_size": "10",
      "random_seed": "None",
      "top_percentage": 10
    },
    "monthly_internal": [],
    "schedule_parameters": [],
    "type": "CapX"
  },
  "capxData": [
    {
      "data": "Continuous",
      "name": "Heating COP"
    }
  ],
  "estarData": {
    "benchmark": [
      [
        0
      ],
      [
        1
      ]
    ],
    "benchmarkInput": {
      "maxSQFT": 507979,
      "minSQFT": 50000,
      "minYear": 2014
    },
    "score": {
      "adjustedEUI": 0,
      "computers": 2055,
      "coolingDays": 65,
      "dataGrossArea": 37156,
      "grossArea": 507979,
      "heatingDays": 300,
      "officeGrossArea": 470823,
      "percentCooled": 50,
      "predictEUI": 0,
      "score": 0,
      "siteConsumption": 32433503.7,
      "siteEUI": 63.9,
      "sourceConsumption": 90813810.4,
      "sourceEUI": 178.9,
      "weeklyOperation": 61,
      "workers": 546
    },
    "targetScore": {
      "area": 507979,
      "current": 69,
      "target": 72,
      "targetEUI": 0,
      "unit": "kWh",
      "usage": 0
    }
  },
  "inputData": {
    "historicalData1": "BEM_Optimization_Input_centergy.xlsx",
    "historicalData2": "BEM_Optimization_Input_centergy.xlsx",
    "jsonData": {
      "AirLeakageLevel": 2,
      "BEMType": 2,
      "COP100": 1,
      "COP25": 0.5,
      "COP50": 0.82,
      "COP75": 0.9,
      "COPWeighting100": 0.01,
      "COPWeighting25": 0.12,
      "COPWeighting50": 0.45,
      "COPWeighting75": 0.42,
      "CoolingCOP": 4.6836437236367265,
      "CoolingEnergySource": "Electricity",
      "DHWDistrinutionSystem": "Taps More Than 3m from Heat Generation",
      "DHWEnergySource": "Electricity",
      "DHWGenerationSystem": "Electric (0.75)",
      "DaylightingFactor": 1,
      "ElectricBattery": {
        "Capacity": 0,
        "ChargingEfficiency": 0,
        "ChargingPowerLimit": 0,
        "DischargingEfficiency": 0,
        "DischargingPowerLimit": 0
      },
      "ElectricVehicle": {
        "ChargingPower": 0,
        "Hour1": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour10": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour11": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour12": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour13": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour14": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour15": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour16": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour17": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour18": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour19": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour2": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour20": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour21": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour22": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour23": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour24": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour3": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour4": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour5": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour6": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour7": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour8": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour9": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "No_EVCharger": 0
      },
      "Electricity": {
        "CO2EmissionCoefficient": 744,
        "PrimaryEnergyFactor": 3.39
      },
      "Envelope": {
        "Opaque1": {
          "BelowGrade": {
            "Area": 3077.89
          },
          "E": {
            "Area": 1969.91
          },
          "N": {
            "Area": 2671.02
          },
          "NE": {
            "Area": 0
          },
          "NW": {
            "Area": 0
          },
          "Roof": {
            "Area": 5852.89
          },
          "S": {
            "Area": 2671.02
          },
          "SE": {
            "Area": 0
          },
          "SW": {
            "Area": 0
          },
          "W": {
            "Area": 1872.91
          }
        },
        "Window1": {
          "BelowGrade": {
            "Area": 0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 0
          },
          "E": {
            "Area": 1456,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 0.4905
          },
          "N": {
            "Area": 1975.7,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 0.4905
          },
          "NE": {
            "Area": 0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 1
          },
          "NW": {
            "Area": 0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 1
          },
          "Roof": {
            "Area": 0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 1
          },
          "S": {
            "Area": 1975.7,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 0.4905
          },
          "SE": {
            "Area": 0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 1
          },
          "SW": {
            "Area": 0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 1
          },
          "W": {
            "Area": 1378,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 0.4905
          }
        }
      },
      "ExhaustAirRecirculation": "Exhaust air recirculation  60%",
      "ExtraVentilation": 0,
      "FanControlFactor": 0.65,
      "Fuel": {
        "CO2EmissionCoefficient": 330,
        "PrimaryEnergyFactor": 1.19
      },
      "Garage": {
        "Appliance": 2,
        "Lighting": 8,
        "Occupancy": 0,
        "SpaceName": ""
      },
      "Garage_Schedule": {
        "Hour1": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour10": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour11": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour12": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour13": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour14": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour15": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour16": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour17": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour18": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour19": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour2": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour20": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour21": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour22": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour23": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour24": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour3": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour4": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour5": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour6": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour7": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour8": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour9": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        }
      },
      "HVACSystemType": "22. Variable air volume / Water or Water&Air / Water / Yes",
      "HeatCapacity": "Heavy: 260,000 * Af",
      "HeatRecoveryType": "Slowly rotating or intermittent heat exchangers (0.7)",
      "HeatingCOP": 0.7452668159525578,
      "HeatingEnergySource": "Electricity",
      "Height": 52,
      "LightingControlFactor": 1,
      "LightingDimmer": {
        "DimmerSaving_WD": 0,
        "DimmerSaving_WE": 0
      },
      "Material": {
        "Opaque1": {
          "Absorptivity": 0.7,
          "Emissivity": 0.92,
          "UValue": 0.37840367791539986
        },
        "Roof1": {
          "Absorptivity": 0.85,
          "Emissivity": 0.7929518053345709,
          "UValue": 0.21
        },
        "Window1": {
          "Emissivity": -0.036142153396077986,
          "SolarTrasmittance": 0.41,
          "UValue": 0.2935935299380026
        }
      },
      "Name": "Building_Name",
      "NaturalGas": {
        "CO2EmissionCoefficient": 277,
        "PrimaryEnergyFactor": 1.09
      },
      "NaturalVentilation": {
        "EffectiveAngle": 0,
        "Height": 0,
        "Width": 0
      },
      "OccupancyFactor": 1,
      "OutputPeriod": "Monthly",
      "PVArea": 0,
      "PVOrientation": "S",
      "PVPeakPower": 0.15,
      "PVPerformanceFactor": 0.7,
      "PVTiltAngle": 30,
      "ParasiticLightingEnergy": "Yes",
      "ParasiticLightingEnergyAmount": 6,
      "PumpCoolingControl": "All other cases",
      "PumpHeatingControl": "All other cases",
      "RHThreshold": 75,
      "RetailRefrig": {
        "Capacity": 0,
        "Zone": ""
      },
      "SHWArea": 0,
      "SHWEfficiency": 0.5,
      "SHWOrientation": "S",
      "SHWTiltAngle": 30,
      "SpecificFanPower": 2.5,
      "StartDay": "Tuesday",
      "TemperatureSetPoint": {
        "Hour1": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour10": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour11": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour12": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour13": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour14": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour15": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour16": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour17": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour18": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour19": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour2": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour20": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour21": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour22": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour23": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour24": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour3": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour4": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour5": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour6": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour7": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour8": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour9": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        }
      },
      "TerrainClass": "Urban / City",
      "VentilationCoolingType": "1. Mechanical system only; no provision for natural ventilation",

      "Volume": 198218,
      "WindTurbineDiameter": 0,
      "WindTurbineEfficiency": 0.4,
      "Zone1": {
        "Appliance": 13.099276456946004,
        "DHW": 4.1,
        "GrossFloorArea": 43213.11,
        "Lighting": 10.27254555831506,
        "MatabolicRate": 105,
        "Occupancy": 30.91,
        "OutdoorAir": 8.33,
        "SpaceName": "Space_Nm"
      },
      "Zone1_Schedule": {
        "Hour1": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour10": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour11": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour12": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour13": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour14": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour15": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour16": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour17": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour18": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour19": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour2": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour20": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour21": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour22": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour23": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour24": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour3": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour4": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour5": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour6": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour7": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour8": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour9": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        }
      }
    },
    "weatherData": "Atlanta_TMY3.epw"
  },
  "interval": [],
  "modeled": [],
  "monthly": [
    597461.3710946427,
    554394.9932013091,
    464793.168906857,
    512953.3581184808,
    616330.3467880326,
    468564.30711223895,
    510833.1881238521,
    524711.9364277617,
    584663.0103323687,
    555621.0517085561,
    627265.3002421116,
    629105.7039985397
  ],
  "real": [],
  "runUQData": {
    "firstGraphDataSA": [
      0
    ],
    "firstGraphDataUA": [
      0
    ],
    "firstGraphNamesSA": "null",
    "firstGraphNamesUA": "null",
    "secondGraphDataSA": [
      0
    ],
    "secondGraphDataUA": [
      0
    ],
    "secondGraphNamesSA": "null",
    "secondGraphNamesUA": "null"
  },
  "status": "success",
  "subs": [
    [
      13893.54349969737
    ],
    [
      23396.786201826802
    ],
    [
      39475.18596198799
    ],
    [
      16837.50610090771
    ],
    [
      4478.0823731956025
    ],
    [
      54441.11692612588
    ],
    [
      4796.585981989138
    ],
    [
      0.0
    ],
    [
      0.0
    ],
    [
      0.0
    ],
    [
      157318.80704573047
    ],
    [
      0.0
    ]
  ]
}
```

# /loadProject
## methods=['GET' 'PUT'])
**Purpose**: Stores the Input Values from the Input Page, UQ Page, and Cal / CapX page so that they can be saved and rerun. 

**Response**:
```
{
  "UQData": {
    "UQInputs": {
      "UQMode": "Uncertainty Analysis",
      "confidenceLevel": 0.95,
      "energyOutput": "Delivered Energy",
      "numLevels": 4,
      "status": "success",
      "totalSamples": 5
    },
    "UQParams": [],
    "heatParams": []
  },
  "calData": {
    "actualGraphData": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "calGraphData": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "calibration_parameters": [],
    "calibration_settings": {
      "convergence_diff": 1e-06,
      "cvrmse_criterion": 2,
      "data_interval": "Monthly",
      "electricity_data": "Yes",
      "n_times_converge": 15,
      "natural_gas_data": "No"
    },
    "capxGraphData": [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "capxParameterValues": {
      "DHWGenerationSystem": {
        "VRBoiler": {
          "cost": "43409 -1088 MBH",
          "param1": 0.61
        },
        "coGeneration": {
          "cost": "50000 -b",
          "param1": 0.9
        },
        "districtHeating": {
          "cost": "50000 -b",
          "param1": 0.9
        },
        "electric": {
          "cost": "33734 -1010 MBH",
          "param1": 0.75
        },
        "gasBoiler": {
          "cost": "43409 -1088 MBH",
          "param1": 0.75
        },
        "heatPump": {
          "cost": "52100 -50 ton",
          "param1": 2
        },
        "steam": {
          "cost": "43509 -1023 MBH",
          "param1": 0.61
        }
      },
      "FinE": {
        "fin1": {
          "cost": 0,
          "param1": 0
        },
        "fin2": {
          "cost": 2500,
          "param1": 30
        },
        "fin3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "FinN": {
        "fin1": {
          "cost": 0,
          "param1": 11
        },
        "fin2": {
          "cost": 2500,
          "param1": 8
        },
        "fin3": {
          "cost": 2500,
          "param1": 9
        }
      },
      "FinNE": {
        "fin1": {
          "cost": 0,
          "param1": 0
        },
        "fin2": {
          "cost": 2500,
          "param1": 30
        },
        "fin3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "FinNW": {
        "fin1": {
          "cost": 0,
          "param1": 0
        },
        "fin2": {
          "cost": 2500,
          "param1": 30
        },
        "fin3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "FinS": {
        "fin1": {
          "cost": 0,
          "param1": 11
        },
        "fin2": {
          "cost": 2500,
          "param1": 8
        },
        "fin3": {
          "cost": 2500,
          "param1": 9
        }
      },
      "FinSE": {
        "fin1": {
          "cost": 0,
          "param1": 0
        },
        "fin2": {
          "cost": 2500,
          "param1": 30
        },
        "fin3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "FinSW": {
        "fin1": {
          "cost": 0,
          "param1": 0
        },
        "fin2": {
          "cost": 2500,
          "param1": 30
        },
        "fin3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "FinW": {
        "fin1": {
          "cost": 0,
          "param1": 11
        },
        "fin2": {
          "cost": 2500,
          "param1": 8
        },
        "fin3": {
          "cost": 2500,
          "param1": 9
        }
      },
      "PVModule": {
        "maximum": {
          "cost": 43056,
          "param1": 500
        },
        "minimum": {
          "cost": 0,
          "param1": 0
        }
      },
      "airLeakage": {
        "maximum": {
          "cost": 0,
          "param1": 0
        },
        "minimum": {
          "cost": 0,
          "param1": 0
        }
      },
      "appliance": {
        "eStarBaseline": {
          "cost": 0,
          "param1": 12
        },
        "eStarTop10": {
          "cost": 1350,
          "param1": 20
        },
        "eStarTop5": {
          "cost": 2120,
          "param1": 25
        }
      },
      "coolingEfficiency": {
        "absorptionWaterChiller": {
          "cost": "240300 -148 ton",
          "param1": 1.9
        },
        "centrifugalWaterChiller": {
          "cost": "164300 -400 ton",
          "param1": 7.1
        },
        "reciprocatingAirChiller": {
          "cost": "121600 -150 ton",
          "param1": 2.8
        },
        "reciprocatingWaterChiller": {
          "cost": "106200 -155 ton",
          "param1": 5
        }
      },
      "electricBattery": {
        "baseline": {
          "cost": 0,
          "param1": 150,
          "param2": 0.98,
          "param3": 0.98
        },
        "improve1": {
          "cost": 3460,
          "param1": 200,
          "param2": 0.98,
          "param3": 0.95
        },
        "improve2": {
          "cost": 6840,
          "param1": 250,
          "param2": 0.96,
          "param3": 0.96
        }
      },
      "heatRecovery": {
        "None": {
          "cost": "0 -O GPM",
          "param1": 0
        },
        "heatExchangePipes": {
          "cost": "3550 -1700 CFM",
          "param1": 0.6
        },
        "heatExchangePlates": {
          "cost": "64625 -800 GPM",
          "param1": 0.9
        },
        "rotation": {
          "cost": "2000 -",
          "param1": 0.75
        },
        "twoElement": {
          "cost": "25800 -152 GPM",
          "param1": 0.65
        }
      },
      "heatingCoolingEfficiency": {
        "heatPumpAA": {
          "cost": "11900 -10 ton",
          "param1": 2.05,
          "param2": 2.8
        },
        "heatPumpWA": {
          "cost": "11650 -10 ton",
          "param1": 2.28,
          "param2": 3.21
        }
      },
      "heatingEfficiency": {
        "electricSteamBoiler": {
          "cost": "43509 -1023 MBH",
          "param1": 0.61
        },
        "electricWaterBoiler": {
          "cost": "33734 -1010 MBH",
          "param1": 0.99
        },
        "gasSteamBoiler": {
          "cost": "49109 -1275 MBH",
          "param1": 0.61
        },
        "gasWaterBoiler": {
          "cost": "43409 -1088 MBH",
          "param1": 0.93
        },
        "oilSteamBoiler": {
          "cost": "53409 -1360 MBH",
          "param1": 0.61
        },
        "oilWaterBoiler": {
          "cost": "53309 -1168 MBH",
          "param1": 0.93
        }
      },
      "lighting": {
        "LED": {
          "cost": 14000,
          "fixtures": 100,
          "param1": 25
        },
        "LEDCFL": {
          "cost": 7000,
          "fixtures": 100,
          "param1": 29
        },
        "allCFL": {
          "cost": 0,
          "fixtures": 100,
          "param1": 33
        }
      },
      "lightingDimmer": {
        "maximumDimmer": {
          "cost": 8000,
          "param1": 30
        },
        "minimumDimmer": {
          "cost": 0,
          "param1": 0
        }
      },
      "naturalVentilation": {
        "baseline": {
          "cost": 0,
          "param1": 1,
          "param2": 1,
          "param3": 270
        },
        "improve1": {
          "cost": 3460,
          "param1": 2,
          "param2": 1,
          "param3": 270
        },
        "improve2": {
          "cost": 6840,
          "param1": 1,
          "param2": 3,
          "param3": 270
        }
      },
      "opaque1": {
        "baseline": {
          "cost": 0,
          "param1": 0.42,
          "param2": 0.7,
          "param3": 0.6
        },
        "improvement1": {
          "cost": 3460,
          "param1": 0.38,
          "param2": 0.6,
          "param3": 0.7
        },
        "improvement2": {
          "cost": 6840,
          "param1": 0.26,
          "param2": 0.6,
          "param3": 0.8
        }
      },
      "overhangE": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangN": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangNE": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangNW": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangS": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangSE": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangSW": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "overhangW": {
        "overhang1": {
          "cost": 0,
          "param1": 0
        },
        "overhang2": {
          "cost": 2500,
          "param1": 30
        },
        "overhang3": {
          "cost": 2500,
          "param1": 45
        }
      },
      "roof1": {
        "baseline": {
          "cost": 0,
          "param1": 0.24,
          "param2": 0.7,
          "param3": 0.6
        },
        "improvement1": {
          "cost": 600,
          "param1": 0.18,
          "param2": 0.6,
          "param3": 0.6
        },
        "improvement2": {
          "cost": 2700,
          "param1": 0.12,
          "param2": 0.5,
          "param3": 0.7
        }
      },
      "solarCollector": {
        "maximum": {
          "cost": 30900,
          "param1": 216
        },
        "minimum": {
          "cost": 9025,
          "param1": 40
        }
      },
      "specificFanPower": {
        "axial": {
          "CFM": 3400,
          "cost": "1470 -3400 CFM",
          "kw": 1000,
          "param1": 623
        },
        "blower": {
          "CFM": 3400,
          "cost": "2305 -3600 CFM",
          "kw": 1000,
          "param1": 623
        },
        "inlineCentrifugal": {
          "CFM": 3400,
          "cost": "1470 -3400 CFM",
          "kw": 1000,
          "param1": 623
        }
      },
      "windTurbine": {
        "maximumDiameter": {
          "cost": 260000,
          "param1": 500
        },
        "minimumDiameter": {
          "cost": 0,
          "param1": 0
        }
      },
      "window1": {
        "baseline": {
          "cost": 0,
          "param1": 2.5,
          "param2": 0.7,
          "param3": 0.5
        },
        "improvement1": {
          "cost": 2140,
          "param1": 1.53,
          "param2": 0.16,
          "param3": 0.2
        },
        "improvement2": {
          "cost": 8700,
          "param1": 1.2,
          "param2": 0.24,
          "param3": 0.2
        }
      },
      "windowSRF_E": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_N": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_NE": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_NW": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_Roof": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_S": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_SE": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_SW": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      },
      "windowSRF_W": {
        "maximumSRF": {
          "cost": 8000,
          "param1": 0.6
        },
        "minimumSRF": {
          "cost": 0,
          "param1": 0
        }
      }
    },
    "capxParameters": [
      {
        "data": "Discrete",
        "name": "Heating COP"
      },
      {
        "data": "Discrete",
        "name": "Cooling COP"
      }
    ],
    "capxSettings": {
      "discount_rate": 0.02,
      "electricity_cost": 0.12,
      "energy_del_restriction": 1600,
      "energy_eff_budget": 1000000000000,
      "natural_gas_cost": 0.1,
      "period_analysis": 15
    },
    "ga_settings": {
      "crossover_rate": 0.9,
      "max_time": "1",
      "mutation_rate": 0.2,
      "population_size": "10",
      "random_seed": "None",
      "top_percentage": 10
    },
    "monthly_internal": [],
    "schedule_parameters": [],
    "type": "CapX"
  },
  "estarData": {
    "benchmark": [
      [
        0
      ],
      [
        1
      ]
    ],
    "benchmarkInput": {
      "maxSQFT": 507979,
      "minSQFT": 50000,
      "minYear": 2014
    },
    "score": {
      "adjustedEUI": 0,
      "computers": 2055,
      "coolingDays": 65,
      "dataGrossArea": 37156,
      "grossArea": 507979,
      "heatingDays": 300,
      "officeGrossArea": 470823,
      "percentCooled": 50,
      "predictEUI": 0,
      "score": 0,
      "siteConsumption": 32433503.7,
      "siteEUI": 63.9,
      "sourceConsumption": 90813810.4,
      "sourceEUI": 178.9,
      "weeklyOperation": 61,
      "workers": 546
    },
    "targetScore": {
      "area": 507979,
      "current": 69,
      "target": 72,
      "targetEUI": 0,
      "unit": "kWh",
      "usage": 0
    }
  },
  "inputData": {
    "historicalData1": "BEM_Optimization_Input_centergy.xlsx",
    "historicalData2": "BEM_Optimization_Input_centergy.xlsx",
    "jsonData": {
      "AirLeakageLevel": 2,
      "BEMType": 2,
      "COP100": 1,
      "COP25": 0.5,
      "COP50": 0.82,
      "COP75": 0.9,
      "COPWeighting100": 0.01,
      "COPWeighting25": 0.12,
      "COPWeighting50": 0.45,
      "COPWeighting75": 0.42,
      "CoolingCOP": 4.6836437236367265,
      "CoolingEnergySource": "Electricity",
      "DHWDistrinutionSystem": "Taps More Than 3m from Heat Generation",
      "DHWEnergySource": "Electricity",
      "DHWGenerationSystem": "Electric (0.75)",
      "DaylightingFactor": 1,
      "ElectricBattery": {
        "Capacity": 0,
        "ChargingEfficiency": 0,
        "ChargingPowerLimit": 0,
        "DischargingEfficiency": 0,
        "DischargingPowerLimit": 0
      },
      "ElectricVehicle": {
        "ChargingPower": 0,
        "Hour1": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour10": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour11": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour12": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour13": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour14": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour15": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour16": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour17": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour18": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour19": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour2": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour20": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour21": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour22": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour23": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour24": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour3": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour4": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour5": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour6": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour7": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour8": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "Hour9": {
          "EV_Weekday": 0,
          "EV_Weekend": 0
        },
        "No_EVCharger": 0
      },
      "Electricity": {
        "CO2EmissionCoefficient": 744,
        "PrimaryEnergyFactor": 3.39
      },
      "Envelope": {
        "Opaque1": {
          "BelowGrade": {
            "Area": 3077.89
          },
          "E": {
            "Area": 1969.91
          },
          "N": {
            "Area": 2671.02
          },
          "NE": {
            "Area": 0
          },
          "NW": {
            "Area": 0
          },
          "Roof": {
            "Area": 5852.89
          },
          "S": {
            "Area": 2671.02
          },
          "SE": {
            "Area": 0
          },
          "SW": {
            "Area": 0
          },
          "W": {
            "Area": 1872.91
          }
        },
        "Window1": {
          "BelowGrade": {
            "Area": 0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 0
          },
          "E": {
            "Area": 1456,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 0.4905
          },
          "N": {
            "Area": 1975.7,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 0.4905
          },
          "NE": {
            "Area": 0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 1
          },
          "NW": {
            "Area": 0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 1
          },
          "Roof": {
            "Area": 0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 1
          },
          "S": {
            "Area": 1975.7,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 0.4905
          },
          "SE": {
            "Area": 0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 1
          },
          "SW": {
            "Area": 0,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 1
          },
          "W": {
            "Area": 1378,
            "FinAngle": 0,
            "HorizonAngle": 0,
            "OverhangAngle": 0,
            "SRF": 0.4905
          }
        }
      },
      "ExhaustAirRecirculation": "Exhaust air recirculation  60%",
      "ExtraVentilation": 0,
      "FanControlFactor": 0.65,
      "Fuel": {
        "CO2EmissionCoefficient": 330,
        "PrimaryEnergyFactor": 1.19
      },
      "Garage": {
        "Appliance": 2,
        "Lighting": 8,
        "Occupancy": 0,
        "SpaceName": ""
      },
      "Garage_Schedule": {
        "Hour1": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour10": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour11": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour12": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour13": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour14": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour15": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour16": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour17": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour18": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour19": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour2": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour20": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour21": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour22": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour23": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour24": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour3": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour4": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour5": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour6": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour7": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour8": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        },
        "Hour9": {
          "Appliance_Weekday": 0,
          "Appliance_Weekend": 0,
          "Lighting_Weekday": 0,
          "Lighting_Weekend": 0
        }
      },
      "HVACSystemType": "22. Variable air volume / Water or Water&Air / Water / Yes",
      "HeatCapacity": "Heavy: 260,000 * Af",
      "HeatRecoveryType": "Slowly rotating or intermittent heat exchangers (0.7)",
      "HeatingCOP": 0.7452668159525578,
      "HeatingEnergySource": "Electricity",
      "Height": 52,
      "LightingControlFactor": 1,
      "LightingDimmer": {
        "DimmerSaving_WD": 0,
        "DimmerSaving_WE": 0
      },
      "Material": {
        "Opaque1": {
          "Absorptivity": 0.7,
          "Emissivity": 0.92,
          "UValue": 0.37840367791539986
        },
        "Roof1": {
          "Absorptivity": 0.85,
          "Emissivity": 0.7929518053345709,
          "UValue": 0.21
        },
        "Window1": {
          "Emissivity": -0.036142153396077986,
          "SolarTrasmittance": 0.41,
          "UValue": 0.2935935299380026
        }
      },
      "Name": "Building_Name",
      "NaturalGas": {
        "CO2EmissionCoefficient": 277,
        "PrimaryEnergyFactor": 1.09
      },
      "NaturalVentilation": {
        "EffectiveAngle": 0,
        "Height": 0,
        "Width": 0
      },
      "OccupancyFactor": 1,
      "OutputPeriod": "Monthly",
      "PVArea": 0,
      "PVOrientation": "S",
      "PVPeakPower": 0.15,
      "PVPerformanceFactor": 0.7,
      "PVTiltAngle": 30,
      "ParasiticLightingEnergy": "Yes",
      "ParasiticLightingEnergyAmount": 6,
      "PumpCoolingControl": "All other cases",
      "PumpHeatingControl": "All other cases",
      "RHThreshold": 75,
      "RetailRefrig": {
        "Capacity": 0,
        "Zone": ""
      },
      "SHWArea": 0,
      "SHWEfficiency": 0.5,
      "SHWOrientation": "S",
      "SHWTiltAngle": 30,
      "SpecificFanPower": 2.5,
      "StartDay": "Tuesday",
      "TemperatureSetPoint": {
        "Hour1": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour10": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour11": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour12": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour13": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour14": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour15": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour16": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour17": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour18": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour19": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour2": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour20": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour21": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour22": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour23": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour24": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour3": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour4": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour5": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour6": {
          "Cooling_Weekday": 25.6,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 18.9,
          "Heating_Weekend": 18.9
        },
        "Hour7": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour8": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        },
        "Hour9": {
          "Cooling_Weekday": 22.8,
          "Cooling_Weekend": 25.6,
          "Heating_Weekday": 22.8,
          "Heating_Weekend": 18.9
        }
      },
      "TerrainClass": "Urban / City",
      "VentilationCoolingType": "1. Mechanical system only; no provision for natural ventilation",

      "Volume": 198218,
      "WindTurbineDiameter": 0,
      "WindTurbineEfficiency": 0.4,
      "Zone1": {
        "Appliance": 13.099276456946004,
        "DHW": 4.1,
        "GrossFloorArea": 43213.11,
        "Lighting": 10.27254555831506,
        "MatabolicRate": 105,
        "Occupancy": 30.91,
        "OutdoorAir": 8.33,
        "SpaceName": "Space_Nm"
      },
      "Zone1_Schedule": {
        "Hour1": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour10": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour11": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour12": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour13": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour14": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour15": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour16": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour17": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour18": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        },
        "Hour19": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour2": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour20": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour21": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour22": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour23": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour24": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour3": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour4": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour5": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour6": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour7": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.1,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour8": {
          "Appliance_Weekday": 0.26,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 0.1,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 0.1,
          "Occupancy_Weekend": 0.1
        },
        "Hour9": {
          "Appliance_Weekday": 1,
          "Appliance_Weekend": 0.26,
          "Lighting_Weekday": 1,
          "Lighting_Weekend": 0.25,
          "Occupancy_Weekday": 1,
          "Occupancy_Weekend": 0.3
        }
      }
    },
    "weatherData": "Atlanta_TMY3.epw"
  },
  "status": "success"
}
```

# /runZero
## methods=['GET' 'PUT'])
**Purpose**: Stores the input values, runs, and returns output of zero_order_model.py. 

**Response**:

```
{
  "chosenZeroModel": "data_tep.csv",
  "error": 38.14547328923108,
  "estimatedCost": 66929.22
}
```
