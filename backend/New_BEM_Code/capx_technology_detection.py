import pandas as pd
import numpy as np
import dask
import dask.dataframe as dd
from dask.distributed import Client

def load_tech(heat_BTU, cool_BTU, SDHV, DHW_BTU, Vol, CH_Bool):

    # Setting Up Dask Client
    # pd.set_option('display.max_colwidth', None, 'display.max_rows', None, 'display.max_columns', None)
    client = Client(n_workers=1, threads_per_worker=4, processes=True, memory_limit="2GB")
    client
    print(client.dashboard_link)

    # Loading Data into Dask and Assigning New Column Names
    furnace_com_warm_air = dd.read_csv("./Input/furnace_commercial_warm_air.csv", header=0)
    furnace_com_warm_air.columns = ['Brand', 'Description', 'Basic Model Number', 'Ind. Model Number', 'Btu/h', 'Efficiency',
                                    'Test Procedure', 'Hearing and Appeals', 'AEDM']
    furnace = dd.read_csv("./Input/furnaces.csv", dtype={'Ignition_Type__Optional__s': 'object'})
    furnace.columns = ['Brand', 'Description', 'Basic Model Number', 'Ind. Model Number', 'Btu/h', 'Ignition Type',
                       'Efficiency', 'Test Procedure', 'Hearing and Appeals', 'Link']
    furnace['Ignition Type'].astype(str)
    AC_central_multi_split = dd.read_csv("./Input/air_conditioner_heat_pumps_central_multi_split.csv", dtype={'Indoor_Unit_1___Type__If_Applicable_s': 'object', 'Indoor_Unit_2__If_Applicable___Brand_s__s': 'object',
                                                                                                              'Indoor_Unit_2__If_Applicable___Individual_Model_Number_m': 'object', 'Indoor_Unit_2__If_Applicable___Type_s': 'object',
                                                                                                              'Indoor_Unit_3__If_Applicable___Brand_s__s': 'object', 'Indoor_Unit_3__If_Applicable___Individual_Model_Number_m': 'object',
                                                                                                              'Indoor_Unit_3__If_Applicable___Type_s': 'object', 'Indoor_Unit_4__If_Applicable___Brand_s__s': 'object',
                                                                                                              'Indoor_Unit_4__If_Applicable___Individual_Model_Number_m': 'object', 'Indoor_Unit_4__If_Applicable___Type_s': 'object'})
    AC_central_multi_split.columns = ['Description', 'Brand', 'Model Number', 'Indoor Unit 1 Brand', 'Indoor Unit 1 Model Number', 'Indoor Unit 1 Type',
                                      'Air Mover 1 Brand', 'Air Mover 1 Model Number', 'Indoor Unit 2 Brand', 'Indoor Unit 2 Model Number', 'Indoor Unit 2 Type',
                                      'Air Mover 2 Brand', 'Air Mover 2 Model Number', 'Indoor Unit 3 Brand', 'Indoor Unit 3 Model Number', 'Indoor Unit 3 Type',
                                      'Air Mover 3 Brand', 'Air Mover 3 Model Number', 'Indoor Unit 4 Brand', 'Indoor Unit 4 Model Number', 'Indoor Unit 4 Type',
                                      'Air Mover 4 Brand', 'Air Mover 4 Model Number', 'Indoor Unit 5 Brand', 'Indoor Unit 5 Model Number', 'Indoor Unit 5 Type',
                                      'Air Mover 5 Brand', 'Air Mover 5 Model Number', 'Non Duct SEER 1', 'Duct SEER 1', 'Mixed SEER 1', 'SDHV SEER', 'SDHV Non Duct SEER',
                                      'SDHV Duct SEER', 'Non Duct HSPF 1', 'Duct HSPF 1', 'Mixed HSPF 1', 'SDHV HSPF', 'SDHV Non Duct HSPF', 'SDHV Duct HSPF', 'Non Duct EER',
                                      'Duct EER', 'Mixed EER', 'SDHV EER', 'SDHV Non Duct EER', 'SDHV Duct EER', 'Avg Off Mode Power Consumption', 'Cooling Btu/h',
                                      'Acceptable Refrigerant Types', 'Sold in South', 'Sold Southwest', 'Test Procedure', 'Hearing and Appeals', 'Indoor Unit Brand',
                                      'Indoor Unit Model Number', 'Air Mover Brand', 'Air Mover Model Number', 'Non Duct SEER', 'Duct SEER', 'Mixed SEER', 'Non Duct HSPF',
                                      'Duct HSPF', 'Mixed HSPF', 'Link']
    AC_variable_refirg_multi_split = dd.read_csv("./Input/air_conditioner_heat_pumps_variable_refrig_multi_split.csv")
    AC_variable_refirg_multi_split.columns = ['Brand', 'Equip Type', 'Cooling Capacity', 'Heating Type', 'Basic Model Number', 'Individual Model Number', 'Cooling Btu/h',
                                              'Seasonal EER.', 'Heating PF', 'EER', 'COP', 'Type Heating', 'Test Procedure', 'Hearing and Appeals']
    AC_central = dd.read_csv("./Input/air_conditioners_heat_pumps_central.csv")
    AC_central.columns = ['Brand', 'Description', 'Basic Model Number', 'Outdoor Model Number', 'Indoor Model Number', 'Air Mover Model Number', 'Cooling Btu/h', 'Heating Btu/h',
                          'Seasonal EER', 'Notes', 'Heating PF', 'Average Off Mode Consumption', 'EER', 'Efficiency Test', 'Test Procedure', 'Hearing and Appeals', 'Link',
                          'Cost Category', 'Nearest DHR']
    AC_central_cool_only = AC_central.loc[AC_central['Cost Category'] == "Cooling"]
    AC_central_cool_only = AC_central_cool_only.compute().reset_index()
    AC_central_both = AC_central.loc[AC_central['Cost Category'] == "Cooling, Heating"]
    AC_central_both = AC_central_both.compute().reset_index()
    AC_commercial = dd.read_csv("./Input/air_conditioners_heat_pumps_commercial.csv", dtype={'Integrated_Energy_Efficiency_Ratio__IEER__Btu_Wh___if_Applicable_d': 'float64', 'Phase_s': 'object'})
    AC_commercial.columns = ['Brand', 'Equip Type', 'Source', 'Phase', 'Basic Model Number', 'Individual Model Number', 'Cooling Btu/h', 'Seasonal EER', 'Integrated EER',
                             'Heating PF', 'Test Procedure', 'Hearing and Appeals']
    AC_package_terminals = dd.read_csv("./Input/air_conditioners_heat_pumps_package_terminals.csv")
    AC_package_terminals.columns = ['Brand', 'Description', 'Cooling Range', 'Basic Model Number', 'Individual Model Number', 'Wall Sleeve Height', 'Wall Sleeve Width', 'Cooling Btu/h',
                                    'EER', 'COP', 'Break In Period', 'Test Procedure', 'Hearing and Appeals', 'Certification AEDM']
    AC_single_package_vertical = dd.read_csv("./Input/air_conditioners_heat_pumps_single_package_vertical.csv")
    AC_single_package_vertical.columns = ['Brand', 'Description', 'Phase', 'Basic Model Number', 'Individual Model Number', 'Cooling Btu/h', 'EER', 'COP', 'Test Procedure', 'Hearing and Appeals']
    direct_heating = dd.read_csv("./Input/direct_heating_equipment.csv")
    direct_heating.columns = ['Brand', 'Product Group', 'Basic Model Number', 'Individual Model Number', 'Mean Input Capacity BTU', 'Mean Output Capacity BTU', 'Fuel Efficiency',
                              'Test Procedure', 'Hearing and Appeals']
    general_pumps = dd.read_csv("./Input/pumps_general_pumps.csv", dtype={'Alternate_Single_Individual_Model_Number_for_Bare_Pump_with_Driver_or_Bare_Pump_with_Driver_and_Controls_m': 'object',
                                                                          'For_EM_Pumps___Was_the_PEICL_Calculated_or_Tested__s': 'object'})
    general_pumps.columns = ['Brand', 'Equipment', 'RPM', 'Mode', 'Basic Model Number', 'Individual Model Number', 'Individual Model Number Driver', 'Individual Model Number Controls',
                             'Alt Model Number', 'Configuration', 'Energy Index', 'Total Head', 'GPM', 'Impeller Diameter', 'BP Driver Power 75 Load', 'BP Driver Power 100 Load',
                             'BP Driver Power 110 Load', 'BP Energy Rating', 'EM Driver Power 75 Load', 'EM Driver Power 100 Load', 'EM Driver Power 110 Load', 'EM PEICL Cal/Test', 'EM Energy Rating',
                             'C NC Driver Power 25 Load', 'C NC Driver Power 50 Load', 'C NC Driver Power 75 Load', 'C NC Driver Power 100 Load', 'C NC PEIVL Cal/Test', 'C NC Energy Rating',
                             'Best Efficiency', 'RSV ST Stages Tested', 'Test Procedure', 'Hearing and Appeals']
    water_heater_commercial_gas_oil = dd.read_csv("./Input/water_heater_boilers_commercial_gas_oil_fired.csv")
    water_heater_commercial_gas_oil.columns = ['Brand', 'Description', 'Basic Model Number', 'Individual Model Number', 'Storage Volume Gal', 'Input Btu/h', 'First Hour Rating Gal', 'Standby Loss Btu/h',
                                               'Recovery Eff', 'Thermal Eff', 'Uniform Energy Factor', 'Thermally Insulated', 'Pilot Light', 'Flue Damper', 'Test Procedure',
                                               'Hearing and Appeals']
    water_heater_commercial_instantaneous = dd.read_csv("./Input/water_heater_boilers_commercial_instantaneous.csv")
    water_heater_commercial_instantaneous.columns = ['Brand', 'Description', 'Basic Model Number', 'Individual Model Number', 'Storage Volume Gal', 'GPM', 'Input Btu/h', 'Standby Loss Btu/h',
                                                     'Recovery Eff', 'Thermal Eff', 'Uniform Energy Factor', 'Thermally Insulated', 'Pilot Light', 'Flue Damper', 'Test Procedure', 'Hearing and Appeals']
    water_heater_commercial_packaged_both_hw_steam = dd.read_csv("./Input/water_heater_boilers_commercial_packaged_Both_HW_Steam.csv")
    water_heater_commercial_packaged_both_hw_steam.columns = ['Brand', 'Equipment', 'Subcategory', 'Basic Model Number', 'Individual Model Number', 'Input Btu/h', 'Thermal Eff', 'Combustion Eff',
                                                              'Test Procedure', 'Hearing and Appeals']
    water_heater_commercial_packaged_hw_or_steam = dd.read_csv("./Input/water_heater_boilers_commercial_packaged_HW_Steam.csv")
    water_heater_commercial_packaged_hw_or_steam.columns = ['Brand', 'Equipment', 'Subcategory', 'Basic Model Number', 'Individual Model Number', 'Input Btu/h', 'Thermal Eff', 'Combustion Eff',
                                                              'Test Procedure', 'Hearing and Appeals']
    water_heater = dd.read_csv("./Input/water_heaters.csv")
    water_heater.columns = ['Brand', 'Basic Model Number', 'Individual Model Number', 'Type', 'Storage Volume Gal', 'Draw Pattern', 'Uniform Energy Factor', 'Energy Factor', 'First Hour Rating',
                            'Max GPM', 'Recovery Eff', 'Test Procedure', 'Hearing and Appeals', 'Link']
    water_heater_boilers_commercial_electric = dd.read_csv("./Input/water_heaters_boilers_commercial_electric.csv")
    water_heater_boilers_commercial_electric.columns = ['Brand', 'Description', 'Basic Model Number', 'Individual Model Number', 'Max Standby Loss', 'Storage Volume Gal',
                                                        'Test Procedure', 'Hearing and Appeals']
    lamps_bare_covered = dd.read_csv("./Input/Lamps_Bare_or_Covered_(No_Reflector)_Medium_Base_Compact_Fluorescent.csv")
    lamps_bare_covered.columns = ['Brand', 'Product', 'Basic Model Number', 'Individual Model Number', 'ILAC Number', 'Output Lumen', 'Power Watts', 'Initial Efficiency', '1000 Hour Maintenance',
                                  '40 Rated Life Maintenance', 'Stress Cycle Test', 'Lifetime Hours', 'Years Life', 'Test Procedure', 'Hearing and Appeals']
    lamps_general_service_fluorescent = dd.read_csv("./Input/Lamps_General_Service_Fluorescent.csv", dtype={'Correlated_Color_Temperature__Degrees_Kelvin__d': 'float64'})
    lamps_general_service_fluorescent.columns = ['Brand', 'Product', 'Basic Model Number', 'Individual Model Number', 'ILAC Number', 'Avg Lamp Efficiency', 'Watts', 'Color Temp', 'Enerdox',
                                                 'Test Procedure', 'Hearing and Appeals']
    lamps_general_service_incandescent = dd.read_csv("./Input/Lamps_General_Service_Incandescent.csv")
    lamps_general_service_incandescent.columns = ['Brand', 'Product', 'Basic Model Number', 'Individual Model Number', 'Avg Rated Wattage', 'Avg Lifetime Hours', 'Avg Color Rendering', 'ILAC Number',
                                                  'Test Procedure', 'Hearing and Appeals']
    lamps_incandescent_reflector = dd.read_csv("./Input/Lamps_Incandescent_Reflector.csv")
    lamps_incandescent_reflector.columns = ['Brand', 'Product', 'Basic Model Number', 'Individual Model Number', 'ILAC Number', 'Watts', 'Avg Efficiency', 'Test Procedure', 'Hearing and Appeals']

    pd.set_option('display.max_colwidth', None, 'display.max_rows', None, 'display.max_columns', None)

    ######__________ Beginning of Assigning Technologies to Key Parameters ___________######

    ##### Heating COP #####

    if CH_Bool == False:
        instant = pd.DataFrame(water_heater_commercial_instantaneous['Input Btu/h'].sub(heat_BTU).div(heat_BTU).abs())
        gas_oil = pd.DataFrame(water_heater_commercial_gas_oil['Input Btu/h'].sub(heat_BTU).div(heat_BTU).abs())
        hw_steam = pd.DataFrame(water_heater_commercial_packaged_both_hw_steam['Input Btu/h'].sub(heat_BTU).div(heat_BTU).abs())
        hw_or_steam = pd.DataFrame(water_heater_commercial_packaged_hw_or_steam['Input Btu/h'].sub(heat_BTU).div(heat_BTU).abs())

        instant_tech = []
        gas_oil_tech = []
        hw_steam_tech = []
        hw_or_steam_tech = []

        for i in range(0, 10, 1):
            min_index = instant.idxmin()
            instant_tech.append(water_heater_commercial_instantaneous.loc[min_index[0]].compute().reset_index())
            instant = instant.drop(index=min_index[0])

            min_index = gas_oil.idxmin()
            gas_oil_tech.append(water_heater_commercial_gas_oil.loc[min_index[0]].compute().reset_index())
            gas_oil = gas_oil.drop(index=min_index[0])

            min_index = hw_steam.idxmin()
            hw_steam_tech.append(water_heater_commercial_packaged_both_hw_steam.loc[min_index[0]].compute().reset_index())
            hw_steam = hw_steam.drop(index=min_index[0])

            min_index = hw_or_steam.idxmin()
            hw_or_steam_tech.append(water_heater_commercial_packaged_hw_or_steam.loc[min_index[0]].compute().reset_index())
            hw_or_steam = hw_or_steam.drop(index=min_index[0])

        form = {"cost": "", "btu": "", "param1": ""}

        num_techs = len(instant_tech)
        heatingEfficiency = []

        for i in range(0, num_techs):
            form["cost"] = 100 # PLACEHOLDER
            form["btu"] = instant_tech[i]["Input Btu/h"][0]
            form["param1"] = instant_tech[i]["Thermal Eff"][0]
            tech = {str(instant_tech[i]["Brand"][0] + " : " + instant_tech[i]["Description"][0]): form.copy()}
            heatingEfficiency.append(tech.copy())

            form["cost"] = 100  # PLACEHOLDER
            form["btu"] = gas_oil_tech[i]["Input Btu/h"][0]
            form["param1"] = gas_oil_tech[i]["Thermal Eff"][0]
            tech = {str(gas_oil_tech[i]["Brand"][0] + " : " + gas_oil_tech[i]["Description"][0]): form.copy()}
            heatingEfficiency.append(tech.copy())

            form["cost"] = 100  # PLACEHOLDER
            form["btu"] = hw_steam_tech[i]["Input Btu/h"][0]
            form["param1"] = hw_steam_tech[i]["Thermal Eff"][0]
            tech = {str(hw_steam_tech[i]["Brand"][0] + " : " + hw_steam_tech[i]["Equipment"][0]): form.copy()}
            heatingEfficiency.append(tech.copy())

            form["cost"] = 100  # PLACEHOLDER
            form["btu"] = hw_or_steam_tech[i]["Input Btu/h"][0]
            form["param1"] = hw_or_steam_tech[i]["Thermal Eff"][0]
            tech = {str(hw_or_steam_tech[i]["Brand"][0] + " : " + hw_or_steam_tech[i]["Equipment"][0]): form.copy()}
            heatingEfficiency.append(tech.copy())
    else:
        heatingEfficiency = []

    ##### DHW #####

    instant_BTU = pd.DataFrame(water_heater_commercial_instantaneous['Input Btu/h'].sub(DHW_BTU).div(DHW_BTU).abs())
    instant_gal = pd.DataFrame(water_heater_commercial_instantaneous['Storage Volume Gal'].sub(Vol).div(Vol).abs())
    instant = instant_BTU + instant_gal
    gas_oil_BTU = pd.DataFrame(water_heater_commercial_gas_oil['Input Btu/h'].sub(DHW_BTU).div(DHW_BTU).abs())
    gas_oil_gal = pd.DataFrame(water_heater_commercial_gas_oil['Storage Volume Gal'].sub(Vol).div(Vol).abs())
    gas_oil = gas_oil_BTU + gas_oil_gal

    instant_tech = []
    gas_oil_tech = []

    for i in range(0, 10, 1):
        min_index = instant.idxmin()
        instant_tech.append(water_heater_commercial_instantaneous.loc[min_index[0]].compute().reset_index())
        instant = instant.drop(index=min_index[0])

        min_index = gas_oil.idxmin()
        gas_oil_tech.append(water_heater_commercial_gas_oil.loc[min_index[0]].compute().reset_index())
        gas_oil = gas_oil.drop(index=min_index[0])

    form = {"cost": "", "btu": "", "gal": "", "param1": ""}

    num_techs = len(instant_tech)
    DHWEfficiency = []

    for i in range(0, num_techs):
        form["cost"] = 100  # PLACEHOLDER
        form["btu"] = instant_tech[i]["Input Btu/h"][0]
        form["gal"] = instant_tech[i]["Storage Volume Gal"][0]
        form["param1"] = instant_tech[i]["Thermal Eff"][0] * .01
        tech = {str(instant_tech[i]["Brand"][0] + " : " + instant_tech[i]["Description"][0]): form.copy()}
        DHWEfficiency.append(tech.copy())

    ##### Cooling COP #####

    if CH_Bool == False:
        central_multi_split = pd.DataFrame(AC_central_multi_split['Cooling Btu/h'].sub(cool_BTU).div(cool_BTU).abs())
        refrig_multi_split = pd.DataFrame(AC_variable_refirg_multi_split['Cooling Btu/h'].sub(cool_BTU).div(cool_BTU).abs())
        commercial = pd.DataFrame(AC_commercial['Cooling Btu/h'].sub(cool_BTU).div(cool_BTU).abs())
        package_terminal = pd.DataFrame(AC_package_terminals['Cooling Btu/h'].sub(cool_BTU).div(cool_BTU).abs())
        single_package_vertical = pd.DataFrame(AC_single_package_vertical['Cooling Btu/h'].sub(cool_BTU).div(cool_BTU).abs())
        central_cool_only = pd.DataFrame(AC_central_cool_only['Cooling Btu/h'].sub(cool_BTU).div(cool_BTU).abs())

        central_multi_split_tech = []
        refrig_multi_split_tech = []
        commercial_tech = []
        package_terminal_tech = []
        single_package_vertical_tech = []
        central_cool_only_tech = []

        for i in range(0, 10, 1):
            min_index = central_multi_split.idxmin()
            central_multi_split_tech.append(AC_central_multi_split.loc[min_index[0]].compute().reset_index())
            central_multi_split = central_multi_split.drop(index=min_index[0])

            min_index = refrig_multi_split.idxmin()
            refrig_multi_split_tech.append(AC_variable_refirg_multi_split.loc[min_index[0]].compute().reset_index())
            refrig_multi_split = refrig_multi_split.drop(index=min_index[0])

            min_index = commercial.idxmin()
            commercial_tech.append(AC_commercial.loc[min_index[0]].compute().reset_index())
            commercial = commercial.drop(index=min_index[0])

            min_index = package_terminal.idxmin()
            package_terminal_tech.append(AC_package_terminals.loc[min_index[0]].compute().reset_index())
            package_terminal = package_terminal.drop(index=min_index[0])

            min_index = single_package_vertical.idxmin()
            single_package_vertical_tech.append(AC_package_terminals.loc[min_index[0]].compute().reset_index())
            single_package_vertical = single_package_vertical.drop(index=min_index[0])

            min_index = central_cool_only.idxmin()
            central_cool_only_tech.append(AC_central_cool_only.loc[min_index[0]])
            central_cool_only = central_cool_only.drop(index=min_index[0])

            # .compute().reset_index()

        form = {"cost": "", "btu": "", "param1": ""}

        num_techs = len(central_multi_split_tech)
        coolingEfficiency = []

        for i in range(0, num_techs):
            form["cost"] = 100  # PLACEHOLDER
            form["btu"] = central_multi_split_tech[i]["Cooling Btu/h"][0]
            if SDHV == True:
                if central_multi_split_tech[i]["SDHV Duct EER"][0] != "":
                    form["param1"] = central_multi_split_tech[i]["Duct EER"][0]/3.41214
                elif central_multi_split_tech[i]["SDHV Non Duct EER"][0] != "":
                    form["param1"] = central_multi_split_tech[i]["Non Duct EER"][0]/3.41214
                elif central_multi_split_tech[i]["SDHV Mixed EER"][0] != "":
                    form["param1"] = central_multi_split_tech[i]["Mixed EER"][0]/3.41214
            else:
                if central_multi_split_tech[i]["Duct EER"][0] != "":
                    form["param1"] = central_multi_split_tech[i]["Duct EER"][0]/3.41214
                elif central_multi_split_tech[i]["Non Duct EER"][0] != "":
                    form["param1"] = central_multi_split_tech[i]["Non Duct EER"][0]/3.41214
                elif central_multi_split_tech[i]["Mixed EER"][0] != "":
                    form["param1"] = central_multi_split_tech[i]["Mixed EER"][0]/3.41214
            tech = {str(central_multi_split_tech[i]["Brand"][0] + " : " + central_multi_split_tech[i]["Description"][0]): form.copy()}
            coolingEfficiency.append(tech.copy())

            form["cost"] = 100  # PLACEHOLDER
            form["btu"] = refrig_multi_split_tech[i]["Cooling Btu/h"][0]
            if refrig_multi_split_tech[i]["EER"][0] != "":
                form["param1"] = refrig_multi_split_tech[i]["EER"][0]/3.41214
            else:
                form["param1"] = refrig_multi_split_tech[i]["COP"][0]
            tech = {str(refrig_multi_split_tech[i]["Brand"][0] + " : " + refrig_multi_split_tech[i]["Equip Type"][0]): form.copy()}
            coolingEfficiency.append(tech.copy())

            form["cost"] = 100  # PLACEHOLDER
            form["btu"] = commercial_tech[i]["Cooling Btu/h"][0]
            form["param1"] = commercial_tech[i]["Seasonal EER"][0]/3.41214
            tech = {str(commercial_tech[i]["Brand"][0] + " : " + commercial_tech[i]["Equip Type"][0]): form.copy()}
            coolingEfficiency.append(tech.copy())

            form["cost"] = 100  # PLACEHOLDER
            form["btu"] = package_terminal_tech[i]["Cooling Btu/h"][0]
            if package_terminal_tech[i]["EER"][0] != "":
                form["param1"] = package_terminal_tech[i]["EER"][0]/3.41214
            else:
                form["param1"] = package_terminal_tech[i]["COP"][0]
            tech = {str(package_terminal_tech[i]["Brand"][0] + " : " + package_terminal_tech[i]["Description"][0]): form.copy()}
            coolingEfficiency.append(tech.copy())

            form["cost"] = 100  # PLACEHOLDER
            form["btu"] = single_package_vertical_tech[i]["Cooling Btu/h"][0]
            if single_package_vertical_tech[i]["EER"][0] != "":
                form["param1"] = single_package_vertical_tech[i]["EER"][0]/3.41214
            else:
                form["param1"] = single_package_vertical_tech[i]["COP"][0]
            tech = {str(single_package_vertical_tech[i]["Brand"][0] + " : " + single_package_vertical_tech[i]["Description"][0]): form.copy()}
            coolingEfficiency.append(tech.copy())

            form["cost"] = 100  # PLACEHOLDER
            # print(central_cool_only_tech[i]["Cooling Btu/h"])
            form["btu"] = central_cool_only_tech[i]["Cooling Btu/h"]
            form["param1"] = central_cool_only_tech[i]["EER"] / 3.41214
            tech = {str(central_cool_only_tech[i]["Brand"] + " : " + central_cool_only_tech[i]["Description"]): form.copy()}
            coolingEfficiency.append(tech.copy())
            # print(coolingEfficiency)
    else:
        coolingEfficiency = []



    ##### Heating and Cooling COP #####

    if CH_Bool == True:

        heatingEfficiency = []
        coolingEfficiency = []

        central_cooling = pd.DataFrame(AC_central_both['Cooling Btu/h'].sub(cool_BTU).div(cool_BTU).abs())
        central_heating = pd.DataFrame(AC_central_both['Heating Btu/h'].sub(heat_BTU).div(heat_BTU).abs())
        central_combo = central_heating['Heating Btu/h'] + central_cooling['Cooling Btu/h']
        central_both_tech = []

        for i in range(0, 10, 1):
            min_index = central_combo.idxmin()
            central_both_tech.append([AC_central_both.loc[min_index]])
            central_combo = central_combo.drop(index=min_index)
        form = {"cost": "", "Heating Btu": "", "Cooling Btu": "", "param1": "", "param2": ""}

        num_techs = len(central_both_tech)
        heatingCoolingEfficiency = []

        # print(central_both_tech)

        for i in range(0, num_techs):
            form["cost"] = 100  # PLACEHOLDER
            form["Heating Btu"] = central_both_tech[i][0]["Heating Btu/h"]
            form["Cooling Btu"] = central_both_tech[i][0]["Cooling Btu/h"]
            form["param1"] = central_both_tech[i][0]["EER"] / 3.41214
            form["param2"] = central_both_tech[i][0]["Heating PF"] * 0.293
            tech = {str(central_both_tech[i][0]["Brand"] + " : " + central_both_tech[i][0]["Description"]): form.copy()}
            heatingCoolingEfficiency.append(tech.copy())
    else:
        heatingCoolingEfficiency = []

    return heatingEfficiency, coolingEfficiency, heatingCoolingEfficiency, DHWEfficiency

if __name__ == '__main__':

    CH_Bool = False          # Combined Heating and Cooling System (Heat Pump)
    SDHV = False            # Small Duct
    heat_BTU = 16000      # Input BTU/h for Heating System
    cool_BTU = 16000       # Input BTU/h for Cooling System
    DHW_BTU = 16000       # Input BTU/h for DHW System
    Vol = 187               # Volume of DHW Tank

    heatingEfficiency, coolingEfficiency, heatingCoolingEfficiency, DHWEfficiency = load_tech(heat_BTU, cool_BTU, SDHV, DHW_BTU, Vol, CH_Bool)
    print(heatingEfficiency)
    print(coolingEfficiency)
    print(heatingCoolingEfficiency)
    print(DHWEfficiency)