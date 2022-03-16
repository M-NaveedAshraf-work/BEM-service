import numpy as np
from math import pi, sin, cos, tan, asin, acos, radians, degrees

##np.set_printoptions(linewidth=2000); np.set_printoptions(formatter={'float': '{: 0.2f}'.format});

class ClimateCalculator(object):

    def __init__(self, epw_file_name):
        self.epw_file_name = epw_file_name
        
    def ClimateCalculation(self):

        Area=1; Esc=1367; r_g=0.14; sigma_list=[30,45,60,90]

        data_from_epw=np.zeros((8760,7)); calculation=np.zeros((8760,71)); calculation_specific_humidity=np.zeros((8760,11)); SRF=np.zeros((8760,96)); hourly_output=np.zeros((8760,16))

        SRF_overhang=np.zeros((8760,24)); SRF_fin=np.zeros((8760,24)); SRF_horizon=np.zeros((8760,48))

        Esol_30=np.zeros((8760,8)); Esol_45=np.zeros((8760,8)); Esol_60=np.zeros((8760,8)); Esol_90=np.zeros((8760,8))

        count_hour=1; count_day=1

        # Open .epw file
        with open("".join(["./Weather/",self.epw_file_name]), 'r') as f:
            data =[]
            for line in f:
                line = line.strip()
                data.append(line.strip().split(','))
        f.close()

        Lat = float(data[0][6]); Lon = float(data[0][7]); time_zone = float(data[0][8]); LSM = time_zone*15;

        # Coefficients
        water_a0 = 6.107799961; water_a1 = 4.436518521*10**(-1); water_a2 = 1.428945805*10**(-2); water_a3 = 2.650648471*10**(-4); water_a4 = 3.031240396*10**(-6); water_a5 = 2.034080948*10**(-8); water_a6 = 6.136820929*10**(-11)
        ice_a0 = 6.109177956; ice_a1 = 5.03469897*10**(-1); ice_a2 = 1.886013408*10**(-2); ice_a3 = 4.176223716*10**(-4); ice_a4 = 5.82472028*10**(-6); ice_a5 = 4.838803174*10**(-8); ice_a6 = 1.838826904*10**(-10)

        # EPW_data sheet
        for i in range(8760):
            data_from_epw[i,0]  = float(data[i+8][6])  # DryBulb {C}
            data_from_epw[i,1]  = float(data[i+8][13]) # GloHorzRad {Wh/m2}
            data_from_epw[i,2]  = float(data[i+8][14]) # DirNormRad {Wh/m2}
            data_from_epw[i,3]  = float(data[i+8][15]) # DifHorzRad {Wh/m2}
            data_from_epw[i,4]  = float(data[i+8][21]) # WindSpd {m/s}
            data_from_epw[i,5]  = float(data[i+8][8])  # RHum {%}
            data_from_epw[i,6]  = float(data[i+8][9])  # Atmospheric station pressure {Pa}
            hourly_output[i,15] = float(data[i+8][20]) # Wind direction
            
        # Start "Calculation" sheet
        for i in range(8760):
            if (i <= 743): # Month
                calculation[i,0] = 1   
            elif (i > 743  and i <= 1415): calculation[i,0] = 2
            elif (i > 1415  and i <= 2159): calculation[i,0] = 3
            elif (i > 2159  and i <= 2879): calculation[i,0] = 4          
            elif (i > 2879  and i <= 3623): calculation[i,0] = 5
            elif (i > 3623  and i <= 4343): calculation[i,0] = 6
            elif (i > 4343  and i <= 5087): calculation[i,0] = 7
            elif (i > 5087  and i <= 5831): calculation[i,0] = 8
            elif (i > 5831  and i <= 6551): calculation[i,0] = 9
            elif (i > 6551  and i <= 7295): calculation[i,0] = 10
            elif (i > 7295  and i <= 8015): calculation[i,0] = 11
            elif (i > 8015  and i <= 8759): calculation[i,0] = 12

            if ((i+1)%24 == 0): # Hour
                calculation[i,2] = 24; count_hour = 1
            else: calculation[i,2] = count_hour; count_hour += 1

            # Day
            if (i <= 743): # Jan
                if (calculation[i,2] == 24): calculation[i,1] = count_day; count_day += 1
                else: calculation[i,1] = count_day
                    
            elif (i > 743  and i <= 1415): # Feb
                if (i == 744): count_day = 1
                if (calculation[i,2] == 24): calculation[i,1] = count_day; count_day += 1
                else: calculation[i,1] = count_day
                        
            elif (i > 1415  and i <= 2159): # Mar
                if (i == 1416): count_day = 1
                if (calculation[i,2] == 24): calculation[i,1] = count_day; count_day += 1
                else:
                    calculation[i,1] = count_day
                    
            elif (i > 2159  and i <= 2879): # Apr
                if (i == 2160): count_day = 1
                if (calculation[i,2] == 24): calculation[i,1] = count_day; count_day += 1
                else: calculation[i,1] = count_day
                    
            elif (i > 2879  and i <= 3623): # May
                if (i == 2880): count_day = 1
                if (calculation[i,2] == 24): calculation[i,1] = count_day; count_day += 1
                else: calculation[i,1] = count_day
                    
            elif (i > 3623  and i <= 4343): # Jun
                if (i == 3624):
                    count_day = 1
                if (calculation[i,2] == 24): calculation[i,1] = count_day; count_day += 1
                else: calculation[i,1] = count_day
                    
            elif (i > 4343  and i <= 5087): # Jul
                if (i == 4344):
                    count_day = 1
                if (calculation[i,2] == 24): calculation[i,1] = count_day;  count_day += 1
                else: calculation[i,1] = count_day
                    
            elif (i > 5087  and i <= 5831): # Aug
                if (i == 5088): count_day = 1
                if (calculation[i,2] == 24): calculation[i,1] = count_day; count_day += 1
                else: calculation[i,1] = count_day
                    
            elif (i > 5831  and i <= 6551): # Sep
                if (i == 5832): count_day = 1
                if (calculation[i,2] == 24): calculation[i,1] = count_day; count_day += 1
                else:
                    calculation[i,1] = count_day
                    
            elif (i > 6551  and i <= 7295): # Oct
                if (i == 6552): count_day = 1
                if (calculation[i,2] == 24): calculation[i,1] = count_day; count_day += 1
                else: calculation[i,1] = count_day
                    
            elif (i > 7295  and i <= 8015): # Nov
                if (i == 7296): count_day = 1
                if (calculation[i,2] == 24): calculation[i,1] = count_day; count_day += 1
                else: calculation[i,1] = count_day
                    
            elif (i > 8015  and i <= 8759): # Dec
                if (i == 8016): count_day = 1
                if (calculation[i,2] == 24): calculation[i,1] = count_day; count_day += 1
                else: calculation[i,1] = count_day   
            
            if (i==0): calculation[i,3] = 1 # Year day number
            elif (calculation[i,0]==calculation[i-1][0]): calculation[i,3] = calculation[i-1][3]+(calculation[i,1]-calculation[i-1][1])
            else: calculation[i,3] = calculation[i-1][3]+1

        for sigma in sigma_list:
            for i in range(8760):
                calculation[i,4] = data_from_epw[i,0] # Dry Bulb Temperature
                calculation[i,5] = data_from_epw[i,1] # Global Horizontal Radiation {Wh/m2}
                calculation[i,6] = data_from_epw[i,2] # Direct Normal Radiation {Wh/m2}
                calculation[i,7] = data_from_epw[i,3] # Diffuse Horizontal Radiation {Wh/m2}
                calculation[i,8] = 2*pi*(calculation[i,3]-1)/365 # in minutes
                calculation[i,9] = 2.2918*(0.0075+0.1868*cos(calculation[i,8])-3.2077*sin(calculation[i,8])-1.4615*cos(2*calculation[i,8])-4.089*sin(2*calculation[i,8]))#
                calculation[i,10] = calculation[i,2] # clock time  
                calculation[i,11] = calculation[i,10]+calculation[i,9]/60+(Lon-LSM)/15 # apparent solar time  
                calculation[i,12] = 23.45*sin((calculation[i,3]+284)/365*2*pi) # solar declination, deg
                calculation[i,13] = 15*(calculation[i,11]-12) # hour angle: angular displacement of the sun east or west of the local meridian due to the rotation of the earth,deg
                calculation[i,14] = cos(Lat*pi/180)*cos(calculation[i,12]*pi/180)*cos(calculation[i,13]*pi/180)+sin(Lat*pi/180)*sin(calculation[i,12]*pi/180) # sin_beta_s
                calculation[i,15] = asin(calculation[i,14]) # solar altitude, radians
                calculation[i,16] = degrees(calculation[i,15]) # solar altitude, degrees
                calculation[i,17] = sin(calculation[i,13]*pi/180)*cos(calculation[i,12]*pi/180)/cos(calculation[i,15]) # sin(azimuth angle)   
                calculation[i,18] =(cos(calculation[i,13]*pi/180)*cos(calculation[i,12]*pi/180)*sin(Lat*pi/180)-sin(calculation[i,12]*pi/180)*cos(Lat*pi/180))/cos(calculation[i,15]) 
                calculation[i,19] = asin(calculation[i,17])*180/pi # fai option 1, deg
                calculation[i,20] = acos(calculation[i,18])*180/pi # fai option 2, deg
                
                if (calculation[i,17] > 0): calculation[i,21] = calculation[i,20] # solar azimuth, deg
                elif (calculation[i,18] > 0): calculation[i,21] = calculation[i,19]
                else: calculation[i,21] = -180-calculation[i,19]

                # surface-solar azimuth, >90 : in shade,
                calculation[i,22] = abs(calculation[i,21]- 0) # South
                calculation[i,23] = abs(calculation[i,21]- (-45)) # SE
                calculation[i,24] = abs(calculation[i,21]- (-90)) # E
                calculation[i,25] = abs(calculation[i,21]- (-135)) # NE
                calculation[i,26] = abs(calculation[i,21]- 180) # N
                calculation[i,27] = abs(calculation[i,21]- 135) # NW
                calculation[i,28] = abs(calculation[i,21]- 90) # W
                calculation[i,29] = abs(calculation[i,21]- 45) # SW

                # angle of incidence, angle between the incident beam and the surface's normal vector
                calculation[i,38] = cos(calculation[i,15])*cos(calculation[i,22]*pi/180)*sin(sigma*pi/180)+sin(calculation[i,15])*cos(sigma*pi/180) # S
                calculation[i,39] = cos(calculation[i,15])*cos(calculation[i,23]*pi/180)*sin(sigma*pi/180)+sin(calculation[i,15])*cos(sigma*pi/180) # SE
                calculation[i,40] = cos(calculation[i,15])*cos(calculation[i,24]*pi/180)*sin(sigma*pi/180)+sin(calculation[i,15])*cos(sigma*pi/180) # E
                calculation[i,41] = cos(calculation[i,15])*cos(calculation[i,25]*pi/180)*sin(sigma*pi/180)+sin(calculation[i,15])*cos(sigma*pi/180) # NE
                calculation[i,42] = cos(calculation[i,15])*cos(calculation[i,26]*pi/180)*sin(sigma*pi/180)+sin(calculation[i,15])*cos(sigma*pi/180) # N
                calculation[i,43] = cos(calculation[i,15])*cos(calculation[i,27]*pi/180)*sin(sigma*pi/180)+sin(calculation[i,15])*cos(sigma*pi/180) # NW
                calculation[i,44] = cos(calculation[i,15])*cos(calculation[i,28]*pi/180)*sin(sigma*pi/180)+sin(calculation[i,15])*cos(sigma*pi/180) # W
                calculation[i,45] = cos(calculation[i,15])*cos(calculation[i,29]*pi/180)*sin(sigma*pi/180)+sin(calculation[i,15])*cos(sigma*pi/180) # SW

                # i_beta (Not needed)
        ##        calculation[i,30] = acos(calculation[i,38])*180/pi # S
        ##        calculation[i,31] = acos(calculation[i,39])*180/pi # SE
        ##        calculation[i,32] = acos(calculation[i,40])*180/pi # E
        ##        calculation[i,33] = acos(calculation[i,41])*180/pi # NE
        ##        calculation[i,34] = acos(calculation[i,42])*180/pi # N
        ##        calculation[i,35] = acos(calculation[i,43])*180/pi # MW
        ##        calculation[i,36] = acos(calculation[i,44])*180/pi # W
        ##        calculation[i,37] = acos(calculation[i,45])*180/pi # SW

                # Beam component, Wh/m2
                if (calculation[i,22]>90 and calculation[i,22]<270): calculation[i,46] = 0
                elif (calculation[i,38]<0): calculation[i,46] = 0
                else: calculation[i,46] = calculation[i,6]*calculation[i,38]

                if (calculation[i,23]>90 and calculation[i,23]<270): calculation[i,47] = 0
                elif (calculation[i,39]<0): calculation[i,47] = 0
                else: calculation[i,47] = calculation[i,6]*calculation[i,39]

                if (calculation[i,24]>90 and calculation[i,24]<270): calculation[i,48] = 0
                elif (calculation[i,40]<0): calculation[i,48] = 0
                else: calculation[i,48] = calculation[i,6]*calculation[i,40]


                if (calculation[i,25]>90 and calculation[i,25]<270): calculation[i,49] = 0
                elif (calculation[i,41]<0): calculation[i,49] = 0
                else: calculation[i,49] = calculation[i,6]*calculation[i,41]
                    

                if (calculation[i,26]>90 and calculation[i,26]<270): calculation[i,50] = 0
                elif (calculation[i,42]<0): calculation[i,50] = 0
                else: calculation[i,50] = calculation[i,6]*calculation[i,42]
                    
                if (calculation[i,27]>90 and calculation[i,27]<270): calculation[i,51] = 0
                elif (calculation[i,43]<0): calculation[i,51] = 0
                else: calculation[i,51] = calculation[i,6]*calculation[i,43]

                if (calculation[i,28]>90 and calculation[i,28]<270): calculation[i,52] = 0
                elif (calculation[i,44]<0): calculation[i,52] = 0
                else: calculation[i,52] = calculation[i,6]*calculation[i,44]

                if (calculation[i,29]>90 and calculation[i,29]<270): calculation[i,53] = 0
                elif (calculation[i,45]<0): calculation[i,53] = 0
                else: calculation[i,53] = calculation[i,6]*calculation[i,45]
                   

                # Diffuse component, Y
                calculation[i,54] = max(0.45,0.55+0.437*calculation[i,38]+0.313*(calculation[i,38]**2)) # S
                calculation[i,55] = max(0.45,0.55+0.437*calculation[i,39]+0.313*(calculation[i,39]**2)) # SE
                calculation[i,56] = max(0.45,0.55+0.437*calculation[i,40]+0.313*(calculation[i,40]**2)) # E
                calculation[i,57] = max(0.45,0.55+0.437*calculation[i,41]+0.313*(calculation[i,41]**2)) # NE
                calculation[i,58] = max(0.45,0.55+0.437*calculation[i,42]+0.313*(calculation[i,42]**2)) # N 
                calculation[i,59] = max(0.45,0.55+0.437*calculation[i,43]+0.313*(calculation[i,43]**2)) # NW
                calculation[i,60] = max(0.45,0.55+0.437*calculation[i,44]+0.313*(calculation[i,44]**2)) # W
                calculation[i,61] = max(0.45,0.55+0.437*calculation[i,45]+0.313*(calculation[i,45]**2)) # SW

                # diffuse radiation, W/m2
                if (sigma <= 90):
                    calculation[i,62] = calculation[i,7]*(calculation[i,54]*sin(sigma*pi/180)+cos(sigma*pi/180)) # S
                    calculation[i,63] = calculation[i,7]*(calculation[i,55]*sin(sigma*pi/180)+cos(sigma*pi/180)) # SE
                    calculation[i,64] = calculation[i,7]*(calculation[i,56]*sin(sigma*pi/180)+cos(sigma*pi/180)) # E
                    calculation[i,65] = calculation[i,7]*(calculation[i,57]*sin(sigma*pi/180)+cos(sigma*pi/180)) # NE
                    calculation[i,66] = calculation[i,7]*(calculation[i,58]*sin(sigma*pi/180)+cos(sigma*pi/180)) # N
                    calculation[i,67] = calculation[i,7]*(calculation[i,59]*sin(sigma*pi/180)+cos(sigma*pi/180)) # NW
                    calculation[i,68] = calculation[i,7]*(calculation[i,60]*sin(sigma*pi/180)+cos(sigma*pi/180)) # W
                    calculation[i,69] = calculation[i,7]*(calculation[i,61]*sin(sigma*pi/180)+cos(sigma*pi/180)) # SW
                else:
                    calculation[i,62] = calculation[i,7]*(calculation[i,54]*sin(sigma*pi/180)) # S
                    calculation[i,63] = calculation[i,7]*(calculation[i,55]*sin(sigma*pi/180)) # SE
                    calculation[i,64] = calculation[i,7]*(calculation[i,56]*sin(sigma*pi/180)) # E
                    calculation[i,65] = calculation[i,7]*(calculation[i,57]*sin(sigma*pi/180)) # NE
                    calculation[i,66] = calculation[i,7]*(calculation[i,58]*sin(sigma*pi/180)) # N
                    calculation[i,67] = calculation[i,7]*(calculation[i,59]*sin(sigma*pi/180)) # NW
                    calculation[i,68] = calculation[i,7]*(calculation[i,60]*sin(sigma*pi/180)) # W
                    calculation[i,69] = calculation[i,7]*(calculation[i,61]*sin(sigma*pi/180)) # SW

                calculation[i,70] = (calculation[i,6]*sin(calculation[i,15])+calculation[i,7])*r_g*(1-cos(sigma*pi/180))/2 # ground reflected total radiation incident on the nonvertical inclination

                # specific humidity
                calculation_specific_humidity[i,0] = data_from_epw[i,0] # Dry bulb Temperature    
                calculation_specific_humidity[i,1]=(water_a0+(calculation_specific_humidity[i,0]*(water_a1+calculation_specific_humidity[i,0]*(water_a2+calculation_specific_humidity[i,0]*(water_a3+calculation_specific_humidity[i,0]*(water_a4+calculation_specific_humidity[i,0]*(water_a5+calculation_specific_humidity[i,0]*water_a6)))))))# e_water {hPa}, saturation vapor pressure
                calculation_specific_humidity[i,2] =(ice_a0+(calculation_specific_humidity[i,0]*(ice_a1+calculation_specific_humidity[i,0]*(ice_a2+calculation_specific_humidity[i,0]*(ice_a3+calculation_specific_humidity[i,0]*(ice_a4+calculation_specific_humidity[i,0]*(ice_a5+calculation_specific_humidity[i,0]*ice_a6))))))) # e_ice {hPa}, saturation vapor pressure
                calculation_specific_humidity[i,3] = min(calculation_specific_humidity[i,1],calculation_specific_humidity[i,2]) # e {hPa},  saturation vapor pressure
                calculation_specific_humidity[i,4] = data_from_epw[i,5]*0.01 # RHum {%}   
                calculation_specific_humidity[i,5] = data_from_epw[i,6]/100 # Pressure
                calculation_specific_humidity[i,6] = calculation_specific_humidity[i,3]*calculation_specific_humidity[i,4] # Partial pressure of water
                calculation_specific_humidity[i,7] = calculation_specific_humidity[i,6]/calculation_specific_humidity[i,5] # Mole fraction, volume mixing ratio of water
                calculation_specific_humidity[i,8] = (calculation_specific_humidity[i,7]*18.015340)/(calculation_specific_humidity[i,7]*18.015340+(1-calculation_specific_humidity[i,7])*28.96440) # Specific humidity, dry air (mass mixing ratio in wet air)
                calculation_specific_humidity[i,9] = calculation_specific_humidity[i,8]/(1-calculation_specific_humidity[i,8]) # Specific humidity dry air (mass mixing ratio in dry air)
                calculation_specific_humidity[i,10] = calculation_specific_humidity[i,9]*1000 # Specific humidity, dry air (mass mixing ratio in dry air)

                # hourly_output
                hourly_output[i,0] = data_from_epw[i,0] # Dry bulb temperature
                hourly_output[i,1] = data_from_epw[i,4] # Wind speed
                hourly_output[i,2] = calculation[i,46] + calculation[i,62] + calculation[i,70] # S
                hourly_output[i,3] = calculation[i,47] + calculation[i,63] + calculation[i,70] # SE
                hourly_output[i,4] = calculation[i,48] + calculation[i,64] + calculation[i,70] # E
                hourly_output[i,5] = calculation[i,49] + calculation[i,65] + calculation[i,70] # NE
                hourly_output[i,6] = calculation[i,50] + calculation[i,66] + calculation[i,70] # N
                hourly_output[i,7] = calculation[i,51] + calculation[i,67] + calculation[i,70] # NW
                hourly_output[i,8] = calculation[i,52] + calculation[i,68] + calculation[i,70] # W
                hourly_output[i,9] = calculation[i,53] + calculation[i,69] + calculation[i,70] # SW
                hourly_output[i,10] = data_from_epw[i,1] # HOR
                hourly_output[i,11] = calculation[i,16] # Solar altitude
                hourly_output[i,12] = calculation_specific_humidity[i,10] # Specific Humidity, dry air
                hourly_output[i,13] = data_from_epw[i,6] # Atmospheric station pressure
                hourly_output[i,14] = data_from_epw[i,5] #Relative humidity
               
                # Overhang & Fin
                if (hourly_output[i,2]==0):
                    pass
##                    # Overhang
##                    SRF[i,0] = 0
##                    SRF[i,8] = 0
##                    SRF[i,16] = 0
##                    # Fin
##                    SRF[i,24] = 0
##                    SRF[i,32] = 0
##                    SRF[i,40] = 0

                else:
                    # Overhang
                    SRF[i,0] = (max(0,1-(0.5*tan(radians(30))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,46]+(1-30/90)*calculation[i,62]+calculation[i,70])/hourly_output[i,2]
                    SRF[i,8] = (max(0,1-(0.5*tan(radians(45))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,46]+(1-45/90)*calculation[i,62]+calculation[i,70])/hourly_output[i,2]
                    SRF[i,16] = (max(0,1-(0.5*tan(radians(60))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,46]+(1-60/90)*calculation[i,62]+calculation[i,70])/hourly_output[i,2]
                    # Fin
                    if (calculation[i,21]- 0 > 90) or ((calculation[i,21]- 0)<0):
                        SRF[i,24] = 1; SRF[i,32] = 1; SRF[i,40] = 1
                    else:
                        SRF[i,24] = ((max(0,1-0.5*tan(radians(30))/tan(radians(90-abs(calculation[i,21]-0)))))*calculation[i,46]+calculation[i,62]+calculation[i,70])/hourly_output[i,2]
                        SRF[i,32] = ((max(0,1-0.5*tan(radians(45))/tan(radians(90-abs(calculation[i,21]-0)))))*calculation[i,46]+calculation[i,62]+calculation[i,70])/hourly_output[i,2]
                        SRF[i,40] = ((max(0,1-0.5*tan(radians(60))/tan(radians(90-abs(calculation[i,21]-0)))))*calculation[i,46]+calculation[i,62]+calculation[i,70])/hourly_output[i,2]

                if (hourly_output[i,3]==0):
                    pass
##                    # Overhang
##                    SRF[i,1] = 0
##                    SRF[i,8] = 0
##                    SRF[i,17] = 0
##                    # Fin
##                    SRF[i,25] = 0
##                    SRF[i,33] = 0
##                    SRF[i,41] = 0
                else:
                    # Overhang
                    SRF[i,1] = (max(0,1-(0.5*tan(radians(30))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,47]+(1-30/90)*calculation[i,63]+calculation[i,70])/hourly_output[i,3]
                    SRF[i,9] = (max(0,1-(0.5*tan(radians(45))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,47]+(1-45/90)*calculation[i,63]+calculation[i,70])/hourly_output[i,3]
                    SRF[i,17] = (max(0,1-(0.5*tan(radians(60))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,47]+(1-60/90)*calculation[i,63]+calculation[i,70])/hourly_output[i,3]
                    # Fin
                    if (calculation[i,21]-(-45)>90 or (calculation[i,21]-(-45))<0):
                        SRF[i,25] = 1; SRF[i,33] = 1; SRF[i,41] = 1
                    else: 
                        SRF[i,25] = ((max(0,1-0.5*tan(radians(30))/tan(radians(90-abs(calculation[i,21]-(-45))))))*calculation[i,47]+calculation[i,63]+calculation[i,70])/hourly_output[i,3]
                        SRF[i,33] = ((max(0,1-0.5*tan(radians(45))/tan(radians(90-abs(calculation[i,21]-(-45))))))*calculation[i,47]+calculation[i,63]+calculation[i,70])/hourly_output[i,3]
                        SRF[i,41] = ((max(0,1-0.5*tan(radians(60))/tan(radians(90-abs(calculation[i,21]-(-45))))))*calculation[i,47]+calculation[i,63]+calculation[i,70])/hourly_output[i,3]

                if (hourly_output[i,4]==0):
                    pass
##                    # Overhang
##                    SRF[i,2] = 0
##                    SRF[i,10] = 0
##                    SRF[i,18] = 0
##                    # Fin
##                    SRF[i,26] = 0
##                    SRF[i,34] = 0
##                    SRF[i,42] = 0
                else:
                    # Overhang
                    SRF[i,2] = (max(0,1-(0.5*tan(radians(30))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,48]+(1-30/90)*calculation[i,64]+calculation[i,70])/hourly_output[i,4]
                    SRF[i,10] = (max(0,1-(0.5*tan(radians(45))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,48]+(1-45/90)*calculation[i,64]+calculation[i,70])/hourly_output[i,4]
                    SRF[i,18] = (max(0,1-(0.5*tan(radians(60))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,48]+(1-60/90)*calculation[i,64]+calculation[i,70])/hourly_output[i,4]
                    # Fin
                    if (calculation[i,21]-(-90)>90 or (calculation[i,21]-(-90))<0):
                        SRF[i,26] = 1; SRF[i,34] = 1; SRF[i,42] = 1
                    else:
                        SRF[i,26] = ((max(0,1-0.5*tan(radians(30))/tan(radians(90-abs(calculation[i,21]-(-90))))))*calculation[i,48]+calculation[i,64]+calculation[i,70])/hourly_output[i,4]
                        SRF[i,34] = ((max(0,1-0.5*tan(radians(45))/tan(radians(90-abs(calculation[i,21]-(-90))))))*calculation[i,48]+calculation[i,64]+calculation[i,70])/hourly_output[i,4]
                        SRF[i,42] = ((max(0,1-0.5*tan(radians(60))/tan(radians(90-abs(calculation[i,21]-(-90))))))*calculation[i,48]+calculation[i,64]+calculation[i,70])/hourly_output[i,4]

                if (hourly_output[i,5]==0):
                    pass
##                    # Overhang
##                    SRF[i,3] = 0
##                    SRF[i,11] = 0
##                    SRF[i,19] = 0
##                    # Fin
##                    SRF[i,27] = 0
##                    SRF[i,35] = 0
##                    SRF[i,43] = 0
                else:
                    # Overhang
                    SRF[i,3] = (max(0,1-(0.5*tan(radians(30))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,49]+(1-30/90)*calculation[i,65]+calculation[i,70])/hourly_output[i,5]
                    SRF[i,11] = (max(0,1-(0.5*tan(radians(45))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,49]+(1-45/90)*calculation[i,65]+calculation[i,70])/hourly_output[i,5]
                    SRF[i,19] = (max(0,1-(0.5*tan(radians(60))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,49]+(1-60/90)*calculation[i,65]+calculation[i,70])/hourly_output[i,5]
                    # Fin
                    if (calculation[i,21]-(-135)>90 or (calculation[i,21]-(-135))<0):
                        SRF[i,27] = 1; SRF[i,35] = 1; SRF[i,43] = 1
                    else:
                        SRF[i,27] = ((max(0,1-0.5*tan(radians(30))/tan(radians(90-abs(calculation[i,21]-(-135))))))*calculation[i,49]+calculation[i,65]+calculation[i,70])/hourly_output[i,5]
                        SRF[i,35] = ((max(0,1-0.5*tan(radians(45))/tan(radians(90-abs(calculation[i,21]-(-135))))))*calculation[i,49]+calculation[i,65]+calculation[i,70])/hourly_output[i,5]
                        SRF[i,43] = ((max(0,1-0.5*tan(radians(60))/tan(radians(90-abs(calculation[i,21]-(-135))))))*calculation[i,49]+calculation[i,65]+calculation[i,70])/hourly_output[i,5]

                if (hourly_output[i,6]==0):
                    pass
##                    # Overhang
##                    SRF[i,4] = 0
##                    SRF[i,12] = 0
##                    SRF[i,20] = 0
##                    # Fin
##                    SRF[i,28] = 0
##                    SRF[i,36] = 0
##                    SRF[i,44] = 0
                else:
                    # Overhang
                    SRF[i,4] = (max(0,1-(0.5*tan(radians(30))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,50]+(1-30/90)*calculation[i,66]+calculation[i,70])/hourly_output[i,6]
                    SRF[i,12] = (max(0,1-(0.5*tan(radians(45))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,50]+(1-45/90)*calculation[i,66]+calculation[i,70])/hourly_output[i,6]
                    SRF[i,20] = (max(0,1-(0.5*tan(radians(60))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,50]+(1-60/90)*calculation[i,66]+calculation[i,70])/hourly_output[i,6]
                    # Fin
                    if (calculation[i,21]-180>0 or (calculation[i,21]-180)<-90):
                        SRF[i,28] = 1; SRF[i,36] = 1; SRF[i,44] = 1
                    else:
                        SRF[i,28] = ((max(0,1-0.5*tan(radians(30))/tan(radians(90-abs(calculation[i,21]-180)))))*calculation[i,50]+calculation[i,66]+calculation[i,70])/hourly_output[i,6]
                        SRF[i,36] = ((max(0,1-0.5*tan(radians(45))/tan(radians(90-abs(calculation[i,21]-180)))))*calculation[i,50]+calculation[i,66]+calculation[i,70])/hourly_output[i,6]
                        SRF[i,44] = ((max(0,1-0.5*tan(radians(60))/tan(radians(90-abs(calculation[i,21]-180)))))*calculation[i,50]+calculation[i,66]+calculation[i,70])/hourly_output[i,6]

                if (hourly_output[i,7]==0):
                    pass
##                    # Overhang
##                    SRF[i,5] = 0
##                    SRF[i,13] = 0
##                    SRF[i,21] = 0
##                    # Fin
##                    SRF[i,29] = 0
##                    SRF[i,37] = 0
##                    SRF[i,45] = 0
                else:
                    # Overhang
                    SRF[i,5] = (max(0,1-(0.5*tan(radians(30))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,51]+(1-30/90)*calculation[i,67]+calculation[i,70])/hourly_output[i,7]
                    SRF[i,13] = (max(0,1-(0.5*tan(radians(45))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,51]+(1-45/90)*calculation[i,67]+calculation[i,70])/hourly_output[i,7]
                    SRF[i,21] = (max(0,1-(0.5*tan(radians(60))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,51]+(1-60/90)*calculation[i,67]+calculation[i,70])/hourly_output[i,7]
                    # Fin
                    if (calculation[i,21]-135>0 or (calculation[i,21]-135)<-90):
                        SRF[i,29] = 1; SRF[i,37] = 1; SRF[i,45] = 1
                    else:
                        SRF[i,29] = ((max(0,1-0.5*tan(radians(30))/tan(radians(90-abs(calculation[i,21]-135)))))*calculation[i,51]+calculation[i,67]+calculation[i,70])/hourly_output[i,7]
                        SRF[i,37] = ((max(0,1-0.5*tan(radians(45))/tan(radians(90-abs(calculation[i,21]-135)))))*calculation[i,51]+calculation[i,67]+calculation[i,70])/hourly_output[i,7]
                        SRF[i,45] = ((max(0,1-0.5*tan(radians(60))/tan(radians(90-abs(calculation[i,21]-135)))))*calculation[i,51]+calculation[i,67]+calculation[i,70])/hourly_output[i,7]

                if (hourly_output[i,8]==0):
                    pass
##                    # Overhang
##                    SRF[i,6] = 0
##                    SRF[i,14] = 0
##                    SRF[i,22] = 0
##                    # Fin
##                    SRF[i,30] = 0
##                    SRF[i,38] = 0
##                    SRF[i,46] = 0
                else:
                    # Overhang
                    SRF[i,6] = (max(0,1-(0.5*tan(radians(30))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,52]+(1-30/90)*calculation[i,68]+calculation[i,70])/hourly_output[i,8]
                    SRF[i,14] = (max(0,1-(0.5*tan(radians(45))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,52]+(1-45/90)*calculation[i,68]+calculation[i,70])/hourly_output[i,8]
                    SRF[i,22] = (max(0,1-(0.5*tan(radians(60))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,52]+(1-60/90)*calculation[i,68]+calculation[i,70])/hourly_output[i,8]
                    # Fin
                    if (calculation[i,21]-90>0 or calculation[i,21]-90<-90):
                        SRF[i,30] = 1; SRF[i,38] = 1; SRF[i,46] = 1
                    else:
                        SRF[i,30] = ((max(0,1-0.5*tan(radians(30))/tan(radians(90-abs(calculation[i,21]-90)))))*calculation[i,52]+calculation[i,68]+calculation[i,70])/hourly_output[i,8]
                        SRF[i,38] = ((max(0,1-0.5*tan(radians(45))/tan(radians(90-abs(calculation[i,21]-90)))))*calculation[i,52]+calculation[i,68]+calculation[i,70])/hourly_output[i,8]
                        SRF[i,46] = ((max(0,1-0.5*tan(radians(60))/tan(radians(90-abs(calculation[i,21]-90)))))*calculation[i,52]+calculation[i,68]+calculation[i,70])/hourly_output[i,8]

                if (hourly_output[i,9]==0):
                    pass
##                    # Overhang
##                    SRF[i,7] = 0
##                    SRF[i,15] = 0
##                    SRF[i,23] = 0
##                    # Fin
##                    SRF[i,31] = 0
##                    SRF[i,39] = 0
##                    SRF[i,47] = 0
                else:
                    # Overhang
                    SRF[i,7] = (max(0,1-(0.5*tan(radians(30))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,53]+(1-30/90)*calculation[i,69]+calculation[i,70])/hourly_output[i,9]
                    SRF[i,15] = (max(0,1-(0.5*tan(radians(45))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,53]+(1-45/90)*calculation[i,69]+calculation[i,70])/hourly_output[i,9]
                    SRF[i,23] = (max(0,1-(0.5*tan(radians(60))/tan(radians(90-max(calculation[i,16],0)))))*calculation[i,53]+(1-60/90)*calculation[i,69]+calculation[i,70])/hourly_output[i,9]
                    # Fin
                    if (calculation[i,21]-45>0 or calculation[i,21]-45<-90):
                        SRF[i,31] = 1; SRF[i,39] = 1; SRF[i,47] = 1
                    else:
                        SRF[i,31] = ((max(0,1-0.5*tan(radians(30))/tan(radians(90-abs(calculation[i,21]-45)))))*calculation[i,53]+calculation[i,69]+calculation[i,70])/hourly_output[i,9]
                        SRF[i,39] = ((max(0,1-0.5*tan(radians(45))/tan(radians(90-abs(calculation[i,21]-45)))))*calculation[i,53]+calculation[i,69]+calculation[i,70])/hourly_output[i,9]
                        SRF[i,47] = ((max(0,1-0.5*tan(radians(60))/tan(radians(90-abs(calculation[i,21]-45)))))*calculation[i,53]+calculation[i,69]+calculation[i,70])/hourly_output[i,9]

                # Horizon
                if (hourly_output[i,2] == 0): # S
                    pass
##                    SRF[i,48] = 0
##                    SRF[i,56] = 0
##                    SRF[i,64] = 0
##                    SRF[i,72] = 0
##                    SRF[i,80] = 0
##                    SRF[i,88] = 0
                else:
                    if (max(calculation[i,16],0)<10): SRF[i,48] = 1-calculation[i,46]/hourly_output[i,2]
                    else: SRF[i,48] = 1

                    if (max(calculation[i,16],0)<20): SRF[i,56] = 1-calculation[i,46]/hourly_output[i,2]
                    else: SRF[i,56] = 1

                    if (max(calculation[i,16],0)<30): SRF[i,64] = 1-calculation[i,46]/hourly_output[i,2]
                    else: SRF[i,64] = 1

                    if (max(calculation[i,16],0)<40): SRF[i,72] = 1-calculation[i,46]/hourly_output[i,2]
                    else: SRF[i,72] = 1

                    if (max(calculation[i,16],0)<50): SRF[i,80] = 1-calculation[i,46]/hourly_output[i,2]
                    else: SRF[i,80] = 1

                    if (max(calculation[i,16],0)<60): SRF[i,88] = 1-calculation[i,46]/hourly_output[i,2]
                    else: SRF[i,88] = 1  

                if (hourly_output[i,3] == 0): # SE
                    pass
##                    SRF[i,49] = 0
##                    SRF[i,57] = 0
##                    SRF[i,65] = 0
##                    SRF[i,73] = 0
##                    SRF[i,81] = 0
##                    SRF[i,89] = 0
                else:
                    if (max(calculation[i,16],0)<10): SRF[i,49] = 1-calculation[i,47]/hourly_output[i,3]
                    else: SRF[i,49] = 1

                    if (max(calculation[i,16],0)<20): SRF[i,57] = 1-calculation[i,47]/hourly_output[i,3]
                    else: SRF[i,57] = 1

                    if (max(calculation[i,16],0)<30): SRF[i,65] = 1-calculation[i,47]/hourly_output[i,3]
                    else: SRF[i,65] = 1

                    if (max(calculation[i,16],0)<40): SRF[i,73] = 1-calculation[i,47]/hourly_output[i,3]
                    else: SRF[i,73] = 1

                    if (max(calculation[i,16],0)<50): SRF[i,81] = 1-calculation[i,47]/hourly_output[i,3]
                    else: SRF[i,81] = 1
                        
                    if (max(calculation[i,16],0)<60): SRF[i,89] = 1-calculation[i,47]/hourly_output[i,3]
                    else: SRF[i,89] = 1
                    
                if (hourly_output[i,4] == 0): # E
                    pass
##                    SRF[i,50] = 0
##                    SRF[i,58] = 0
##                    SRF[i,66] = 0
##                    SRF[i,74] = 0
##                    SRF[i,82] = 0
##                    SRF[i,90] = 0
                else:
                    if (max(calculation[i,16],0)<10): SRF[i,50] = 1-calculation[i,48]/hourly_output[i,4]
                    else: SRF[i,50] = 1

                    if (max(calculation[i,16],0)<20): SRF[i,58] = 1-calculation[i,48]/hourly_output[i,4]
                    else: SRF[i,58] = 1

                    if (max(calculation[i,16],0)<30): SRF[i,66] = 1-calculation[i,48]/hourly_output[i,4]
                    else: SRF[i,66] = 1

                    if (max(calculation[i,16],0)<40): SRF[i,74] = 1-calculation[i,48]/hourly_output[i,4]
                    else: SRF[i,74] = 1

                    if (max(calculation[i,16],0)<50): SRF[i,82] = 1-calculation[i,48]/hourly_output[i,4]
                    else: SRF[i,82] = 1

                    if (max(calculation[i,16],0)<60): SRF[i,90] = 1-calculation[i,48]/hourly_output[i,4]
                    else: SRF[i,90] = 1
                    
                if (hourly_output[i,5] == 0): # NE
                    pass
##                    SRF[i,51] = 0
##                    SRF[i,59] = 0
##                    SRF[i,67] = 0
##                    SRF[i,75] = 0
##                    SRF[i,83] = 0
##                    SRF[i,91] = 0
                else:
                    if (max(calculation[i,16],0)<10): SRF[i,51] = 1-calculation[i,49]/hourly_output[i,5]
                    else: SRF[i,51] = 1

                    if (max(calculation[i,16],0)<20): SRF[i,59] = 1-calculation[i,49]/hourly_output[i,5]
                    else: SRF[i,59] = 1

                    if (max(calculation[i,16],0)<30): SRF[i,67] = 1-calculation[i,49]/hourly_output[i,5]
                    else: SRF[i,67] = 1

                    if (max(calculation[i,16],0)<40): SRF[i,75] = 1-calculation[i,49]/hourly_output[i,5]
                    else: SRF[i,75] = 1

                    if (max(calculation[i,16],0)<50): SRF[i,83] = 1-calculation[i,49]/hourly_output[i,5]
                    else: SRF[i,83] = 1

                    if (max(calculation[i,16],0)<60): SRF[i,91] = 1-calculation[i,49]/hourly_output[i,5]
                    else: SRF[i,91] = 1

                if (hourly_output[i,6] == 0): # N
                    pass
##                    SRF[i,52] = 0
##                    SRF[i,60] = 0
##                    SRF[i,68] = 0
##                    SRF[i,76] = 0
##                    SRF[i,84] = 0
##                    SRF[i,92] = 0
                else:
                    if (max(calculation[i,16],0)<10): SRF[i,52] = 1-calculation[i,50]/hourly_output[i,6]
                    else: SRF[i,52] = 1

                    if (max(calculation[i,16],0)<20): SRF[i,60] = 1-calculation[i,50]/hourly_output[i,6]
                    else: SRF[i,60] = 1

                    if (max(calculation[i,16],0)<30): SRF[i,68] = 1-calculation[i,50]/hourly_output[i,6]
                    else: SRF[i,68] = 1

                    if (max(calculation[i,16],0)<40): SRF[i,76] = 1-calculation[i,50]/hourly_output[i,6]
                    else: SRF[i,76] = 1

                    if (max(calculation[i,16],0)<50): SRF[i,84] = 1-calculation[i,50]/hourly_output[i,6]
                    else: SRF[i,84] = 1

                    if (max(calculation[i,16],0)<60): SRF[i,92] = 1-calculation[i,50]/hourly_output[i,6]
                    else: SRF[i,92] = 1

                if (hourly_output[i,7] == 0): # NW
                    pass
##                    SRF[i,53] = 0
##                    SRF[i,61] = 0
##                    SRF[i,69] = 0
##                    SRF[i,77] = 0
##                    SRF[i,85] = 0
##                    SRF[i,93] = 0
                else:
                    if (max(calculation[i,16],0)<10): SRF[i,53] = 1-calculation[i,51]/hourly_output[i,7]
                    else: SRF[i,53] = 1

                    if (max(calculation[i,16],0)<20): SRF[i,61] = 1-calculation[i,51]/hourly_output[i,7]
                    else: SRF[i,61] = 1

                    if (max(calculation[i,16],0)<30): SRF[i,69] = 1-calculation[i,51]/hourly_output[i,7]
                    else: SRF[i,69] = 1

                    if (max(calculation[i,16],0)<40): SRF[i,77] = 1-calculation[i,51]/hourly_output[i,7]
                    else: SRF[i,77] = 1

                    if (max(calculation[i,16],0)<50): SRF[i,85] = 1-calculation[i,51]/hourly_output[i,7]
                    else: SRF[i,85] = 1

                    if (max(calculation[i,16],0)<60): SRF[i,93] = 1-calculation[i,51]/hourly_output[i,7]
                    else: SRF[i,93] = 1

                if (hourly_output[i,8] == 0): # W
                    pass
##                    SRF[i,54] = 0
##                    SRF[i,62] = 0
##                    SRF[i,70] = 0
##                    SRF[i,78] = 0
##                    SRF[i,86] = 0
##                    SRF[i,94] = 0
                else:
                    if (max(calculation[i,16],0)<10): SRF[i,54] = 1-calculation[i,52]/hourly_output[i,8]
                    else: SRF[i,54] = 1
                        
                    if (max(calculation[i,16],0)<20): SRF[i,62] = 1-calculation[i,52]/hourly_output[i,8]
                    else: SRF[i,62] = 1

                    if (max(calculation[i,16],0)<30): SRF[i,70] = 1-calculation[i,52]/hourly_output[i,8]
                    else: SRF[i,70] = 1

                    if (max(calculation[i,16],0)<40): SRF[i,78] = 1-calculation[i,52]/hourly_output[i,8]
                    else: SRF[i,78] = 1

                    if (max(calculation[i,16],0)<50): SRF[i,86] = 1-calculation[i,52]/hourly_output[i,8]
                    else: SRF[i,86] = 1

                    if (max(calculation[i,16],0)<60): SRF[i,94] = 1-calculation[i,52]/hourly_output[i,8]
                    else: SRF[i,94] = 1

                if (hourly_output[i,9] == 0): # SW
                    pass
##                    SRF[i,55] = 0
##                    SRF[i,63] = 0
##                    SRF[i,71] = 0
##                    SRF[i,79] = 0
##                    SRF[i,87] = 0
##                    SRF[i,95] = 0
                else:
                    if (max(calculation[i,16],0)<10): SRF[i,55] = 1-calculation[i,53]/hourly_output[i,9]
                    else: SRF[i,55] = 1

                    if (max(calculation[i,16],0)<20): SRF[i,63] = 1-calculation[i,53]/hourly_output[i,9]
                    else: SRF[i,63] = 1

                    if (max(calculation[i,16],0)<30): SRF[i,71] = 1-calculation[i,53]/hourly_output[i,9]
                    else: SRF[i,71] = 1

                    if (max(calculation[i,16],0)<40): SRF[i,79] = 1-calculation[i,53]/hourly_output[i,9]
                    else: SRF[i,79] = 1

                    if (max(calculation[i,16],0)<50): SRF[i,87] = 1-calculation[i,53]/hourly_output[i,9]
                    else: SRF[i,87] = 1

                    if (max(calculation[i,16],0)<60): SRF[i,95] = 1-calculation[i,53]/hourly_output[i,9]
                    else: SRF[i,95] = 1

            if (sigma == 30):
                for j in range(0,8760):
                    Esol_30[j,0] = hourly_output[j,2]; Esol_30[j,1] = hourly_output[j,3]; Esol_30[j,2] = hourly_output[j,4]; Esol_30[j,3] = hourly_output[j,5];
                    Esol_30[j,4] = hourly_output[j,6]; Esol_30[j,5] = hourly_output[j,7]; Esol_30[j,6] = hourly_output[j,8]; Esol_30[j,7] = hourly_output[j,9];
                    
            elif (sigma == 45):
                for j in range(0,8760):
                    Esol_45[j,0] = hourly_output[j,2]; Esol_45[j,1] = hourly_output[j,3]; Esol_45[j,2] = hourly_output[j,4]; Esol_45[j,3] = hourly_output[j,5];
                    Esol_45[j,4] = hourly_output[j,6]; Esol_45[j,5] = hourly_output[j,7]; Esol_45[j,6] = hourly_output[j,8]; Esol_45[j,7] = hourly_output[j,9];
                    
            elif (sigma == 60):
                for j in range(0,8760):
                    Esol_60[j,0] = hourly_output[j,2]; Esol_60[j,1] = hourly_output[j,3]; Esol_60[j,2] = hourly_output[j,4]; Esol_60[j,3] = hourly_output[j,5];
                    Esol_60[j,4] = hourly_output[j,6]; Esol_60[j,5] = hourly_output[j,7]; Esol_60[j,6] = hourly_output[j,8]; Esol_60[j,7] = hourly_output[j,9];
                    
            elif (sigma == 90):
                for j in range(0,8760):
                    Esol_90[j,0] = hourly_output[j,2]; Esol_90[j,1] = hourly_output[j,3]; Esol_90[j,2] = hourly_output[j,4]; Esol_90[j,3] = hourly_output[j,5];
                    Esol_90[j,4] = hourly_output[j,6]; Esol_90[j,5] = hourly_output[j,7]; Esol_90[j,6] = hourly_output[j,8]; Esol_90[j,7] = hourly_output[j,9];

        for i in range(0,8760):
            for j in range(0,24):
                SRF_overhang[i][j] = SRF[i][j]; SRF_fin[i][j] = SRF[i][j+24]
                
            for j in range(0,48):
                SRF_horizon[i][j] = SRF[i][j+48]

        # Change unit from W to kWh
        Esol_30 /= 1000
        Esol_45 /= 1000
        Esol_60 /= 1000
        Esol_90 /= 1000
        
        # Pickling
        partial_name = "".join(["./Weather/",self.epw_file_name[:-4],"_"])
        
        np.save("".join([partial_name, "climate.npy"]),hourly_output,allow_pickle=True, fix_imports=False)
        
        np.save("".join([partial_name, "direct_solar.npy"]),calculation[:,6],allow_pickle=True, fix_imports=False)
        np.save("".join([partial_name, "diffuse_solar.npy"]),calculation[:,7],allow_pickle=True, fix_imports=False)
        
        np.save("".join([partial_name, "Esol_30.npy"]),Esol_30,allow_pickle=True, fix_imports=False)
        np.save("".join([partial_name, "Esol_45.npy"]),Esol_45,allow_pickle=True, fix_imports=False)
        np.save("".join([partial_name, "Esol_60.npy"]),Esol_60,allow_pickle=True, fix_imports=False)
        np.save("".join([partial_name, "Esol_90.npy"]),Esol_90,allow_pickle=True, fix_imports=False)
        
        np.save("".join([partial_name, "SRF_overhang.npy"]),SRF_overhang,allow_pickle=True, fix_imports=False)
        np.save("".join([partial_name, "SRF_fin.npy"]),SRF_fin,allow_pickle=True, fix_imports=False)
        np.save("".join([partial_name, "SRF_horizon.npy"]),SRF_horizon,allow_pickle=True, fix_imports=False) 

        return hourly_output, Esol_30, Esol_45, Esol_60, Esol_90, SRF_overhang, SRF_fin, SRF_horizon


if __name__ == '__main__':
    print("Please execute 'ControlAgent.py'")   


