import numpy as np
import json
import pandas as pd
from math import sqrt

class BEM:
    
    def __init__(self, jsonData, weatherData, SRF_overhang, SRF_fin, SRF_horizon, Essol_30, Essol_45, Essol_60, Essol_90):
        self.jsonData = jsonData
        self.weatherData  = weatherData
        self.SRF_overhang = SRF_overhang
        self.SRF_fin      = SRF_fin
        self.SRF_horizon  = SRF_horizon
        self.Essol_30     = Essol_30
        self.Essol_45     = Essol_45
        self.Essol_60     = Essol_60
        self.Essol_90     = Essol_90

        # 1. Variables for the "INPUT" sheet
        # left-hand side of excel BEM file
        self._left_numeric_range = [13, 14, 21, 22, 23, 27, 28, 41, 44, 45, 46, 53, 57, 59, 60, 61, 63, 65, 68, 69]
        self.left_numeric = np.zeros((20,1))
        self._right_string_range = [12, 17, 24, 38, 39, 42, 43, 47, 48, 50, 51, 58, 64, 72, 73, 74]
        self.right_string=[]

        # Right hand side of excel BEM file
        self.zone             = np.zeros((7,10))
        self.setPoint         = np.zeros((24,4))
        self.zone1_schedule   = np.zeros((24,6))
        self.zone2_schedule   = np.zeros((24,6))
        self.zone3_schedule   = np.zeros((24,6))
        self.zone4_schedule   = np.zeros((24,6))
        self.zone5_schedule   = np.zeros((24,6))
        self.zone6_schedule   = np.zeros((24,6))
        self.zone7_schedule   = np.zeros((24,6))
        self.zone8_schedule   = np.zeros((24,6))
        self.zone9_schedule   = np.zeros((24,6))
        self.zone10_schedule  = np.zeros((24,6))
        self.envelope         = np.zeros((10,12))
        self.material         = np.zeros((6,4))

        # 2. Variables for the "CALC" sheet
        # 2.1 General Data Processing
        self.zone_schedule = np.zeros((24,6)) # Final Total aggregated
        
        # 2.2 Building Geometry and Transmission Heat Transfer 
        self.EvenlopeHeatCapacity=0
        self.AmFactor=0

        # 2.3 Ventilation Air Flow and Ventilation Heat Transfer
        self.qv_min=0
        self.ResMin_ACH=0.3
        self.ventSupply=0
        self.ventExhaust=0
        self.ventRecirculation=0
        self.HR_efficiency=0
        self.vsite=0

        # 2.4 Cooling and Heating System Energy
        self.f_waste=0 # Distribution loss
        self.a_heat=0
        self.a_cool=0
        self.f_dem_cold=0
        self.f_dem_heat=0
        self.dist_cool=0
        self.dist_heat=0
        self.Q_heat_nd = np.zeros((13,1))
        self.Q_cool_nd = np.zeros((13,1))
        self._range = [0,744,1416,2160,2880,3623,4344, 5088, 5832, 6552, 7296, 8016, 8760]

        # 2.6 Fan Energy
        self.T_supply_h=0; self.T_supply_c=0
        
        # 2.7 PumpSystemEnergy
        self.fcntrl_heat=0; self.fcntrl_cool=0
        self.pump_Equip=np.zeros((13,2))
        self.constants=[2.6784, 2.4192, 2.6784, 2.5920, 2.6784, 2.5920, 2.6784, 2.6784, 2.5920, 2.6784, 2.5920, 2.6784, 31.536]
        
        # 2.8 DHW and Solar Water Heating
        self.hotWaterDemand=0
        self.Qdem_kWh=0
        self.DHW_system=0
        self.total_DHW_system=0
        self.effi_sys_DHW=0
        self.effi_gen_DHW=0
        
        # 2.9 BEM System
        self.f_BAC_hc=0; self.f_BAC_e=0
        
        # 3. Varables for the "CALC_H" sheet
        # Upper parts coefficients
        self.Htr_w_Af=0; self.Htr_op_Af=0; self.Htr_w=0 
        self.Htr_op=0; self.Htr_total=0; self.Htr_w=0  
        self.Htr_op=0; self.H_es=0; self.Htr_em=0 
        self.Htr_ms=0; self.Htr_is=15.525
        self.Prs=0; self.Prm=0 
        self.glazing1         = np.zeros((11,9))
        self.glazing2         = np.zeros((11,9))
        self.opaque1          = np.zeros((7,9)) 
        self.opaque2          = np.zeros((7,9)) 
        self.Rse              = np.zeros((8760,1)) # Rse colum (column DR in hourly BEM)
        self.heatgainGlazing1 = np.zeros((8760,11))
        self.heatgainGlazing2 = np.zeros((8760,11)) 
        self.heatgainOpaque1  = np.zeros((8760,10))
        self.heatgainOpaque2  = np.zeros((8760,10)) 
        self.SRFOverhang1=1; self.SRFOverhang2=1
        self.SRFFin1=1; self.SRFFin2=1
        self.SRFHor1=1; self.SRFHor2=1
        self.occu_equi_hours=0
        self.deliveredEnergy  = np.zeros((8760,11))
        self.Overall_Array    = np.zeros((8760,96))
        self.Overall_deliveredEnergy=0 # aggregation value of 8,760 Etotal (Eheat+Ecool+Elight+Efan+Epump+Eequip+Edhw+Eev-Egen_pv-Egen_wind))
        self.deliveredEnergy_fuel=np.zeros((8760,4)) # 0th: electricity, 1st: natural gas, 2nd: fuel, 3rd: total, # Unit: kWh                                                       
        self.BEMP_JSON={}
        
        # natural ventilation
        self.Cw=0; self.Qw=0; self.Cd=0; self.Qs=0
        self.NV_width=0; self.NV_height=0; self.NV_effective_angle=0; self.QNV_total=0; self.NV_openingRatio=0; self.NV_included=False

        # electric battery
        self.electric_battery = np.zeros((8760,7))
        self.eb_capacity=0; self.eta_charge=0; self.eta_discharge=0
        self.P_charg_limit=0; self.P_discharge_limit=0

        # lighting dimmer
        self.dimmer_wd=0; self.dimmer_we=0

        # electric vehicle
        self.EV_no_charger=0; self.EV_charging_power=0
        self.EV_schedule = np.zeros((24,2))
        self.EV_tempo=0

        # retail refrig
        self.retail_refrig_cap=0; self.retail_refrig_cap_per_area=0
        self.retail_zone="Zone1"

        # monthly internal heat gain
        self.monthly_internal_heat_gain_bool = False
        self.monthly_internal_heat_gain = np.zeros((12,3))
        
        # garage
        self.garage_appliance=0; self.garage_lighting=0
        self.garage_schedule=np.zeros((24,4)); self.garage_schedule_all=np.zeros((8760,4)) ####

        
        # Initial setup
        self.Overall_Array[:,0]  = range(1,8761) # cumulative hour
        self.Overall_Array[:,26] = 10
    
    def readJSON(self):
        # with open(self.jsonData) as f:
        #    self.BEMP_JSON = json.load(f)
        # with open(self.buildingName) as f:
        #    self.BEMP_JSON = json.load(f)
        self.BEMP_JSON = self.jsonData

        self.outputPeriod = self.BEMP_JSON["OutputPeriod"]

        self.left_numeric[0,0] = self.BEMP_JSON["Volume"]
        self.left_numeric[1,0] = self.BEMP_JSON["Height"]
        self.left_numeric[2,0] = self.BEMP_JSON["DaylightingFactor"]
        self.left_numeric[3,0] = self.BEMP_JSON["OccupancyFactor"]
        self.left_numeric[4,0] = self.BEMP_JSON["LightingControlFactor"]
        self.left_numeric[5,0] = self.BEMP_JSON["HeatingCOP"]
        self.left_numeric[6,0] = self.BEMP_JSON["CoolingCOP"]
        self.left_numeric[7,0] = self.BEMP_JSON["ExtraVentilation"]
        self.left_numeric[8,0] = self.BEMP_JSON["AirLeakageLevel"]
        self.left_numeric[9,0] = self.BEMP_JSON["SpecificFanPower"]
        self.left_numeric[10,0] = self.BEMP_JSON["FanControlFactor"]
        self.left_numeric[11,0] = self.BEMP_JSON["BEMType"]
        self.left_numeric[12,0] = self.BEMP_JSON["PVArea"]
        self.left_numeric[13,0] = self.BEMP_JSON["PVTiltAngle"]
        self.left_numeric[14,0] = self.BEMP_JSON["PVPeakPower"]
        self.left_numeric[15,0] = self.BEMP_JSON["PVPerformanceFactor"]
        self.left_numeric[16,0] = self.BEMP_JSON["SHWArea"]
        self.left_numeric[17,0] = self.BEMP_JSON["SHWTiltAngle"]
        self.left_numeric[18,0] = self.BEMP_JSON["WindTurbineDiameter"]
        self.left_numeric[19,0] = self.BEMP_JSON["WindTurbineEfficiency"]
        self.right_string.append(self.BEMP_JSON["TerrainClass"])
        self.right_string.append(self.BEMP_JSON["HeatCapacity"])
        self.right_string.append(self.BEMP_JSON["ParasiticLightingEnergy"])
        self.right_string.append(self.BEMP_JSON["HVACSystemType"])
        self.right_string.append(self.BEMP_JSON["VentilationCoolingType"])
        self.right_string.append(self.BEMP_JSON["HeatRecoveryType"])
        self.right_string.append(self.BEMP_JSON["ExhaustAirRecirculation"])
        self.right_string.append(self.BEMP_JSON["PumpCoolingControl"])
        self.right_string.append(self.BEMP_JSON["PumpHeatingControl"])
        self.right_string.append(self.BEMP_JSON["DHWDistrinutionSystem"])
        self.right_string.append(self.BEMP_JSON["DHWGenerationSystem"])
        self.right_string.append(self.BEMP_JSON["PVOrientation"])
        self.right_string.append(self.BEMP_JSON["SHWOrientation"])
        self.right_string.append(self.BEMP_JSON["HeatingEnergySource"])
        self.right_string.append(self.BEMP_JSON["DHWEnergySource"])
        self.right_string.append(self.BEMP_JSON["CoolingEnergySource"])

        hour_index             = ["".join(["Hour",str(i)]) for i in range(1,25)]
        zone_container         = ["GrossFloorArea", "Occupancy", "MatabolicRate", "Appliance", "Lighting", "OutdoorAir", "DHW"]
        schduel_index          = ["Occupancy_Weekday", "Occupancy_Weekend", "Appliance_Weekday", "Appliance_Weekend", "Lighting_Weekday", "Lighting_Weekend"]
        Orientation_container  = ["S", "SE", "E", "NE", "N", "NW", "W", "SW", "Roof", "BelowGrade"]
        material_container     = ["UValue", "Absorptivity", "Emissivity"]
        window_container       = ["UValue", "dummy" , "Emissivity", "SolarTrasmittance"]

        for i in range(24):
            self.setPoint[i,0] =  self.BEMP_JSON["TemperatureSetPoint"][hour_index[i]]["Heating_Weekday"]
            self.setPoint[i,1] =  self.BEMP_JSON["TemperatureSetPoint"][hour_index[i]]["Heating_Weekend"]
            self.setPoint[i,2] =  self.BEMP_JSON["TemperatureSetPoint"][hour_index[i]]["Cooling_Weekday"]
            self.setPoint[i,3] =  self.BEMP_JSON["TemperatureSetPoint"][hour_index[i]]["Cooling_Weekend"]
                    
        for key in self.BEMP_JSON:                                    
            if key[:4] == "Zone" and len(key) == 5:
                for j in range(7):
                    zone_index = "".join(["Zone", str(key[4])])
                    zone_number = int(key[-1])-1
                    self.zone[j,zone_number] = self.BEMP_JSON[zone_index][zone_container[j]]

            elif key[:4] == "Zone" and len(key) == 6: # Zone 10
                for j in range(7):
                    self.zone[j,9] = self.BEMP_JSON["Zone10"][zone_container[j]]      
                     
            if key[-8:] == "Schedule":
                if key[4] == '1' and key[5] != '0': # zone 1
                    for i in range(24):
                        for j in range(6):
                            self.zone1_schedule[i,j] = self.BEMP_JSON["Zone1_Schedule"][hour_index[i]][schduel_index[j]]
     
                elif key[4] == '2': # zone 2
                    for i in range(24):
                        for j in range(6):
                            self.zone2_schedule[i,j] = self.BEMP_JSON["Zone2_Schedule"][hour_index[i]][schduel_index[j]]

                elif key[4] == '3': # zone 3
                    for i in range(24):
                        for j in range(6):
                            self.zone3_schedule[i,j] = self.BEMP_JSON["Zone3_Schedule"][hour_index[i]][schduel_index[j]]

                elif key[4] == '4': # zone 4
                    for i in range(24):
                        for j in range(6):
                            self.zone4_schedule[i,j] = self.BEMP_JSON["Zone4_Schedule"][hour_index[i]][schduel_index[j]]     

                elif key[4] == '5': # zone 5
                    for i in range(24):
                        for j in range(6):
                            self.zone5_schedule[i,j] = self.BEMP_JSON["Zone5_Schedule"][hour_index[i]][schduel_index[j]]
                
                elif key[4] == '6': # zone 6
                    for i in range(24):
                        for j in range(6):
                            self.zone6_schedule[i,j] = self.BEMP_JSON["Zone6_Schedule"][hour_index[i]][schduel_index[j]]
              
                elif key[4] == '7': # zone 7
                    for i in range(24):
                        for j in range(6):
                            self.zone7_schedule[i,j] = self.BEMP_JSON["Zone7_Schedule"][hour_index[i]][schduel_index[j]]
                     
                elif key[4] == '8': # zone 8
                    for i in range(24):
                        for j in range(6):
                            self.zone8_schedule[i,j] = self.BEMP_JSON["Zone8_Schedule"][hour_index[i]][schduel_index[j]]
                       
                elif key[4] == '9': # zone 9
                    for i in range(24):
                        for j in range(6):
                            self.zone9_schedule[i,j] = self.BEMP_JSON["Zone9_Schedule"][hour_index[i]][schduel_index[j]]

                elif key[4] == '1' and key[5] == '0': # zone 10
                    for i in range(24):
                        for j in range(6):
                            self.zone10_schedule[i,j] = self.BEMP_JSON["Zone10_Schedule"][hour_index[i]][schduel_index[j]]
            
        for i in range(10):
            self.envelope[i,0] = self.BEMP_JSON["Envelope"]["Opaque1"][Orientation_container[i]]["Area"]

            try:
                self.envelope[i,1] = self.BEMP_JSON["Envelope"]["Opaque2"][Orientation_container[i]]["Area"]
            except:
                pass
                
        try:
            for i in range(9):
                self.envelope[i,2] = self.BEMP_JSON["Envelope"]["Window1"][Orientation_container[i]]["Area"]
                self.envelope[i,3] = self.BEMP_JSON["Envelope"]["Window1"][Orientation_container[i]]["OverhangAngle"]
                self.envelope[i,4] = self.BEMP_JSON["Envelope"]["Window1"][Orientation_container[i]]["FinAngle"]
                self.envelope[i,5] = self.BEMP_JSON["Envelope"]["Window1"][Orientation_container[i]]["HorizonAngle"]
                self.envelope[i,6] = self.BEMP_JSON["Envelope"]["Window1"][Orientation_container[i]]["SRF"]
        except:
            pass    

        try:
            for i in range(9):
                self.envelope[i,7] = self.BEMP_JSON["Envelope"]["Window2"][Orientation_container[i]]["Area"]
                self.envelope[i,8] = self.BEMP_JSON["Envelope"]["Window2"][Orientation_container[i]]["OverhangAngle"]
                self.envelope[i,9] = self.BEMP_JSON["Envelope"]["Window2"][Orientation_container[i]]["FinAngle"]
                self.envelope[i,10] = self.BEMP_JSON["Envelope"]["Window2"][Orientation_container[i]]["HorizonAngle"]
                self.envelope[i,11] = self.BEMP_JSON["Envelope"]["Window2"][Orientation_container[i]]["SRF"]
        except:
            pass
        
        for j in range(3):
            self.material[0,j] = self.BEMP_JSON["Material"]["Roof1"][material_container[j]]
            self.material[2,j] = self.BEMP_JSON["Material"]["Opaque1"][material_container[j]]

    
        for j in [0,2,3]:
            self.material[4,j] = self.BEMP_JSON["Material"]["Window1"][window_container[j]]

        try:
            for j in range(3):
                self.material[1,j] = self.BEMP_JSON["Material"]["Roof2"][material_container[j]]
        except:
            pass

        try:
            for j in range(3):
                self.material[3,j] = self.BEMP_JSON["Material"]["Opaque2"][material_container[j]]
        except:
            pass
        
        try:
            for j in [0,2,3]:
                self.material[4,j] = self.BEMP_JSON["Material"]["Window2"][window_container[j]]
        except:
            pass

        # start day
        self.start_day_setup = np.ones((7,1))
        if self.BEMP_JSON["StartDay"] in ["Sunday", "sunday"]:
            self.start_day_setup[0,0]=0; self.start_day_setup[6,0]=0 
        elif self.BEMP_JSON["StartDay"] in ["Monday", "monday"]:
            self.start_day_setup[5,0]=0; self.start_day_setup[6,0]=0
        elif self.BEMP_JSON["StartDay"] in ["Tuesday", "tuesday"]:
            self.start_day_setup[4,0]=0; self.start_day_setup[5,0]=0
        elif self.BEMP_JSON["StartDay"] in ["Wednesday", "wednesday"]:
            self.start_day_setup[3,0]=0; self.start_day_setup[4,0]=0
        elif self.BEMP_JSON["StartDay"] in ["Thursday", "thursday"]:
            self.start_day_setup[2,0]=0; self.start_day_setup[3,0]=0
        elif self.BEMP_JSON["StartDay"] in ["Friday", "friday"]:
            self.start_day_setup[1,0]=0; self.start_day_setup[2,0]=0
        elif self.BEMP_JSON["StartDay"] in ["Saturday", "saturday"]:
            self.start_day_setup[0,0]=0; self.start_day_setup[1,0]=0

        # natural ventilation
        try:
            self.NV_width           = self.BEMP_JSON["NaturalVentilation"]["Width"]
            self.NV_height          = self.BEMP_JSON["NaturalVentilation"]["Height"]
            self.NV_effective_angle = self.BEMP_JSON["NaturalVentilation"]["EffectiveAngle"]
            self.NV_included        = True
        except:
            pass

        # electric battery
        try:
            self.eb_capacity       = self.BEMP_JSON["ElectricBattery"]["Capacity"]
            self.eta_charge        = self.BEMP_JSON["ElectricBattery"]["ChargingEfficiency"]
            self.eta_discharge     = self.BEMP_JSON["ElectricBattery"]["DischargingEfficiency"]
            self.P_charg_limit     = self.BEMP_JSON["ElectricBattery"]["ChargingPowerLimit"]
            self.P_discharge_limit = self.BEMP_JSON["ElectricBattery"]["DischargingPowerLimit"]
        except:
            pass

        # lighting dimmer
        try:
            self.dimmer_wd         = self.BEMP_JSON["LightingDimmer"]["DimmerSaving_WD"]
            self.dimmer_we         = self.BEMP_JSON["LightingDimmer"]["DimmerSaving_WE"]

        except:
            pass

        # electric vechile
        try:
            self.EV_no_charger     = self.BEMP_JSON["ElectricVehicle"]["No_EVCharger"]
            self.EV_charging_power = self.BEMP_JSON["ElectricVehicle"]["ChargingPower"]
            for i in range(24):
                tempo_time = "".join(["Hour", str(i+1)])
                self.EV_schedule[i,0] = self.BEMP_JSON["ElectricVehicle"][tempo_time]["EV_Weekday"]
                self.EV_schedule[i,1] = self.BEMP_JSON["ElectricVehicle"][tempo_time]["EV_Weekend"]

            self.EV_tempo = self.EV_no_charger*self.EV_charging_power
        except:
            pass

        # retail
        try:
            self.retail_refrig_cap = self.BEMP_JSON["RetailRefrig"]["Capacity"]
            self.retail_zone       = self.BEMP_JSON["RetailRefrig"]["Zone"]      
        except:
            pass

        # monthly internal heat gain
        try:
            month_name = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
            for i in range(12):
                self.monthly_internal_heat_gain[i,0] = self.BEMP_JSON["Monthly_InternalHeatGain"]["Occupancy"][month_name[i]]
                self.monthly_internal_heat_gain[i,1] = self.BEMP_JSON["Monthly_InternalHeatGain"]["Appliance"][month_name[i]]
                self.monthly_internal_heat_gain[i,2] = self.BEMP_JSON["Monthly_InternalHeatGain"]["Lighting"][month_name[i]]
            self.monthly_internal_heat_gain_bool = True
        except:
            pass

        # garage
        try:
            self.garage_appliance = self.BEMP_JSON["Garage"]["Appliance"]*self.BEMP_JSON["Garage"]["Area"]
            self.garage_lighting  = self.BEMP_JSON["Garage"]["Lighting"]*self.BEMP_JSON["Garage"]["Area"]
            for i in range(24):  ####
                tempo_hour = "".join(["Hour", str(i + 1)])
                self.garage_schedule[i, 0] = self.BEMP_JSON["Garage_Schedule"][tempo_hour]["Appliance_Weekday"]
                self.garage_schedule[i, 1] = self.BEMP_JSON["Garage_Schedule"][tempo_hour]["Appliance_Weekend"]
                self.garage_schedule[i, 2] = self.BEMP_JSON["Garage_Schedule"][tempo_hour]["Lighting_Weekday"]
                self.garage_schedule[i, 3] = self.BEMP_JSON["Garage_Schedule"][tempo_hour]["Lighting_Weekend"]
        except:
            pass
    
        # Save the JSON instance
        # with open(self.buildingName, 'w', encoding='utf-8') as f:
        #     json.dump(self.BEMP_JSON, f, ensure_ascii=False, indent=4)
        
    def GeneralDataProcessing(self): 

        self.totalArea=0 
        self.totalOccupants=0
        self.standard_OA=0
        self.TotalOccupants2=0
        self.totalAppliance=0
        self.totalLighting=0
        self.hs_unoccupied=0
        
        self.totalArea = np.sum(self.zone[0,:])

        if self.retail_zone   == "Zone1":
            self.retail_refrig_cap_per_area = self.retail_refrig_cap*self.zone[0,0]/self.totalArea
        elif self.retail_zone == "Zone2":
            self.retail_refrig_cap_per_area = self.retail_refrig_cap*self.zone[0,1]/self.totalArea
        elif self.retail_zone == "Zone3":
            self.retail_refrig_cap_per_area = self.retail_refrig_cap*self.zone[0,2]/self.totalArea
        elif self.retail_zone == "Zone4":
            self.retail_refrig_cap_per_area = self.retail_refrig_cap*self.zone[0,3]/self.totalArea
        elif self.retail_zone == "Zone5":
            self.retail_refrig_cap_per_area = self.retail_refrig_cap*self.zone[0,4]/self.totalArea
        elif self.retail_zone == "Zone6":
            self.retail_refrig_cap_per_area = self.retail_refrig_cap*self.zone[0,5]/self.totalArea
        elif self.retail_zone == "Zone7":
            self.retail_refrig_cap_per_area = self.retail_refrig_cap*self.zone[0,6]/self.totalArea
        elif self.retail_zone == "Zone8":
            self.retail_refrig_cap_per_area = self.retail_refrig_cap*self.zone[0,7]/self.totalArea
        elif self.retail_zone == "Zone9":
            self.retail_refrig_cap_per_area = self.retail_refrig_cap*self.zone[0,8]/self.totalArea
        elif self.retail_zone == "Zone10":
            self.retail_refrig_cap_per_area = self.retail_refrig_cap*self.zone[0,9]/self.totalArea

        if self.totalArea == self.zone[0,0]: # Reason for this if statement: one thermal zone is set up most times thus, below two for-loops are usually unnecessary 
            self.zone_schedule = self.zone1_schedule

            # Internal gains
            self.totalOccupants  += self.zone[0,0]*self.zone[2,0]/self.zone[1,0]/self.totalArea
            self.standard_OA     += self.zone[5,0]*self.zone[0,0]/self.zone[1,0]
            self.TotalOccupants2 += self.zone[0,0]/self.zone[1,0]
            self.totalAppliance  += self.zone[0,0]*self.zone[3,0]/self.totalArea
            self.totalLighting   += self.zone[0,0]*self.zone[4,0]/self.totalArea
        else:
            # Aggregated schedule value
            for i in range(24):
                for j in range(6):
                    #(Schedule density * each zone's area)/total area
                    self.zone_schedule[i,j] = (self.zone1_schedule[i,j]*self.zone[0,0]+self.zone2_schedule[i,j]*self.zone[0,1]+self.zone3_schedule[i,j]*self.zone[0,2]+self.zone4_schedule[i,j]*self.zone[0,3]+self.zone5_schedule[i,j]*self.zone[0,4]+self.zone6_schedule[i,j]*self.zone[0,5]+self.zone7_schedule[i,j]*self.zone[0,6]+self.zone8_schedule[i,j]*self.zone[0,7]+self.zone9_schedule[i,j]*self.zone[0,8]+self.zone10_schedule[i,j]*self.zone[0,9])/np.asarray(self.totalArea) 
##            # Aggregated schedule value
##            self.zone_schedule = (self.zone1_schedule*self.zone[0,0]+self.zone2_schedule*self.zone[0,1]+self.zone3_schedule*self.zone[0,2]+self.zone4_schedule*self.zone[0,3]+self.zone5_schedule*self.zone[0,4]+self.zone6_schedule*self.zone[0,5]+self.zone7_schedule*self.zone[0,6]+self.zone8_schedule*self.zone[0,7]+self.zone9_schedule*self.zone[0,8]+self.zone10_schedule*self.zone[0,9])/self.totalArea #Schedule density * area

            # Internal gains
            for i in range(10):
                if self.zone[1,i] != 0:
                    self.totalOccupants  += self.zone[0,i]*self.zone[2,i]/self.zone[1,i] # area * (metabolic rate (W/person) * 1/(occupant density (m2/person)
                    self.standard_OA     += self.zone[5,i]*self.zone[0,i]/self.zone[1,i]
                    self.TotalOccupants2 += self.zone[0,i]/self.zone[1,i]                # Total number of occupants
                if self.zone[3,i] != 0: 
                    self.totalAppliance  += self.zone[0,i]*self.zone[3,i]
                if self.zone[4,i] != 0: 
                    self.totalLighting   += self.zone[0,i]*self.zone[4,i]
        
            self.totalOccupants /= self.totalArea
            self.totalAppliance /= self.totalArea
            self.totalLighting /= self.totalArea

        # Minimum heating set point
        self.hs_unoccupied = min(float(np.amin(self.setPoint[:,0],axis=0)),float(np.amin(self.setPoint[:,1],axis=0)))

        # garage
        self.garage_appliance /= self.totalArea
        self.garage_lighting  /= self.totalArea
        
    def TransmissionHeatTransfer(self):
                
        if self.right_string[1] == 'Very Light: 80,000 * Af':
            self.EvenlopeHeatCapacity=80000; self.AmFactor=2.5
        elif self.right_string[1] == 'Light : 110,000 * Af':
            self.EvenlopeHeatCapacity=110000; self.AmFactor=2.5
        elif self.right_string[1] == 'Medium: 165,000 * Af':
            self.EvenlopeHeatCapacity=165000; self.AmFactor=2.5
        elif self.right_string[1] == 'Heavy: 260,000 * Af':
            self.EvenlopeHeatCapacity=260000; self.AmFactor=3
        elif self.right_string[1] == 'Very heavy: 370,000 * Af':
            self.EvenlopeHeatCapacity=370000; self.AmFactor=3.5
            
    def VentilationAirFlowandVentilationHeatTransfer(self):
        self.ventSupply  = self.standard_OA*3.6/self.totalArea
        self.ventExhaust = self.standard_OA*3.6/self.totalArea
        self.qv_min      = 30*self.TotalOccupants2/self.totalArea

        if self.right_string[6] == 'No exhaust air recirculation':
            self.ventRecirculation = 1
        elif self.right_string[6] == 'Exhaust air recirculation 20%':
            self.ventRecirculation = 0.8
        elif self.right_string[6] in ['Exhaust air recirculation  40%', 'Exhaust air recirculation 40%']:
            self.ventRecirculation = 0.6
        elif self.right_string[6] == 'Exhaust air recirculation  60%':
            self.ventRecirculation = 0.4
        else:
            self.ventRecirculation = float(self.right_string[6]) 

        if self.right_string[5] == 'No heat recovery':
            self.HR_efficiency = 0
        elif self.right_string[5] == 'Heat exchange plates or pipes (0.65)':
            self.HR_efficiency = 0.65
        elif self.right_string[5] == 'Two-elements-system (0.6)':
            self.HR_efficiency = 0.6
        elif self.right_string[5] == 'Loading cold with air-conditioning (0.4)':
            self.HR_efficiency = 0.4
        elif self.right_string[5] == 'Heat-pipes (0.6)':
            self.HR_efficiency = 0.6
        elif self.right_string[5] == 'Slowly rotating or intermittent heat exchangers (0.7)':
            self.HR_efficiency = 0.7
        else:
            self.HR_efficiency = float(self.right_string[5])
            
        if self.right_string[0] == 'Open terrain':
            self.vsite = 1
        elif self.right_string[0] == 'Country':
            self.vsite = 0.9
        elif self.right_string[0] == 'Urban / City':
            self.vsite = 0.8

    def BEMSystem(self):
        if self.left_numeric[11,0] == 1:
            self.f_BAC_hc=1.51; self.f_BAC_e=1.1
        elif self.left_numeric[11,0] == 2:
            self.f_BAC_hc=1; self.f_BAC_e=1
        elif self.left_numeric[11,0] == 3:
            self.f_BAC_hc=0.8; self.f_BAC_e=0.93
        elif self.left_numeric[11,0] == 4:
            self.f_BAC_hc=0.7; self.f_BAC_e=0.87
            
    def CoolingandHeatingSystemEnergy(self):
        if int(self.right_string[3][0:2]) == 1:
            self.f_waste=0; self.a_heat=0.08; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 2:
            self.f_waste=0; self.a_heat=0.25; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 4:
            self.f_waste=0; self.a_heat=0.36; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 5:
            self.f_waste=0.03; self.a_heat=0.08; self.a_cool=0.01
        elif int(self.right_string[3][0:2]) == 6:
            self.f_waste=0; self.a_heat=0.08; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 7:
            self.f_waste=0; self.a_heat=0.25; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 8:
            self.f_waste=0.04; self.a_heat=0; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 9:
            self.f_waste=0; self.a_heat=0.36; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 10:
            self.f_waste=0.03; self.a_heat=0.08; self.a_cool=0.01
        elif int(self.right_string[3][0:2]) == 11:
            self.f_waste=0; self.a_heat=0.08; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 12:
            self.f_waste=0; self.a_heat=0.25; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 13:
            self.f_waste=0.08; self.a_heat=0; self.a_cool=0.01
        elif int(self.right_string[3][0:2]) == 14:
            self.f_waste=0.03; self.a_heat=0.08; self.a_cool=0.01
        elif int(self.right_string[3][0:2]) == 15:
            self.f_waste=0; self.a_heat=0.08; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 16:
            self.f_waste=0; self.a_heat=0.25; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 17:
            self.f_waste=0.03; self.a_heat=0.08; self.a_cool=0.01
        elif int(self.right_string[3][0:2]) == 18:
            self.f_waste=0; self.a_heat=0.08; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 19:
            self.f_waste=0; self.a_heat=0.25; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 20:
            self.f_waste=0.04; self.a_heat=0; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 21:
            self.f_waste=0; self.a_heat=0.36; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 22:
            self.f_waste=0.03; self.a_heat=0.08; self.a_cool=0.01
        elif int(self.right_string[3][0:2]) == 23:
            self.f_waste=0; self.a_heat=0.08; self.a_cool=0
        elif int(self.right_string[3][0:2]) == 24:
            self.f_waste=0; self.a_heat=0.25; self.a_cool=0
        elif int(self.right_string[3][0:2]) >= 25 and int(self.right_string[3][0:2])<= 27:
            self.f_waste=0.04; self.a_heat=0.08; self.a_cool=0.01
        elif int(self.right_string[3][0:2]) == 28:
            self.f_waste=0.08; self.a_heat=0; self.a_cool=0.01
        elif int(self.right_string[3][0:2]) >= 29 and int(self.right_string[3][0:2]) <= 34:
            self.f_waste=0.04; self.a_heat=0.08; self.a_cool=0.01
               
    def FanEnergy(self):
        self.T_supply_h = (float(np.amax(self.setPoint, axis=0)[0]))+7 
        self.T_supply_c = (float(np.amin(self.setPoint, axis=0)[2]))-7

    def PumpSystemEnergy(self):
        if self.right_string[8] == 'No pump for heating':
            self.fcntrl_heat = 0
        elif self.right_string[8] == 'Automatic control more than 50%':
            self.fcntrl_heat = 0.5
        elif self.right_string[8] == 'All other cases':
            self.fcntrl_heat = 1
            
        if self.right_string[7] == 'No pump for cooling':
            self.fcntrl_cool = 0
        elif self.right_string[7] == 'Automatic control more than 50%':
            self.fcntrl_cool = 0.5
        elif self.right_string[7] == 'All other cases':
            self.fcntrl_cool = 1

        self.pump_Equip[12,0] = 8*(self.fcntrl_heat*self.totalArea+self.fcntrl_cool*self.totalArea)

        for i in range(12):
            self.pump_Equip[i,0] = self.pump_Equip[12,0]*(self.constants[i]/self.constants[12])

        self.pump_Equip[0:12,1] = self.pump_Equip[0:12,0]/3.6
        self.pump_Equip[12,1] = float(self.pump_Equip[0:12,1].sum())

    def DHWandSolarWaterHeating(self):

        self.hotWaterDemand = np.dot(self.zone[0,:], self.zone[6,:].T)
            
        if self.right_string[9] == 'All Taps Within 3m from Heat Generation':
            self.effi_sys_DHW = 1 
        elif self.right_string[9] == 'Taps More Than 3m from Heat Generation':
            self.effi_sys_DHW = 0.8
        elif self.right_string[9] == 'Circulation system or Unknown':
            self.effi_sys_DHW = 0.6

        if self.right_string[10] == 'Electric (0.75)':
            self.effi_gen_DHW = 0.75
        elif self.right_string[10] == 'VR-Boiler (0.61)':
            self.effi_gen_DHW = 0.61
        elif self.right_string[10] == 'Gas Boiler, HR-Boiler (0.75)':
            self.effi_gen_DHW = 0.75
        elif self.right_string[10] == 'Co-Generation (0.9)':
            self.effi_gen_DHW = 0.90
        elif self.right_string[10] == 'District Heating (0.9)':
            self.effi_gen_DHW = 0.90
        elif self.right_string[10] == 'Heat Pump (1.4)':
            self.effi_gen_DHW = 1.4
        elif self.right_string[10] == 'Steam (0.61)':
            self.effi_gen_DHW = 0.61
        else:
            self.effi_gen_DHW = float(self.right_string[10])            

        self.Qdem_kWh = self.hotWaterDemand*50*4.18/1000/3.6      
        self.total_DHW_system = 12*self.Qdem_kWh/self.effi_sys_DHW
        
    def hourly_BEM(self):
        self.Overall_Array[:,1:26] = 0
        self.Overall_Array[:, 27:] = 0
        # other coefficients
        self.Q_heat_nd = np.zeros((13,1))
        self.Q_cool_nd = np.zeros((13,1))
        self.Htr_w=(np.sum(self.envelope[0:8,2])+self.envelope[9,2])*self.material[4,0]+self.envelope[8,2]*self.material[4,0]+(np.sum(self.envelope[0:8,7])+self.envelope[9,7])*self.material[5,0]+self.envelope[8,7]*self.material[5,0]
        self.Htr_op=(np.sum(self.envelope[0:8,0])+self.envelope[9,0])*self.material[2,0]+self.envelope[8,0]*self.material[0,0]+(np.sum(self.envelope[0:8,1])+self.envelope[9,0])*self.material[3,0]+self.envelope[8,0]*self.material[1,0] 

        self.Htr_w_Af  = self.Htr_w/self.totalArea # V7 
        self.Htr_op_Af = self.Htr_op/self.totalArea # V8
        self.Htr_total = self.Htr_w + self.Htr_op # V6
        
        self.H_es      = self.Htr_w_Af # V10
        self.Htr_ms    = 9.1*self.AmFactor # V12
        self.Htr_em    = 1/(1/self.Htr_op_Af-1/self.Htr_ms) # V11 
                
        self.Prs       = (1-self.AmFactor/4.5-self.H_es/40.95) # 40.95 = 9.1*4.5 # V15 
        self.Prm       = self.AmFactor/4.5 # V16 
            
        # 2. Solar heat gain (Glazing & Opaque)
        # 2.1 Rse
        self.Rse[self.weatherData[:,1] <= 1.5] = .08
        self.Rse[(self.weatherData[:,1] > 1.5) & (self.weatherData[:,1] <= 2.5)] = .06
        self.Rse[(self.weatherData[:,1] > 2.5) & (self.weatherData[:,1] <= 3.5)] = .05
        self.Rse[(self.weatherData[:,1] > 3.5) & (self.weatherData[:,1] <= 4.5)] = .04
        self.Rse[(self.weatherData[:,1] > 4.5) & (self.weatherData[:,1] <= 6.5)] = .04
        self.Rse[(self.weatherData[:,1] > 6) & (self.weatherData[:,1] <= 8.5)] = .03
        self.Rse[self.weatherData[:,1] > 8.5] = .02
        
        # 2.2 "CALC_H" Sheet preparation
        for i in range(9):
            self.glazing1[0,i] = self.envelope[i,2]
            self.glazing1[1,i] = self.envelope[i,3]
            self.glazing1[2,i] = self.envelope[i,4]
            self.glazing1[3,i] = self.envelope[i,5]
            self.glazing1[4,i] = self.envelope[i,6]

            self.glazing2[0,i] = self.envelope[i,7]
            self.glazing2[1,i] = self.envelope[i,8]
            self.glazing2[2,i] = self.envelope[i,9]
            self.glazing2[3,i] = self.envelope[i,10]
            self.glazing2[4,i] = self.envelope[i,11]
            
            if i == 8: # roof
                self.glazing1[5,i] = 1.0
                self.glazing2[5,i] = 1.0
                
                self.opaque1[1,i] = 1.0
                self.opaque1[3,i] = self.material[0,0]
                self.opaque1[4,i] = self.material[0,1]
                self.opaque1[5,i] = self.material[0,2]
                self.opaque1[6,i] = 5*self.material[0,2]

                self.opaque2[1,i] = 1.0
                self.opaque2[3,i] = self.material[1,0]
                self.opaque2[4,i] = self.material[1,1]
                self.opaque2[5,i] = self.material[1,2]
                self.opaque2[6,i] = 5*self.material[1,2]
            else: 
                self.glazing1[5,i] = 0.5
                self.glazing2[5,i] = 0.5
                
                self.opaque1[1,i] = 0.5
                self.opaque1[3,i] = self.material[2,0]
                self.opaque1[4,i] = self.material[2,1]
                self.opaque1[5,i] = self.material[2,2]
                self.opaque1[6,i] = 5*self.material[2,2]

                self.opaque2[1,i] = 0.5
                self.opaque2[3,i] = self.material[3,0]
                self.opaque2[4,i] = self.material[3,1]
                self.opaque2[5,i] = self.material[3,2]
                self.opaque2[6,i] = 5*self.material[3,2]
            
            self.glazing1[7,i] = self.material[4,0]
            self.glazing1[8,i] = 0.3
            self.glazing1[9,i] = self.material[4,2]
            self.glazing1[10,i] = 5*self.material[4,2]
            self.glazing1[6,i] = self.Rse[0,0]*self.glazing1[0,i]*self.glazing1[7,i]*self.glazing1[10,i]*11

            self.glazing2[7,i] = self.material[5,0]
            self.glazing2[8,i] = 0.3
            self.glazing2[9,i] = self.material[5,2]
            self.glazing2[10,i] = 5*self.material[5,2]
            self.glazing2[6,i] = self.glazing2[0,i]*self.glazing2[7,i]*self.glazing2[10,i]*11*self.Rse[0,0]

            self.opaque1[0,i] = self.envelope[i,0]
            self.opaque1[2,i] = self.opaque1[0,i]*self.opaque1[3,i]*self.opaque1[6,i]*self.Rse[0,0]*11

            self.opaque2[0,i] = self.envelope[i,1]
            self.opaque2[2,i] = self.opaque2[0,i]*self.opaque2[3,i]*self.opaque2[6,i]*self.Rse[0,0]*11
                                                               
        # 2.3 calculate the overall array
##______2
        for i in range(8760):
            if self.weatherData[i,11] > 0 and self.weatherData[i,11] < 90:
                self.heatgainGlazing1[i,0] = (-0.000003*np.power(self.weatherData[i,11],3)+0.0002*np.power(self.weatherData[i,11],2)-0.0053*self.weatherData[i,11]+0.9986)*self.material[4,3]
                self.heatgainGlazing2[i,0] = (-0.000003*np.power(self.weatherData[i,11],3)+0.0002*np.power(self.weatherData[i,11],2)-0.0053*self.weatherData[i,11]+0.9986)*self.material[5,3]
            else:
                self.heatgainGlazing1[i,0] = 0

            # glazing 1
            # Overhang 1
            for j in range(9): # Nine orientations
                if self.glazing1[1,j] != 0:
                    if j == 0: # S
                        if self.glazing1[1,j] == 30:
                            self.SRFOverhang1 = self.SRF_overhang[i,0]
                        elif self.glazing1[1,j] == 45:
                            self.SRFOverhang1 = self.SRF_overhang[i,8]
                        elif self.glazing1[1,j] == 60:
                            self.SRFOverhang1 = self.SRF_overhang[i,16]

                    elif j == 1: # SE
                        if self.glazing1[1,j] == 30:
                            self.SRFOverhang1 = self.SRF_overhang[i,1]
                        elif self.glazing1[1,j] == 45:
                            self.SRFOverhang1 = self.SRF_overhang[i,9]
                        elif self.glazing1[1,j] == 60:
                            self.SRFOverhang1 = self.SRF_overhang[i,17]

                    elif j == 2: # E
                        if self.glazing1[1,j] == 30:
                            self.SRFOverhang1 = self.SRF_overhang[i,2]
                        elif self.glazing1[1,j] == 45:
                            self.SRFOverhang1 = self.SRF_overhang[i,10]
                        elif self.glazing1[1,j] == 60:
                            self.SRFOverhang1 = self.SRF_overhang[i,18]

                    elif j == 3: # NE
                        if self.glazing1[1,j] == 30:
                            self.SRFOverhang1 = self.SRF_overhang[i,3]
                        elif self.glazing1[1,j] == 45:
                            self.SRFOverhang1 = self.SRF_overhang[i,11]
                        elif self.glazing1[1,j] == 60:
                            self.SRFOverhang1 = self.SRF_overhang[i,19]

                    elif j == 4: # N
                        if self.glazing1[1,j] == 30:
                            self.SRFOverhang1 = self.SRF_overhang[i,4]
                        elif self.glazing1[1,j] == 45:
                            self.SRFOverhang1 = self.SRF_overhang[i,12]
                        elif self.glazing1[1,j] == 60:
                            self.SRFOverhang1 = self.SRF_overhang[i,20]

                    elif j == 5: # NW
                        if self.glazing1[1,j] == 30:
                            self.SRFOverhang1 = self.SRF_overhang[i,5]
                        elif self.glazing1[1,j] == 45:
                            self.SRFOverhang1 = self.SRF_overhang[i,13]
                        elif self.glazing1[1,j] == 60:
                            self.SRFOverhang1 = self.SRF_overhang[i,21]

                    elif j == 6: # W
                        if self.glazing1[1,j] == 30:
                            self.SRFOverhang1 = self.SRF_overhang[i,6]
                        elif self.glazing1[1,j] == 45:
                            self.SRFOverhang1 = self.SRF_overhang[i,14]
                        elif self.glazing1[1,j] == 60:
                            self.SRFOverhang1 = self.SRF_overhang[i,22]

                    elif j == 7: # SW
                        if self.glazing1[1,j] == 30:
                            self.SRFOverhang1 = self.SRF_overhang[i,7]
                        elif self.glazing1[1,j] == 45:
                            self.SRFOverhang1 = self.SRF_overhang[i,15]
                        elif self.glazing1[1,j] == 60:
                            self.SRFOverhang1 = self.SRF_overhang[i,23]

                # Fin 1
                if self.glazing1[2,j] != 0:
                    if j == 0: # S
                        if self.glazing1[2,j] == 30:
                            self.SRFFin1 = self.SRF_fin[i,0]
                        elif self.glazing1[2,j] == 45:
                            self.SRFFin1 = self.SRF_fin[i,8]
                        elif self.glazing1[2,j] == 60:
                            self.SRFFin1 = self.SRF_fin[i,16]

                    elif j == 1: # SE
                        if self.glazing1[2,j] == 30:
                            self.SRFFin1 = self.SRF_fin[i,1]
                        elif self.glazing1[2,j] == 45:
                            self.SRFFin1 = self.SRF_fin[i,9]
                        elif self.glazing1[2,j] == 60:
                            self.SRFFin1 = self.SRF_fin[i,17]

                    elif j == 2: # E
                        if self.glazing1[2,j] == 30:
                            self.SRFFin1 = self.SRF_fin[i,2]
                        elif self.glazing1[2,j] == 45:
                            self.SRFFin1 = self.SRF_fin[i,10]
                        elif self.glazing1[2,j] == 60:
                            self.SRFFin1 = self.SRF_fin[i,18]

                    elif j == 3: # NE
                        if self.glazing1[2,j] == 30:
                            self.SRFFin1 = self.SRF_fin[i,3]
                        elif self.glazing1[2,j] == 45:
                            self.SRFFin1 = self.SRF_fin[i,11]
                        elif self.glazing1[2,j] == 60:
                            self.SRFFin1 = self.SRF_fin[i,19]

                    elif j == 4: # N
                        if self.glazing1[2,j] == 30:
                            self.SRFFin1 = self.SRF_fin[i,4]
                        elif self.glazing1[2,j] == 45:
                            self.SRFFin1 = self.SRF_fin[i,12]
                        elif self.glazing1[2,j] == 60:
                            self.SRFFin1 = self.SRF_fin[i,20]

                    elif j == 5: # NW
                        if self.glazing1[2,j] == 30:
                            self.SRFFin1 = self.SRF_fin[i,5]
                        elif self.glazing1[2,j] == 45:
                            self.SRFFin1 = self.SRF_fin[i,13]
                        elif self.glazing1[2,j] == 60:
                            self.SRFFin1 = self.SRF_fin[i,21]

                    elif j == 6: # W
                        if self.glazing1[2,j] == 30:
                            self.SRFFin1 = self.SRF_fin[i,6]
                        elif self.glazing1[2,j] == 45:
                            self.SRFFin1 = self.SRF_fin[i,14]
                        elif self.glazing1[2,j] == 60:
                            self.SRFFin1 = self.SRF_fin[i,22]

                    elif j == 7: # SW
                        if self.glazing1[2,j] == 30:
                            self.SRFFin1 = self.SRF_fin[i,7]
                        elif self.glazing1[2,j] == 45:
                            self.SRFFin1 = self.SRF_fin[i,15]
                        elif self.glazing1[2,j] == 60:
                            self.SRFFin1 = self.SRF_fin[i,23]

                # Horizon 1
                if self.glazing1[3,j] != 0:
                    if j == 0: # S
                        if self.glazing1[3,j] == 10:
                            self.SRFHor1 = self.SRF_horizon[i,0]
                        elif self.glazing1[3,j] == 20:
                            self.SRFHor1 = self.SRF_horizon[i,8]
                        elif self.glazing1[3,j] == 30:
                            self.SRFHor1 = self.SRF_horizon[i,16]
                        elif self.glazing1[3,j] == 40:
                            self.SRFHor1 = self.SRF_horizon[i,24]
                        elif self.glazing1[3,j] == 50:
                            self.SRFHor1 = self.SRF_horizon[i,32]
                        elif self.glazing1[3,j] == 60:
                            self.SRFHor1 = self.SRF_horizon[i,40]

                    elif j == 1: # SE
                        if self.glazing1[3,j] == 10:
                            self.SRFHor1 = self.SRF_horizon[i,1]
                        elif self.glazing1[3,j] == 20:
                            self.SRFHor1 = self.SRF_horizon[i,9]
                        elif self.glazing1[3,j] == 30:
                            self.SRFHor1 = self.SRF_horizon[i,17]
                        elif self.glazing1[3,j] == 40:
                            self.SRFHor1 = self.SRF_horizon[i,25]
                        elif self.glazing1[3,j] == 50:
                            self.SRFHor1 = self.SRF_horizon[i,33]
                        elif self.glazing1[3,j] == 60:
                            self.SRFHor1 = self.SRF_horizon[i,41]

                    elif j == 2: # E
                        if self.glazing1[3,j] == 10:
                            self.SRFHor1 = self.SRF_horizon[i,2]
                        elif self.glazing1[3,j] == 20:
                            self.SRFHor1 = self.SRF_horizon[i,10]
                        elif self.glazing1[3,j] == 30:
                            self.SRFHor1 = self.SRF_horizon[i,18]
                        elif self.glazing1[3,j] == 40:
                            self.SRFHor1 = self.SRF_horizon[i,26]
                        elif self.glazing1[3,j] == 50:
                            self.SRFHor1 = self.SRF_horizon[i,34]
                        elif self.glazing1[3,j] == 60:
                            self.SRFHor1 = self.SRF_horizon[i,42]

                    elif j == 3: # NE
                        if self.glazing1[3,j] == 10:
                            self.SRFHor1 = self.SRF_horizon[i,3]
                        elif self.glazing1[3,j] == 20:
                            self.SRFHor1 = self.SRF_horizon[i,11]
                        elif self.glazing1[3,j] == 30:
                            self.SRFHor1 = self.SRF_horizon[i,19]
                        elif self.glazing1[3,j] == 40:
                            self.SRFHor1 = self.SRF_horizon[i,27]
                        elif self.glazing1[3,j] == 50:
                            self.SRFHor1 = self.SRF_horizon[i,35]
                        elif self.glazing1[3,j] == 60:
                            self.SRFHor1 = self.SRF_horizon[i,43]

                    elif j == 4: # N
                        if self.glazing1[3,j] == 10:
                            self.SRFHor1 = self.SRF_horizon[i,4]
                        elif self.glazing1[3,j] == 20:
                            self.SRFHor1 = self.SRF_horizon[i,12]
                        elif self.glazing1[3,j] == 30:
                            self.SRFHor1 = self.SRF_horizon[i,20]
                        elif self.glazing1[3,j] == 40:
                            self.SRFHor1 = self.SRF_horizon[i,28]
                        elif self.glazing1[3,j] == 50:
                            self.SRFHor1 = self.SRF_horizon[i,36]
                        elif self.glazing1[3,j] == 60:
                            self.SRFHor1 = self.SRF_horizon[i,44]

                    elif j == 5: # NW
                        if self.glazing1[3,j] == 10:
                            self.SRFHor1 = self.SRF_horizon[i,5]
                        elif self.glazing1[3,j] == 20:
                            self.SRFHor1 = self.SRF_horizon[i,13]
                        elif self.glazing1[3,j] == 30:
                            self.SRFHor1 = self.SRF_horizon[i,21]
                        elif self.glazing1[3,j] == 40:
                            self.SRFHor1 = self.SRF_horizon[i,29]
                        elif self.glazing1[3,j] == 50:
                            self.SRFHor1 = self.SRF_horizon[i,37]
                        elif self.glazing1[3,j] == 60:
                            self.SRFHor1 = self.SRF_horizon[i,45]

                    elif j == 6: # W
                        if self.glazing1[3,j] == 10:
                            self.SRFHor1 = self.SRF_horizon[i,6]
                        elif self.glazing1[3,j] == 20:
                            self.SRFHor1 = self.SRF_horizon[i,14]
                        elif self.glazing1[3,j] == 30:
                            self.SRFHor1 = self.SRF_horizon[i,22]
                        elif self.glazing1[3,j] == 40:
                            self.SRFHor1 = self.SRF_horizon[i,30]
                        elif self.glazing1[3,j] == 50:
                            self.SRFHor1 = self.SRF_horizon[i,38]
                        elif self.glazing1[3,j] == 60:
                            self.SRFHor1 = self.SRF_horizon[i,46]

                    elif j == 7: # SW
                        if self.glazing1[3,j] == 10:
                            self.SRFHor1 = self.SRF_horizon[i,7]
                        elif self.glazing1[3,j] == 20:
                            self.SRFHor1 = self.SRF_horizon[i,15]
                        elif self.glazing1[3,j] == 30:
                            self.SRFHor1 = self.SRF_horizon[i,23]
                        elif self.glazing1[3,j] == 40:
                            self.SRFHor1 = self.SRF_horizon[i,31]
                        elif self.glazing1[3,j] == 50:
                            self.SRFHor1 = self.SRF_horizon[i,39]
                        elif self.glazing1[3,j] == 60:
                            self.SRFHor1 = self.SRF_horizon[i,47]

                self.heatgainGlazing1[i,j+1]=self.weatherData[i,j+2]*self.glazing1[0,j]*(self.SRFOverhang1*self.SRFFin1*self.SRFHor1*self.glazing1[4,j]*(1-self.glazing1[8,j])*self.heatgainGlazing1[i,0])-(self.glazing1[5,j]*(self.Rse[i,0]*self.glazing1[7,j]*self.glazing1[0,j]*self.glazing1[10,j]*11))
                self.SRFOverhang1 = self.SRFFin1 = self.SRFHor1=1

            # glazing 2
            # glazing 2 Overhang
                if self.glazing2[1,j] != 0:
                    if j == 0: # S
                        if self.glazing2[1,j] == 30:
                            self.SRFOverhang2 = self.SRF_overhang[i,0]
                        elif self.glazing2[1,j] == 45:
                            self.SRFOverhang2 = self.SRF_overhang[i,8]
                        elif self.glazing2[1,j] == 60:
                            self.SRFOverhang2 = self.SRF_overhang[i,16]

                    elif j == 1: # SE
                        if self.glazing2[1,j] == 30:
                            self.SRFOverhang2 = self.SRF_overhang[i,1]
                        elif self.glazing2[1,j] == 45:
                            self.SRFOverhang2 = self.SRF_overhang[i,9]
                        elif self.glazing2[1,j] == 60:
                            self.SRFOverhang2 = self.SRF_overhang[i,17]

                    elif j == 2: # E
                        if self.glazing2[1,j] == 30:
                            self.SRFOverhang2 = self.SRF_overhang[i,2]
                        elif self.glazing2[1,j] == 45:
                            self.SRFOverhang2 = self.SRF_overhang[i,10]
                        elif self.glazing2[1,j] == 60:
                            self.SRFOverhang2 = self.SRF_overhang[i,18]

                    elif j == 3: # NE
                        if self.glazing2[1,j] == 30:
                            self.SRFOverhang2 = self.SRF_overhang[i,3]
                        elif self.glazing2[1,j] == 45:
                            self.SRFOverhang2 = self.SRF_overhang[i,11]
                        elif self.glazing2[1,j] == 60:
                            self.SRFOverhang2 = self.SRF_overhang[i,19]

                    elif j == 4: # N
                        if self.glazing2[1,j] == 30:
                            self.SRFOverhang2 = self.SRF_overhang[i,4]
                        elif self.glazing2[1,j] == 45:
                            self.SRFOverhang2 = self.SRF_overhang[i,12]
                        elif self.glazing2[1,j] == 60:
                            self.SRFOverhang2 = self.SRF_overhang[i,20]

                    elif j == 5: # NW
                        if self.glazing2[1,j] == 30:
                            self.SRFOverhang2 = self.SRF_overhang[i,5]
                        elif self.glazing2[1,j] == 45:
                            self.SRFOverhang2 = self.SRF_overhang[i,13]
                        elif self.glazing2[1,j] == 60:
                            self.SRFOverhang2 = self.SRF_overhang[i,21]

                    elif j == 6: # W
                        if self.glazing2[1,j] == 30:
                            self.SRFOverhang2 = self.SRF_overhang[i,6]
                        elif self.glazing2[1,j] == 45:
                            self.SRFOverhang2 = self.SRF_overhang[i,14]
                        elif self.glazing2[1,j] == 60:
                            self.SRFOverhang2 = self.SRF_overhang[i,22]

                    elif j == 7: # SW
                        if self.glazing2[1,j] == 30:
                            self.SRFOverhang2 = self.SRF_overhang[i,7]
                        elif self.glazing2[1,j] == 45:
                            self.SRFOverhang2 = self.SRF_overhang[i,15]
                        elif self.glazing2[1,j] == 60:
                            self.SRFOverhang2 = self.SRF_overhang[i,23]

                # glazing 2 Fin
                if self.glazing2[2,j] != 0:
                    if j == 0: # S
                        if self.glazing2[2,j] == 30:
                            self.SRFFin2 = self.SRF_fin[i,0]
                        elif self.glazing2[2,j] == 45:
                            self.SRFFin2 = self.SRF_fin[i,8]
                        elif self.glazing2[2,j] == 60:
                            self.SRFFin2 = self.SRF_fin[i,16]

                    elif j == 1: # SE
                        if self.glazing2[2,j] == 30:
                            self.SRFFin2 = self.SRF_fin[i,1]
                        elif self.glazing2[2,j] == 45:
                            self.SRFFin2 = self.SRF_fin[i,9]
                        elif self.glazing2[2,j] == 60:
                            self.SRFFin2 = self.SRF_fin[i,17]

                    elif j == 2: # E
                        if self.glazing2[2,j] == 30:
                            self.SRFFin2 = self.SRF_fin[i,2]
                        elif self.glazing2[2,j] == 45:
                            self.SRFFin2 = self.SRF_fin[i,10]
                        elif self.glazing2[2,j] == 60:
                            self.SRFFin2 = self.SRF_fin[i,18]

                    elif j == 3: # NE
                        if self.glazing2[2,j] == 30:
                            self.SRFFin2 = self.SRF_fin[i,3]
                        elif self.glazing2[2,j] == 45:
                            self.SRFFin2 = self.SRF_fin[i,11]
                        elif self.glazing2[2,j] == 60:
                            self.SRFFin2 = self.SRF_fin[i,19]

                    elif j == 4: # N
                        if self.glazing2[2,j] == 30:
                            self.SRFFin2 = self.SRF_fin[i,4]
                        elif self.glazing2[2,j] == 45:
                            self.SRFFin2 = self.SRF_fin[i,12]
                        elif self.glazing2[2,j] == 60:
                            self.SRFFin2 = self.SRF_fin[i,20]

                    elif j == 5: # NW
                        if self.glazing2[2,j] == 30:
                            self.SRFFin2 = self.SRF_fin[i,5]
                        elif self.glazing2[2,j] == 45:
                            self.SRFFin2 = self.SRF_fin[i,13]
                        elif self.glazing2[2,j] == 60:
                            self.SRFFin2 = self.SRF_fin[i,21]

                    elif j == 6: # W
                        if self.glazing2[2,j] == 30:
                            self.SRFFin2 = self.SRF_fin[i,6]
                        elif self.glazing2[2,j] == 45:
                            self.SRFFin2 = self.SRF_fin[i,14]
                        elif self.glazing2[2,j] == 60:
                            self.SRFFin2 = self.SRF_fin[i,22]

                    elif j == 7: # SW
                        if self.glazing2[2,j] == 30:
                            self.SRFFin2 = self.SRF_fin[i,7]
                        elif self.glazing2[2,j] == 45:
                            self.SRFFin2 = self.SRF_fin[i,15]
                        elif self.glazing2[2,j] == 60:
                            self.SRFFin2 = self.SRF_fin[i,23]

                # glazing 2 Horizon
                if self.glazing2[3,j] != 0:
                    if j == 0: # S
                        if self.glazing2[3,j] == 10:
                            self.SRFHor2 = self.SRF_horizon[i,0]
                        elif self.glazing2[3,j] == 20:
                            self.SRFHor2 = self.SRF_horizon[i,8]
                        elif self.glazing2[3,j] == 30:
                            self.SRFHor2 = self.SRF_horizon[i,16]
                        elif self.glazing2[3,j] == 40:
                            self.SRFHor2 = self.SRF_horizon[i,24]
                        elif self.glazing2[3,j] == 50:
                            self.SRFHor2 = self.SRF_horizon[i,32]
                        elif self.glazing2[3,j] == 60:
                            self.SRFHor2 = self.SRF_horizon[i,40]

                    elif j == 1: # SE
                        if self.glazing2[3,j] == 10:
                            self.SRFHor2 = self.SRF_horizon[i,1]
                        elif self.glazing2[3,j] == 20:
                            self.SRFHor2 = self.SRF_horizon[i,9]
                        elif self.glazing2[3,j] == 30:
                            self.SRFHor2 = self.SRF_horizon[i,17]
                        elif self.glazing2[3,j] == 40:
                            self.SRFHor2 = self.SRF_horizon[i,25]
                        elif self.glazing2[3,j] == 50:
                            self.SRFHor2 = self.SRF_horizon[i,33]
                        elif self.glazing2[3,j] == 60:
                            self.SRFHor2 = self.SRF_horizon[i,41]

                    elif j == 2: # E
                        if self.glazing2[3,j] == 10:
                            self.SRFHor2 = self.SRF_horizon[i,2]
                        elif self.glazing2[3,j] == 20:
                            self.SRFHor2 = self.SRF_horizon[i,10]
                        elif self.glazing2[3,j] == 30:
                            self.SRFHor2 = self.SRF_horizon[i,18]
                        elif self.glazing2[3,j] == 40:
                            self.SRFHor2 = self.SRF_horizon[i,26]
                        elif self.glazing2[3,j] == 50:
                            self.SRFHor2 = self.SRF_horizon[i,34]
                        elif self.glazing2[3,j] == 60:
                            self.SRFHor2 = self.SRF_horizon[i,42]

                    elif j == 3: # NE
                        if self.glazing2[3,j] == 10:
                            self.SRFHor2 = self.SRF_horizon[i,3]
                        elif self.glazing2[3,j] == 20:
                            self.SRFHor2 = self.SRF_horizon[i,11]
                        elif self.glazing2[3,j] == 30:
                            self.SRFHor2 = self.SRF_horizon[i,19]
                        elif self.glazing2[3,j] == 40:
                            self.SRFHor2 = self.SRF_horizon[i,27]
                        elif self.glazing2[3,j] == 50:
                            self.SRFHor2 = self.SRF_horizon[i,35]
                        elif self.glazing2[3,j] == 60:
                            self.SRFHor2 = self.SRF_horizon[i,43]

                    elif j == 4: # N
                        if self.glazing2[3,j] == 10:
                            self.SRFHor2 = self.SRF_horizon[i,4]
                        elif self.glazing2[3,j] == 20:
                            self.SRFHor2 = self.SRF_horizon[i,12]
                        elif self.glazing2[3,j] == 30:
                            self.SRFHor2 = self.SRF_horizon[i,20]
                        elif self.glazing2[3,j] == 40:
                            self.SRFHor2 = self.SRF_horizon[i,28]
                        elif self.glazing2[3,j] == 50:
                            self.SRFHor2 = self.SRF_horizon[i,36]
                        elif self.glazing2[3,j] == 60:
                            self.SRFHor2 = self.SRF_horizon[i,44]

                    elif j == 5: # NW
                        if self.glazing2[3,j] == 10:
                            self.SRFHor2 = self.SRF_horizon[i,5]
                        elif self.glazing2[3,j] == 20:
                            self.SRFHor2 = self.SRF_horizon[i,13]
                        elif self.glazing2[3,j] == 30:
                            self.SRFHor2 = self.SRF_horizon[i,21]
                        elif self.glazing2[3,j] == 40:
                            self.SRFHor2 = self.SRF_horizon[i,29]
                        elif self.glazing2[3,j] == 50:
                            self.SRFHor2 = self.SRF_horizon[i,37]
                        elif self.glazing2[3,j] == 60:
                            self.SRFHor2 = self.SRF_horizon[i,45]

                    elif j == 6: # W
                        if self.glazing2[3,j] == 10:
                            self.SRFHor2 = self.SRF_horizon[i,6]
                        elif self.glazing2[3,j] == 20:
                            self.SRFHor2 = self.SRF_horizon[i,14]
                        elif self.glazing2[3,j] == 30:
                            self.SRFHor2 = self.SRF_horizon[i,22]
                        elif self.glazing2[3,j] == 40:
                            self.SRFHor2 = self.SRF_horizon[i,30]
                        elif self.glazing2[3,j] == 50:
                            self.SRFHor2 = self.SRF_horizon[i,38]
                        elif self.glazing2[3,j] == 60:
                            self.SRFHor2 = self.SRF_horizon[i,46]

                    elif j == 7: # SW
                        if self.glazing2[3,j] == 10:
                            self.SRFHor2 = self.SRF_horizon[i,7]
                        elif self.glazing2[3,j] == 20:
                            self.SRFHor2 = self.SRF_horizon[i,15]
                        elif self.glazing2[3,j] == 30:
                            self.SRFHor2 = self.SRF_horizon[i,23]
                        elif self.glazing2[3,j] == 40:
                            self.SRFHor2 = self.SRF_horizon[i,31]
                        elif self.glazing2[3,j] == 50:
                            self.SRFHor2 = self.SRF_horizon[i,39]
                        elif self.glazing2[3,j] == 60:
                            self.SRFHor2 = self.SRF_horizon[i,47]

                self.heatgainGlazing2[i,j+1]= self.weatherData[i,j+2]*self.glazing2[0,j]*(self.SRFOverhang2*self.SRFFin2*self.SRFHor2*self.glazing2[4,j]*(1-self.glazing2[8,j])*self.heatgainGlazing2[i,0])-(self.glazing2[5,j]*(self.Rse[i,0]*self.glazing2[7,j]*self.glazing2[0,j]*self.glazing2[10,j]*11))
                self.SRFOverhang2 = self.SRFFin2 = self.SRFHor2=1

            self.heatgainGlazing1[i,10] = np.sum(self.heatgainGlazing1[i,0:10])
            self.heatgainGlazing2[i,10] = np.sum(self.heatgainGlazing2[i,0:10])

            # Opaque 1, 2
            for j in range(9):
                self.heatgainOpaque1[i,j]=self.weatherData[i,j+2]*self.opaque1[0,j]*self.opaque1[3,j]*self.opaque1[4,j]*self.Rse[i,0]-(self.opaque1[1,j]*self.Rse[i,0]*self.opaque1[3,j]*self.opaque1[0,j]*self.opaque1[6,j]*11)
                self.heatgainOpaque2[i,j]=self.weatherData[i,j+2]*self.opaque2[0,j]*self.opaque2[3,j]*self.opaque2[4,j]*self.Rse[i,0]-(self.opaque2[1,j]*self.Rse[i,0]*self.opaque2[3,j]*self.opaque2[0,j]*self.opaque2[6,j]*11)

            self.heatgainOpaque1[i,9] = np.sum(self.heatgainOpaque1[i,0:9])
            self.heatgainOpaque2[i,9] = np.sum(self.heatgainOpaque2[i,0:9])

            if ((i+1)%24) == 0:
                self.Overall_Array[i,1] = int((i+1)/24) # nth day of the day
            else:
                self.Overall_Array[i,1] = int((i+1)/24)+1

            if (self.Overall_Array[i,1]%7)== 0: # nth of the week
                self.Overall_Array[i,2] = 7
            else:
                self.Overall_Array[i,2] = self.Overall_Array[i,1]%7

            if (self.Overall_Array[i,0]%24)== 0: # hour of the day
                self.Overall_Array[i,3] = 24
            else:
                self.Overall_Array[i,3] = self.Overall_Array[i,0]%24

            if self.Overall_Array[i,2] == 1:
                self.Overall_Array[i,4] = self.start_day_setup[0,0]
            elif self.Overall_Array[i,2] == 2:
                self.Overall_Array[i,4] = self.start_day_setup[1,0]
            elif self.Overall_Array[i,2] == 3:
                self.Overall_Array[i,4] = self.start_day_setup[2,0]
            elif self.Overall_Array[i,2] == 4:
                self.Overall_Array[i,4] = self.start_day_setup[3,0]
            elif self.Overall_Array[i,2] == 5:
                self.Overall_Array[i,4] = self.start_day_setup[4,0]
            elif self.Overall_Array[i,2] == 6:
                self.Overall_Array[i,4] = self.start_day_setup[5,0]
            elif self.Overall_Array[i,2] == 7:
                self.Overall_Array[i,4] = self.start_day_setup[6,0]

            ## Holiday
            if self.Overall_Array[i,1] in [1, 21, 147, 185, 245, 287, 315, 332, 333, 358, 359]:
                self.Overall_Array[i,4] = 0

            if i%24 == 0: # schedule + setpoint temp
                if self.Overall_Array[i,4] == 0: # Weekend
                    for j in range(24):
                        self.Overall_Array[i+j,5] = self.zone_schedule[j,1]
                        self.Overall_Array[i+j,6] = self.zone_schedule[j,3]
                        self.Overall_Array[i+j,7] = self.zone_schedule[j,5]

                        self.Overall_Array[i+j,36] = self.setPoint[j,1] # heating set point
                        self.Overall_Array[i+j,37] = self.setPoint[j,3] # cooling set point
                        self.Overall_Array[i+j,38] = self.weatherData[i+j,0]

                        self.garage_schedule_all[i+j,0] = self.garage_schedule[j,0] # garage appliance 
                        self.garage_schedule_all[i+j,2] = self.garage_schedule[j,2] # garage lighting 
                else:
                    for j in range(24):
                        self.Overall_Array[i+j,5] = self.zone_schedule[j,0]
                        self.Overall_Array[i+j,6] = self.zone_schedule[j,2]
                        self.Overall_Array[i+j,7] = self.zone_schedule[j,4]

                        self.Overall_Array[i+j,36] = self.setPoint[j,0] # heating set point
                        self.Overall_Array[i+j,37] = self.setPoint[j,2] # cooling set point
                        self.Overall_Array[i+j,38] = self.weatherData[i+j,0]

                        self.garage_schedule_all[i+j,1] = self.garage_schedule[j,1] # garage appliance 
                        self.garage_schedule_all[i+j,3] = self.garage_schedule[j,3] # garage lighting 

            if i == 0:
                self.Overall_Array[i,19] = self.Overall_Array[i,30] = self.Overall_Array[i,39] = self.Overall_Array[i,49] = self.hs_unoccupied
            else:
                self.Overall_Array[i,19] = self.Overall_Array[i,30] = self.Overall_Array[i,49] = self.Overall_Array[i-1,50]

            # Airflow: Min & Fresh Airflow: mechanical supply
            self.Overall_Array[i,55] = self.Overall_Array[i,5]*self.qv_min # Airflow Minimum
            self.Overall_Array[i,56] =(self.ventSupply*self.Overall_Array[i,5])*self.ventRecirculation
            self.Overall_Array[i,57] = self.Overall_Array[i,56]
            #self.Overall_Array[i,58] = sel.fOverall_Array[i,56] - self.Overall_Array[i,57]

            if self.right_string[4] == '3. Same as 2, with fully natural fresh air supply (always)':
                self.Overall_Array[i,59] = 0
            else:
                self.Overall_Array[i,59] = self.Overall_Array[i,56]*(1-self.HR_efficiency)

            if i == 0:
                self.Overall_Array[i,60] = max(0.0146*self.left_numeric[8,0]*(0.7*self.left_numeric[1,0]*abs(self.weatherData[i,0]- self.hs_unoccupied))**0.667,0.001)
            else:
                self.Overall_Array[i,60] = max(0.0146*self.left_numeric[8,0]*(0.7*self.left_numeric[1,0]*abs(self.weatherData[i,0]- self.Overall_Array[i-1,39]))**0.667,0.001)

            self.Overall_Array[i,61] = 0.0769*self.left_numeric[8,0]*(0.75*self.vsite*self.weatherData[i,1]**2)**0.667
            self.Overall_Array[i,62] = max(self.Overall_Array[i,60],self.Overall_Array[i,61]) + 0.14*self.Overall_Array[i,60]*self.Overall_Array[i,61]/self.left_numeric[8,0]
            self.Overall_Array[i,63] = max(self.Overall_Array[i,62],(self.Overall_Array[i,60]*abs(self.Overall_Array[i,58])/2+self.Overall_Array[i,61]*abs(self.Overall_Array[i,58])*2/3)/(self.Overall_Array[i,60]+self.Overall_Array[i,61]))
            self.Overall_Array[i,64] = max(0,-self.Overall_Array[i,58])+ self.Overall_Array[i,62]

            if self.right_string[4] == '3. Same as 2, with fully natural fresh air supply (always)':
                self.Overall_Array[i,65] = self.Overall_Array[i,55] + self.Overall_Array[i,64]
            else:
                self.Overall_Array[i,65] = self.Overall_Array[i,59] + self.Overall_Array[i,64]

            # natural ventilation
            if self.NV_included == True and 3624 < i < 6551:
                if abs(self.NV_effective_angle-self.weatherData[i,15])>180:
                    self.Qw = (0.55-((abs(self.NV_effective_angle-self.weatherData[i,15])-180)/180)*0.25)*self.NV_width*self.NV_height*self.weatherData[i,1]
                else:
                    self.Qw = (0.55-((abs(self.NV_effective_angle-self.weatherData[i,15]))/180)*0.25)*self.NV_width*self.NV_height*self.weatherData[i,1]

                self.Qs = (0.4+0.0045*abs(self.weatherData[i,0]-self.Overall_Array[i,53]))*self.NV_width*self.NV_height*sqrt(2*9.81*0.5*self.NV_height*abs(self.Overall_Array[i,53]-self.weatherData[i,0])/(self.Overall_Array[i,53]+273))

                if self.Overall_Array[i-1,53] > self.weatherData[i,0]:
                    self.NV_openingRatio = 1
                else:
                    self.NV_openingRatio = 0

                self.QNV_total = sqrt(self.Qs**2 + self.Qw**2)*3600/self.totalArea*self.NV_openingRatio
##                print(f"i: {i}, Qw: {self.Qw}, Qs:{self.Qs}, NV_openingRatio: {self.NV_openingRatio}, QNV_total: {self.QNV_total}")

                self.Overall_Array[i,65] += self.QNV_total

            self.Overall_Array[i,66] = self.Overall_Array[i,64]*self.totalArea/self.left_numeric[0]
            self.Overall_Array[i,67] = self.Overall_Array[i,59]*self.totalArea/self.left_numeric[0]

            if self.right_string[4] == '3. Same as 2, with fully natural fresh air supply (always)':
                self.Overall_Array[i,68] = self.Overall_Array[i,55]*self.totalArea/self.left_numeric[0]
            else:
                self.Overall_Array[i,68] = 0

            self.Overall_Array[i,69] = self.Overall_Array[i,65]*self.totalArea/self.left_numeric[0]

            self.Overall_Array[i,72] = self.Overall_Array[i,65]
            self.Overall_Array[i,73] = self.left_numeric[7,0]*3600/1000/self.totalArea*self.Overall_Array[i,5]
            self.Overall_Array[i,74] = self.left_numeric[7,0]*3600/1000/self.totalArea*self.Overall_Array[i,5]
### where is lighting
            if self.monthly_internal_heat_gain_bool == False:
                self.Overall_Array[i,77] = self.Overall_Array[i,5]*self.totalOccupants
                self.Overall_Array[i,78] = self.Overall_Array[i,6]*self.totalAppliance

            else:
                if 1 <= self.Overall_Array[i,0] <= 744: # Jan
                    self.Overall_Array[i,77] = self.Overall_Array[i,5]*self.monthly_internal_heat_gain[0,0]
                    self.Overall_Array[i,78] = self.Overall_Array[i,6]*self.monthly_internal_heat_gain[0,1]
                    self.totalLighting       = self.monthly_internal_heat_gain[0,2]
                elif 745 <= self.Overall_Array[i,0] <= 1416: # Feb
                    self.Overall_Array[i,77] = self.Overall_Array[i,5]*self.monthly_internal_heat_gain[1,0]
                    self.Overall_Array[i,78] = self.Overall_Array[i,6]*self.monthly_internal_heat_gain[1,1]
                    self.totalLighting       = self.monthly_internal_heat_gain[1,2]
                elif 1417 <= self.Overall_Array[i,0] <= 2160: # Mar
                    self.Overall_Array[i,77] = self.Overall_Array[i,5]*self.monthly_internal_heat_gain[2,0]
                    self.Overall_Array[i,78] = self.Overall_Array[i,6]*self.monthly_internal_heat_gain[2,1]
                    self.totalLighting       = self.monthly_internal_heat_gain[2,2]
                elif 2161 <= self.Overall_Array[i,0] <= 2880: # Apr
                    self.Overall_Array[i,77] = self.Overall_Array[i,5]*self.monthly_internal_heat_gain[3,0]
                    self.Overall_Array[i,78] = self.Overall_Array[i,6]*self.monthly_internal_heat_gain[3,1]
                    self.totalLighting       = self.monthly_internal_heat_gain[3,2]
                elif 2881 <= self.Overall_Array[i,0] <= 3624: # May
                    self.Overall_Array[i,77] = self.Overall_Array[i,5]*self.monthly_internal_heat_gain[4,0]
                    self.Overall_Array[i,78] = self.Overall_Array[i,6]*self.monthly_internal_heat_gain[4,1]
                    self.totalLighting       = self.monthly_internal_heat_gain[4,2]
                elif 3625 <= self.Overall_Array[i,0] <= 4344: # Jun
                    self.Overall_Array[i,77] = self.Overall_Array[i,5]*self.monthly_internal_heat_gain[5,0]
                    self.Overall_Array[i,78] = self.Overall_Array[i,6]*self.monthly_internal_heat_gain[5,1]
                    self.totalLighting       = self.monthly_internal_heat_gain[5,2]
                elif 4345 <= self.Overall_Array[i,0] <= 5088: # Jul
                    self.Overall_Array[i,77] = self.Overall_Array[i,5]*self.monthly_internal_heat_gain[6,0]
                    self.Overall_Array[i,78] = self.Overall_Array[i,6]*self.monthly_internal_heat_gain[6,1]
                    self.totalLighting       = self.monthly_internal_heat_gain[6,2]
                elif 5089 <= self.Overall_Array[i,0] <= 5832: # Aug
                    self.Overall_Array[i,77] = self.Overall_Array[i,5]*self.monthly_internal_heat_gain[7,0]
                    self.Overall_Array[i,78] = self.Overall_Array[i,6]*self.monthly_internal_heat_gain[7,1]
                    self.totalLighting       = self.monthly_internal_heat_gain[7,2]
                elif 5833 <= self.Overall_Array[i,0] <= 6552: # Sep
                    self.Overall_Array[i,77] = self.Overall_Array[i,5]*self.monthly_internal_heat_gain[8,0]
                    self.Overall_Array[i,78] = self.Overall_Array[i,6]*self.monthly_internal_heat_gain[8,1]
                    self.totalLighting       = self.monthly_internal_heat_gain[8,2]
                elif 6553 <= self.Overall_Array[i,0] <= 7296: # Oct
                    self.Overall_Array[i,77] = self.Overall_Array[i,5]*self.monthly_internal_heat_gain[9,0]
                    self.Overall_Array[i,78] = self.Overall_Array[i,6]*self.monthly_internal_heat_gain[9,1]
                    self.totalLighting       = self.monthly_internal_heat_gain[9,2]
                elif 7297 <= self.Overall_Array[i,0] <= 8016: # Nov
                    self.Overall_Array[i,77] = self.Overall_Array[i,5]*self.monthly_internal_heat_gain[10,0]
                    self.Overall_Array[i,78] = self.Overall_Array[i,6]*self.monthly_internal_heat_gain[10,1]
                    self.totalLighting       = self.monthly_internal_heat_gain[10,2]
                elif 8017 <= self.Overall_Array[i,0]: # Dec
                    self.Overall_Array[i,77] = self.Overall_Array[i,5]*self.monthly_internal_heat_gain[11,0]
                    self.Overall_Array[i,78] = self.Overall_Array[i,6]*self.monthly_internal_heat_gain[11,1]
                    self.totalLighting       = self.monthly_internal_heat_gain[11,2]

            self.Overall_Array[i,81] = (self.heatgainGlazing1[i,10]+self.heatgainGlazing2[i,10]+self.heatgainOpaque1[i,9]+self.heatgainOpaque2[i,9])/self.totalArea

            if self.weatherData[i,10] != 0:
                if self.Overall_Array[i,4] == 0:
                    self.Overall_Array[i,82] = self.Overall_Array[i,7]*(self.totalLighting*self.left_numeric[4,0])*(self.left_numeric[2,0]*self.left_numeric[3,0])*(1-self.dimmer_we)
                else:
                    self.Overall_Array[i,82] = self.Overall_Array[i,7]*(self.totalLighting*self.left_numeric[4,0])*(self.left_numeric[2,0]*self.left_numeric[3,0])*(1-self.dimmer_wd)
            else:
                if self.Overall_Array[i,4] == 0:
                    self.Overall_Array[i,82] = self.Overall_Array[i,7]*(self.totalLighting*self.left_numeric[4,0])*self.left_numeric[3,0]*(1-self.dimmer_we)
                else:
                    self.Overall_Array[i,82] = self.Overall_Array[i,7]*(self.totalLighting*self.left_numeric[4,0])*self.left_numeric[3,0]*(1-self.dimmer_wd)

            self.Overall_Array[i,83] = 0.684936
            self.Overall_Array[i,84] = self.Overall_Array[i,82] + 0.684936

            self.Overall_Array[i,79] = self.Overall_Array[i,84]
            self.Overall_Array[i,80] = self.Overall_Array[i,77]+self.Overall_Array[i,78]+self.Overall_Array[i,79]

            self.Overall_Array[i,8]  = self.Overall_Array[i,80]
            self.Overall_Array[i,9]  = self.Overall_Array[i,81]
            self.Overall_Array[i,10] = self.Overall_Array[i,8]+self.Overall_Array[i,9]
            self.Overall_Array[i,11] = (1.2/3.6) * self.Overall_Array[i,65]
            self.Overall_Array[i,12] = 1/(1/(self.Overall_Array[i,11])+1/(4.5*3.45))
            self.Overall_Array[i,13] = self.Overall_Array[i,12] + self.Htr_w_Af
            self.Overall_Array[i,14] = 1/(1/self.Overall_Array[i,13]+1/self.Htr_ms)
            self.Overall_Array[i,15] = 0.5*self.Overall_Array[i,8]
            self.Overall_Array[i,16] = self.Prm*(0.5*self.Overall_Array[i,8]+self.Overall_Array[i,9])
            self.Overall_Array[i,17] = self.Prs*(0.5*self.Overall_Array[i,8]+self.Overall_Array[i,9])
            self.Overall_Array[i,18] = self.Overall_Array[i,16]+self.Htr_em*self.weatherData[i,0]+self.Overall_Array[i,14]*(self.Overall_Array[i,17]+self.Htr_w_Af*self.weatherData[i,0]+self.Overall_Array[i,12]*(self.Overall_Array[i,15]/self.Overall_Array[i,11]+self.Overall_Array[i,38]))/self.Overall_Array[i,13]

            self.Overall_Array[i,20] = (self.Overall_Array[i,19]*((self.EvenlopeHeatCapacity/3600)-0.5*(self.Overall_Array[i,14]+self.Htr_em))+self.Overall_Array[i,18])/((self.EvenlopeHeatCapacity/3600)+0.5*(self.Overall_Array[i,14]+self.Htr_em))
            self.Overall_Array[i,21] = (self.Overall_Array[i,19] + self.Overall_Array[i,20])/2
            self.Overall_Array[i,22] = (self.Htr_ms*self.Overall_Array[i,21]+self.Overall_Array[i,17]+self.Htr_w_Af*self.weatherData[i,0]+self.Overall_Array[i,12]*(self.Overall_Array[i,38]+self.Overall_Array[i,15]/self.Overall_Array[i,11]))/(self.Htr_ms+self.Htr_w_Af+self.Overall_Array[i,12])
            self.Overall_Array[i,23] = (self.Htr_is*self.Overall_Array[i,22]+self.Overall_Array[i,11]*self.Overall_Array[i,38]+self.Overall_Array[i,15])/(self.Htr_is+self.Overall_Array[i,11])

            if i > 0:
                if self.Overall_Array[i,23] < self.Overall_Array[i,36]:
                    self.Overall_Array[i,39] = self.Overall_Array[i,36]
                elif self.Overall_Array[i,23] > self.Overall_Array[i,37]:
                    self.Overall_Array[i,39] = self.Overall_Array[i,37]
                else:
                    self.Overall_Array[i,39] = self.Overall_Array[i,23]

            self.Overall_Array[i,24] = 0.3*self.Overall_Array[i,23]+0.7*self.Overall_Array[i,22]
            self.Overall_Array[i,25] = self.Overall_Array[i,15]

            self.Overall_Array[i,27] = self.Overall_Array[i,16]
            self.Overall_Array[i,28] = self.Overall_Array[i,17]
            self.Overall_Array[i,29] = self.Overall_Array[i,27]+self.Htr_em*self.weatherData[i,0]+self.Overall_Array[i,14]*(self.Overall_Array[i,28]+self.Htr_w_Af*self.weatherData[i,0]+self.Overall_Array[i,12]*((self.Overall_Array[i,25]+self.Overall_Array[i,26])/self.Overall_Array[i,11]+self.Overall_Array[i,38]))/self.Overall_Array[i,13]

            self.Overall_Array[i,31] = (self.Overall_Array[i,30]*((self.EvenlopeHeatCapacity/3600)-0.5*(self.Overall_Array[i,14]+self.Htr_em))+self.Overall_Array[i,29])/((self.EvenlopeHeatCapacity/3600)+0.5*(self.Overall_Array[i,14]+self.Htr_em))
            self.Overall_Array[i,32] = (self.Overall_Array[i,30]+self.Overall_Array[i,31])/2
            self.Overall_Array[i,33] = (self.Htr_ms*self.Overall_Array[i,32]+self.Overall_Array[i,28]+self.Htr_w_Af*self.weatherData[i,0]+self.Overall_Array[i,12]*(self.Overall_Array[i,38]+(self.Overall_Array[i,25]+self.Overall_Array[i,26])/self.Overall_Array[i,11]))/(self.Htr_ms+self.Htr_w_Af+self.Overall_Array[i,12])
            self.Overall_Array[i,34] = (self.Htr_is*self.Overall_Array[i,33]+self.Overall_Array[i,11]*self.Overall_Array[i,38]+self.Overall_Array[i,25]+self.Overall_Array[i,26])/(self.Htr_is+self.Overall_Array[i,11])
            self.Overall_Array[i,35] = 0.3*self.Overall_Array[i,34]+0.7*self.Overall_Array[i,33]

            if (self.Overall_Array[i,23] >= self.Overall_Array[i,36]) and (self.Overall_Array[i,23] <= self.Overall_Array[i,37]):
                self.Overall_Array[i,40] = 0
            else:
                self.Overall_Array[i,40] = 10*(self.Overall_Array[i,39]-self.Overall_Array[i,23])/(self.Overall_Array[i,34]-self.Overall_Array[i,23])

            self.Overall_Array[i,41] = max(0,10*(self.Overall_Array[i,36]-self.Overall_Array[i,23])/(self.Overall_Array[i,34]-self.Overall_Array[i,23]))
            self.Overall_Array[i,42] = min(0,10*(self.Overall_Array[i,37]-self.Overall_Array[i,23])/(self.Overall_Array[i,34]-self.Overall_Array[i,23]))

            self.Overall_Array[i,44] = self.Overall_Array[i,15]
            self.Overall_Array[i,45] = self.Overall_Array[i,40]
            self.Overall_Array[i,46] = self.Overall_Array[i,16]
            self.Overall_Array[i,47] = self.Overall_Array[i,17]
            self.Overall_Array[i,48] = self.Overall_Array[i,46]+self.Htr_em*self.weatherData[i,0]+self.Overall_Array[i,14]*(self.Overall_Array[i,47]+self.Htr_w_Af*self.weatherData[i,0]+self.Overall_Array[i,12]*((self.Overall_Array[i,44]+self.Overall_Array[i,45])/self.Overall_Array[i,11]+self.Overall_Array[i,38]))/self.Overall_Array[i,13]

            self.Overall_Array[i,50] = (self.Overall_Array[i,49]*((self.EvenlopeHeatCapacity/3600)-0.5*(self.Overall_Array[i,14]+self.Htr_em))+self.Overall_Array[i,48])/((self.EvenlopeHeatCapacity/3600)+0.5*(self.Overall_Array[i,14]+self.Htr_em))

            self.Overall_Array[i,51] = (self.Overall_Array[i,49]+self.Overall_Array[i,50])/2
            self.Overall_Array[i,52] = (self.Htr_ms*self.Overall_Array[i,51]+self.Overall_Array[i,47]+self.Htr_w_Af*self.weatherData[i,0]+self.Overall_Array[i,12]*(self.Overall_Array[i,38]+(self.Overall_Array[i,44]+self.Overall_Array[i,45])/self.Overall_Array[i,11]))/(self.Htr_ms+self.Htr_w_Af+self.Overall_Array[i,12])
            self.Overall_Array[i,53] = (self.Htr_is*self.Overall_Array[i,52]+self.Overall_Array[i,11]*self.Overall_Array[i,38]+self.Overall_Array[i,44]+self.Overall_Array[i,45])/(self.Htr_is+self.Overall_Array[i,11])

            if i == 0:
                if self.Overall_Array[i,42] < 0 and self.weatherData[i,0] < self.hs_unoccupied and self.weatherData[i,14] < 75:
                    self.Overall_Array[i,95] = 1
                else:
                    self.Overall_Array[i,95] = 0
            else:
                if self.Overall_Array[i,42] < 0 and self.weatherData[i,0] < self.Overall_Array[i-1,53] and self.weatherData[i,14] < 75:
                    self.Overall_Array[i,95] = 1
                else:
                    self.Overall_Array[i,95] = 0

            if self.Overall_Array[i,95] == 0:
                self.Overall_Array[i,43] = self.Overall_Array[i,42]
            else:
                self.Overall_Array[i,43] = 0

            self.Overall_Array[i,54] = 0.3*self.Overall_Array[i,53] + 0.7*self.Overall_Array[i,52]

            self.Overall_Array[i,70] = (self.Overall_Array[i,41]/1000*3.6)/(self.T_supply_h -self.Overall_Array[i,53])/(1.22521*0.001012)

            if self.right_string[4] == '1. Mechanical system only; no provision for natural ventilation':
                self.Overall_Array[i,71] = -(self.Overall_Array[i,42])/1000*3.6/(self.Overall_Array[i,53]-self.T_supply_c)/(1.22521*0.001012)
            else:
                self.Overall_Array[i,71] = -(self.Overall_Array[i,43])/1000*3.6/(self.Overall_Array[i,53]-self.T_supply_c)/(1.22521*0.001012)

            self.Overall_Array[i,75] = max(self.Overall_Array[i,59],self.Overall_Array[i,70],self.Overall_Array[i,71])+self.Overall_Array[i,74]
            self.Overall_Array[i,76] = self.Overall_Array[i,75]*self.left_numeric[9,0]*self.left_numeric[10,0]*self.f_BAC_e/3600*1000

            self.Overall_Array[i,89] = self.Overall_Array[i,41]

            if self.right_string[4] == '1. Mechanical system only; no provision for natural ventilation':
                self.Overall_Array[i,90] = self.Overall_Array[i,42]
            else:
                self.Overall_Array[i,90] = self.Overall_Array[i,43]

        for i in range(12):
            self.Q_heat_nd[i,0] = float(np.sum(self.Overall_Array[self._range[i]:self._range[i+1],41]))/1000 
            self.Q_cool_nd[i,0] = -float(np.sum(self.Overall_Array[self._range[i]:self._range[i+1],42]))/1000           

        self.Q_heat_nd[12,0] = float(np.sum(self.Q_heat_nd)) 
        self.Q_cool_nd[12,0] = float(np.sum(self.Q_cool_nd)) 
        self.f_dem_heat = max(self.Q_heat_nd[12,0]/(self.Q_cool_nd[12,0]+self.Q_heat_nd[12,0]),0.1)
        self.f_dem_cold = max((1-self.f_dem_heat),0.1)
        self.dist_cool = 1/(1+self.a_cool+self.f_waste/self.f_dem_cold)
        self.dist_heat = 1/(1+self.a_heat+self.f_waste/self.f_dem_heat)
        self.occu_equi_hours = float(np.sum(self.Overall_Array[:,5]))

                
        for i in range(8760): # can't eliminate this for-loop b/c of the "f_dem_heat" and "f_dem_cold" variables
            # PV
            if self.left_numeric[12,0] != 0: # if PV area is not equal to 0
                if self.left_numeric[13,0] == 0: # Tilt
                    self.Overall_Array[i,85] = self.weatherData[i,10]

                elif self.left_numeric[13,0] == 30:
                    if self.right_string[11] == 'S':
                        self.Overall_Array[i,85] = self.Essol_30[i,0]
                    if self.right_string[11] == 'SE':
                        self.Overall_Array[i,85] = self.Essol_30[i,1]
                    if self.right_string[11] == 'E':
                        self.Overall_Array[i,85] = self.Essol_30[i,2]
                    if self.right_string[11] == 'W':
                        self.Overall_Array[i,85] = self.Essol_30[i,6]
                    if self.right_string[11] == 'SW':
                        self.Overall_Array[i,85] = self.Essol_30[i,7]
                        
                elif self.left_numeric[13,0] == 45:
                    if self.right_string[11] == 'S':
                        self.Overall_Array[i,85] = self.Essol_45[i,0]    
                    if self.right_string[11] == 'SE':
                        self.Overall_Array[i,85] = self.Essol_45[i,1]
                    if self.right_string[11] == 'E':
                        self.Overall_Array[i,85] = self.Essol_45[i,2]
                    if self.right_string[11] == 'W':
                        self.Overall_Array[i,85] = self.Essol_45[i,6]
                    if self.right_string[11] == 'SW':
                        self.Overall_Array[i,85] = self.Essol_45[i,7]
                        
                elif self.left_numeric[13,0] == 60:
                    if self.right_string[11] == 'S':
                        self.Overall_Array[i,85] = self.Essol_60[i,0]    
                    if self.right_string[11] == 'SE':
                        self.Overall_Array[i,85] = self.Essol_60[i,1]
                    if self.right_string[11] == 'E':
                        self.Overall_Array[i,85] = self.Essol_60[i,2]
                    if self.right_string[11] == 'W':
                        self.Overall_Array[i,85] = self.Essol_60[i,6]
                    if self.right_string[11] == 'SW':
                        self.Overall_Array[i,85] = self.Essol_60[i,7]
                        
                elif self.left_numeric[13,0] == 90:
                    if self.right_string[11] == 'S':
                        self.Overall_Array[i,85] = self.Essol_90[i,0]    
                    if self.right_string[11] == 'SE':
                        self.Overall_Array[i,85] = self.Essol_90[i,1]
                    if self.right_string[11] == 'E':
                        self.Overall_Array[i,85] = self.Essol_90[i,2]
                    if self.right_string[11] == 'W':
                        self.Overall_Array[i,85] = self.Essol_90[i,6]
                    if self.right_string[11] == 'SW':
                        self.Overall_Array[i,85] = self.Essol_90[i,7]
            
            self.Overall_Array[i,86] = self.Overall_Array[i,85]*self.left_numeric[12,0]*self.left_numeric[14,0]*self.left_numeric[15,0]

            # Solar water heating
            if self.left_numeric[16,0] != 0: # if area is not equal to 0
                if self.left_numeric[17,0] == 0: # Tilt
                    self.Overall_Array[i,87] = self.weatherData[i,10]
                    
                elif self.left_numeric[17,0] == 30:
                    if self.right_string[12] == 'S':
                        self.Overall_Array[i,87] = self.Essol_30[i,0]
                    if self.right_string[12] == 'SE':
                        self.Overall_Array[i,87] = self.Essol_30[i,1]
                    if self.right_string[12] == 'E':
                        self.Overall_Array[i,87] = self.Essol_30[i,2]
                    if self.right_string[12] == 'W':
                        self.Overall_Array[i,87] = self.Essol_30[i,6]
                    if self.right_string[12] == 'SW':
                        self.Overall_Array[i,87] = self.Essol_30[i,7]
                        
                elif self.left_numeric[17,0] == 45:
                    if self.right_string[12] == 'S':
                        self.Overall_Array[i,87] = self.Essol_45[i,0]    
                    if self.right_string[12] == 'SE':
                        self.Overall_Array[i,87] = self.Essol_45[i,1]
                    if self.right_string[12] == 'E':
                        self.Overall_Array[i,87] = self.Essol_45[i,2]
                    if self.right_string[12] == 'W':
                        self.Overall_Array[i,87] = self.Essol_45[i,6]
                    if self.right_string[12] == 'SW':
                        self.Overall_Array[i,87] = self.Essol_45[i,7]
                        
                elif self.left_numeric[17,0] == 60:
                    if self.right_string[12] == 'S':
                        self.Overall_Array[i,87] = self.Essol_60[i,0]    
                    if self.right_string[12] == 'SE':
                        self.Overall_Array[i,87] = self.Essol_60[i,1]
                    if self.right_string[12] == 'E':
                        self.Overall_Array[i,87] = self.Essol_60[i,2]
                    if self.right_string[12] == 'W':
                        self.Overall_Array[i,87] = self.Essol_60[i,6]
                    if self.right_string[12] == 'SW':
                        self.Overall_Array[i,87] = self.Essol_60[i,7]
                        
                elif self.left_numeric[17,0] == 90:
                    if self.right_string[12] == 'S':
                        self.Overall_Array[i,87] = self.Essol_90[i,0]    
                    if self.right_string[12] == 'SE':
                        self.Overall_Array[i,87] = self.Essol_90[i,1]
                    if self.right_string[12] == 'E':
                        self.Overall_Array[i,87] = self.Essol_90[i,2]
                    if self.right_string[12] == 'W':
                        self.Overall_Array[i,87] = self.Essol_90[i,6]
                    if self.right_string[12] == 'SW':
                        self.Overall_Array[i,87] = self.Essol_90[i,7]

            self.Overall_Array[i,88] = max((self.total_DHW_system*self.Overall_Array[i,5]/self.occu_equi_hours-self.Overall_Array[i,87]*self.left_numeric[16,0]*0.5)/self.effi_gen_DHW,0)
            
            self.Overall_Array[i,91] = self.Overall_Array[i,89]*(1-self.dist_heat)/self.dist_heat
            self.Overall_Array[i,92] = (self.Overall_Array[i,89]+self.Overall_Array[i,91])*self.f_BAC_hc/float(self.left_numeric[5,0])
            self.Overall_Array[i,93] = self.Overall_Array[i,90]*(1-self.dist_cool)/self.dist_cool
            self.Overall_Array[i,94] = (self.Overall_Array[i,90]+self.Overall_Array[i,93])*self.f_BAC_hc/(float(self.left_numeric[6,0])*0.817)
            
            self.deliveredEnergy[i,0] = self.Overall_Array[i,92]  # Eheat
            self.deliveredEnergy[i,1] = -self.Overall_Array[i,94] # Ecool
            self.deliveredEnergy[i,2] = self.Overall_Array[i,84] + self.garage_lighting*self.garage_schedule_all[i,1] # Elight ####
            self.deliveredEnergy[i,3] = self.Overall_Array[i,76]  # Efan
            self.deliveredEnergy[i,4] = self.pump_Equip[12,1]*1000/self.totalArea*self.Overall_Array[i,5]/self.occu_equi_hours # Epump
            self.deliveredEnergy[i,5] = self.Overall_Array[i,78] + self.retail_refrig_cap_per_area + self.garage_appliance*self.garage_schedule_all[i,0] # Eequip ####
            self.deliveredEnergy[i,6] = self.Overall_Array[i,88]*1000/self.totalArea # Edhw
    
            if self.Overall_Array[i,4] == 1: # E_EV
                self.deliveredEnergy[i,7] = self.EV_tempo*self.EV_schedule[i%24,0]/self.totalArea
            else:
                self.deliveredEnergy[i,7] = self.EV_tempo*self.EV_schedule[i%24,1]/self.totalArea
                
            self.deliveredEnergy[i,8] = self.Overall_Array[i,86]*1000/self.totalArea # Egen_pv
            self.deliveredEnergy[i,9] = (self.weatherData[i,13]/287/(self.weatherData[i,0]+273)*0.5*(0.25*3.14159265359*self.left_numeric[18,0]**2)*self.left_numeric[19,0]*self.weatherData[i,1]**3)/self.totalArea  # Egen_wind
            self.deliveredEnergy[i,10] = float(np.sum(self.deliveredEnergy[i,0:8]))-float(np.sum(self.deliveredEnergy[i,8:10])) # Etotal

            # Delivered Energy by fuel (kWh) # Initially it was assumed all the energy sources are electricity
            self.deliveredEnergy_fuel[i,0] = self.deliveredEnergy[i,10]*self.totalArea/1000 # (heat+cool+lighting+fan+pump+equip+DHW)-(PV+wind)

            # If HEATING energy source is not from electricity
            if self.right_string[13] == "Natural Gas": 
                self.deliveredEnergy_fuel[i,0] = self.deliveredEnergy_fuel[i,0] - (self.deliveredEnergy[i,0]*self.totalArea/1000)
                self.deliveredEnergy_fuel[i,1] = self.deliveredEnergy[i,0]*self.totalArea/1000 
            elif self.right_string[13] == "Fuel": 
                self.deliveredEnergy_fuel[i,0] = self.deliveredEnergy_fuel[i,0] - (self.deliveredEnergy[i,0]*self.totalArea/1000)
                self.deliveredEnergy_fuel[i,2] = self.deliveredEnergy[i,0]*self.totalArea/1000 

            # If DOMESTIC HOT WATER energy source is not from electricity
            if self.right_string[14] == "Natural Gas": 
                self.deliveredEnergy_fuel[i,0] = self.deliveredEnergy_fuel[i,0] - (self.deliveredEnergy[i,6]*self.totalArea/1000) 
                self.deliveredEnergy_fuel[i,1] = self.deliveredEnergy[i,6]*self.totalArea/1000 
            elif self.right_string[14] == "Fuel":
                self.deliveredEnergy_fuel[i,0] = self.deliveredEnergy_fuel[i,0] - (self.deliveredEnergy[i,6]*self.totalArea/1000)
                self.deliveredEnergy_fuel[i,2] = self.deliveredEnergy[i,6]*self.totalArea/1000 

            # If COOLING energy source is not from electricity
            if self.right_string[14] == "Natural Gas":  
                self.deliveredEnergy_fuel[i,0] = self.deliveredEnergy_fuel[i,0] - (self.deliveredEnergy[i,1]*self.totalArea/1000)
                self.deliveredEnergy_fuel[i,1] = self.deliveredEnergy[i,1]*self.totalArea/1000 
            elif self.right_string[14] == "Fuel":
                self.deliveredEnergy_fuel[i,0] = self.deliveredEnergy_fuel[i,0] - (self.deliveredEnergy[i,1]*self.totalArea/1000)
                self.deliveredEnergy_fuel[i,2] = self.deliveredEnergy[i,1]*self.totalArea/1000 

               
            # electric battery
            if self.eb_capacity>0:
                self.electric_battery[i,0] = self.deliveredEnergy_fuel[i,0]
                if self.electric_battery[i,0] < 0:
                    self.electric_battery[i,1] = 0
                    self.electric_battery[i,2] = -self.electric_battery[i,0]
                else:
                    self.electric_battery[i,1] = self.electric_battery[i,0]
                    self.electric_battery[i,2] = 0


        if self.eb_capacity>0:
            for i in range(1,8759):
                if self.electric_battery[i,2] <= self.P_charg_limit:    
                    self.electric_battery[i,3] = self.electric_battery[i,2]
                else:
                    self.electric_battery[i,3] = self.P_charg_limit

                tempo = self.electric_battery[i-1,4]+self.electric_battery[i,3]*self.eta_charge-self.electric_battery[i-1,6]/self.eta_discharge
                if 0 < tempo <= self.eb_capacity:
                    self.electric_battery[i,4] = tempo
                else:
                    self.electric_battery[i,4] = 0

                if self.electric_battery[i+1,1]>0 and self.electric_battery[i,4]>0:
                    if self.electric_battery[i,4] > self.electric_battery[i+1,1]:
                        self.electric_battery[i,5] = self.electric_battery[i+1,1]
                    else:
                        self.electric_battery[i,5] = self.electric_battery[i,4]
                else:
                    self.electric_battery[i,5] = 0

                if self.electric_battery[i,5] < self.P_discharge_limit:
                    self.electric_battery[i,6] = self.electric_battery[i,5]
                else:
                    self.electric_battery[i,6] = self.P_discharge_limit

                if self.electric_battery[i,1] - self.electric_battery[i-1,5]<0:
                    self.deliveredEnergy_fuel[i,0] = 0
                else:
                    self.deliveredEnergy_fuel[i,0] = self.electric_battery[i,1] - self.electric_battery[i-1,5]              
                self.deliveredEnergy_fuel[i,3] = np.sum(self.deliveredEnergy_fuel[i,0:3])
                
        self.Overall_deliveredEnergy = float(np.sum(self.deliveredEnergy[:,10]))/1000 # unit kWh/m2

        self.outcome = self.deliveredEnergy
        self.outcome2 = self.Overall_deliveredEnergy
        self.outcome3 = self.deliveredEnergy_fuel

        self.out = np.asarray(self.outcome[:, -1]) * self.totalArea / 1000

        subDeliveredEnergy = np.zeros((12,11))
        for i in range(11):
            subDeliveredEnergy[0, i] = np.sum(self.outcome[0:744, i])
            subDeliveredEnergy[1, i] = np.sum(self.outcome[744:1416, i])
            subDeliveredEnergy[2, i] = np.sum(self.outcome[0:744, i])
            subDeliveredEnergy[3, i] = np.sum(self.outcome[1416:2159, i])
            subDeliveredEnergy[4, i] = np.sum(self.outcome[2159:2880, i])
            subDeliveredEnergy[5, i] = np.sum(self.outcome[2880:3624, i])
            subDeliveredEnergy[6, i] = np.sum(self.outcome[3624:4344, i])
            subDeliveredEnergy[7, i] = np.sum(self.outcome[4344:5088, i])
            subDeliveredEnergy[8, i] = np.sum(self.outcome[5088:5832, i])
            subDeliveredEnergy[9, i] = np.sum(self.outcome[5832:6552, i])
            subDeliveredEnergy[10, i] = np.sum(self.outcome[6552:7296, i])
            subDeliveredEnergy[11, i] = np.sum(self.outcome[8016:8760, i])

        subMonthlyTotal = np.zeros((12,1))
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



        manipulated_result = np.zeros((12, 1))
        manipulated_result[0, 0] = np.sum(self.outcome3[0:744, 0])
        manipulated_result[1, 0] = np.sum(self.outcome3[744:1416, 0])
        manipulated_result[2, 0] = np.sum(self.outcome3[1416:2159, 0])
        manipulated_result[3, 0] = np.sum(self.outcome3[2159:2880, 0])
        manipulated_result[4, 0] = np.sum(self.outcome3[2880:3624, 0])
        manipulated_result[5, 0] = np.sum(self.outcome3[3624:4344, 0])
        manipulated_result[6, 0] = np.sum(self.outcome3[4344:5088, 0])
        manipulated_result[7, 0] = np.sum(self.outcome3[5088:5832, 0])
        manipulated_result[8, 0] = np.sum(self.outcome3[5832:6552, 0])
        manipulated_result[9, 0] = np.sum(self.outcome3[6552:7296, 0])
        manipulated_result[10, 0] = np.sum(self.outcome3[7296:8016, 0])
        manipulated_result[11, 0] = np.sum(self.outcome3[8016:8760, 0])

        # deviation = 0
        # for j in range(self.num_of_loop):
        #     deviation += (self.measuredData[j, 0] - manipulated_result[j, 0]) ** 2
        # cvRMSE = (1 / self.y_bar) * sqrt(deviation / (self.num_of_loop * self.number_of_data - 1)) * 100
        if self.outputPeriod == "Monthly":
            plot_data = pd.DataFrame(self.out, columns=['Delivered'])
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

            self.grouped = (plot_data.groupby(['Month'], sort=False).sum()).reset_index()
        elif self.outputPeriod == "Hourly":
            self.grouped = pd.DataFrame(self.out, columns=['Delivered'])



        #self.grouped = (plot_data.groupby(['Month'], sort=False).sum()).reset_index()


        # plt.figure(figsize=(14, 8))
        # plt.plot(grouped.Month.values, grouped.Delivered.values, label="Model", marker='o')
        # plt.plot(grouped.Month.values, self.measuredData[:, 0], label="Utility", marker='o')
        # plt.ylim(0, (self.y_max + 100000))
        # plt.legend()
        # plt.xlabel('Month')
        # plt.ylabel('Energy Consumption (kWh)')
        # plt.title(f"Model Results vs. Utility Data for CV RMSE of {round(best_so_far_fitness_value[-1], 3)}%")
        # plt.ticklabel_format(style='plain', axis='y')
        # plt.savefig(f"calibration_result_{self.result_file_name}.png")
        # plt.show()
       
        return self.deliveredEnergy, self.Overall_deliveredEnergy, self.deliveredEnergy_fuel, self.grouped


def Hourly_BEM_JSON(jsonData, weatherData, SRF_overhang, SRF_fin, SRF_horizon, Esol_30, Esol_45, Esol_60, Esol_90):
    instance = BEM(jsonData, weatherData, SRF_overhang, SRF_fin, SRF_horizon, Esol_30, Esol_45, Esol_60, Esol_90)
    instance.readJSON()
    instance.GeneralDataProcessing()
    instance.TransmissionHeatTransfer()
    instance.VentilationAirFlowandVentilationHeatTransfer()
    instance.BEMSystem()
    instance.CoolingandHeatingSystemEnergy()
    instance.FanEnergy()
    instance.PumpSystemEnergy()
    instance.DHWandSolarWaterHeating()
    outcome, outcome2, outcome3, grouped = instance.hourly_BEM()

    return outcome, outcome2, outcome3, grouped

if __name__ == '__main__':
    print("Please execute the 'main.py' script.")

