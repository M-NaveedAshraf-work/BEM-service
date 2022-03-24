from BEMP import Hourly_BEM_JSON
# from CPython.BEMP import Hourly_BEM_JSON
from CSV_to_JSON import json_Insance_Generation
import numpy as np
import time

# app = Flask(__name__)
# app.config.from_object(__name__)
# CORS(app, resources={r'/*': {'origins': '*'}})
#
# @app.route('/ping', methods=['GET'])
# def ping_pong():
#     return "<p>Hello, World</p>"

np.set_printoptions(linewidth=2000); np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

def main(mode, building_name, epw_file_name, original_file_name = None, result_file_name = None): # mode i) simulaiton ii) calibration iii) UQ
    # 0. Generate json instance from CSV file
    # json_Insance_Generation("".join(["./Input/", building_name[:-4], "csv"]))

    # 1. Conduct the climnate calculation
    print("The climate calculation has initiated.\n")
    try:
        partial_name = "".join(["./Weather/",epw_file_name[:-4],"_"])
        climate_data = np.load("".join([partial_name, "climate.npy"]))
        solar_30     = np.load("".join([partial_name, "Esol_30.npy"]))
        solar_45     = np.load("".join([partial_name, "Esol_45.npy"]))
        solar_60     = np.load("".join([partial_name, "Esol_60.npy"]))
        solar_90     = np.load("".join([partial_name, "Esol_90.npy"]))
        overhang     = np.load("".join([partial_name, "SRF_overhang.npy"]))
        fin          = np.load("".join([partial_name, "SRF_fin.npy"]))
        horizon      = np.load("".join([partial_name, "SRF_horizon.npy"]))
        del partial_name
    except:
        from Weather import Climate
        climate_instance = Climate.ClimateCalculator(epw_file_name)
        climate_data, solar_30, solar_45, solar_60, solar_90, overhang, fin, horizon = climate_instance.ClimateCalculation()

    # 2. Conduct BEM calculation
    """
    hourly_delivered_energy (W/m2): The hourly results in the Excel BEM in the "CALC_H" 
                            column: 0th: heating energy,  1st: cooling, 2nd: light, 3rd: fan, 4th: pump, 5th: equipment, 6th: DHW, 7th: EV 8th: PV, 9th: wind, 10th: Etotal
    sum_delivered_energy (float: kWh/m2/yr): Yearly delivered energy.
    energy_use_by_fuel (kWh): energy use by fuel.
                              column 0th: Electricity, 1st: Natural gas, 2nd Fuel
    """
    print("The BEM calculation has initiated.\n")

    if mode == "simulation":
        startTime = time.time()
        # hourly_delivered_energy, sum_delivered_energy, energy_use_by_fuel = Hourly_BEM_JSON("".join(["./Input/",building_name]), climate_data, overhang, fin, horizon, solar_30, solar_45, solar_60, solar_90)
        outcome, outcome2, outcome3, grouped = Hourly_BEM_JSON(
            building_name, climate_data, overhang, fin, horizon, solar_30, solar_45, solar_60, solar_90)

        executionTime = (time.time() - startTime)
        print(f'Execution time in seconds: {executionTime}')

        return outcome, outcome2, outcome3, grouped

    elif mode in ["calibration", "capX"]:
        from Genetic_Algorithm import BEMP_Optimization
        # BEMP_Optimization("".join(["./Input/",building_name]), climate_data, overhang, fin, horizon, solar_30, solar_45, solar_60, solar_90, original_file_name, result_file_name)
        real, simulated, interval = BEMP_Optimization(building_name, climate_data, overhang, fin, horizon, solar_30,
                          solar_45, solar_60, solar_90, original_file_name, result_file_name)

        return real, simulated, interval

    elif mode == "UQ":
        from Uncertainty_Analysis import UQ
        UQ("".join(["./Input/",building_name]), climate_data, overhang, fin, horizon, solar_30, solar_45, solar_60, solar_90, graph=True)

    else:
        raise Exception("Please check the mode input")


if __name__ == '__main__':
    # Execute the normal simulation

    # delivered_energy, sum_delivered_energy, energy_use_by_fuel = main(mode="simulation", building_name="centergy_BEM_2019.json", epw_file_name="centergy_2019_epw_file.epw")
    # Execute the calibration
    # main(mode="calibration", building_name="centergy_BEM_2019.json", epw_file_name="centergy_2019_epw_file.epw", original_file_name = "centergy_BEM_2019", result_file_name = "iteration1")
    # main(mode="calibration", building_name="park_center_2019_updated.json", epw_file_name="park_center_2019_epw_file.epw",original_file_name = "park_center_2019_best", result_file_name = "iteration1")

    # Execute UQ
    main(mode="UQ", building_name="centergy_BEM_2019.json", epw_file_name="Atlanta_TMY3.epw")



# ' -   '

# i: 19, j: 13, k:16