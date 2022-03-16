#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:23:21 2021

@author: kiarashahmadi
"""
from epw import epw
import pandas as pd
def weather_conversion(filename,output):

    a = epw()
    a.read('weather_files/testing.epw')
    df = a.dataframe  # this is pandas dataframe
    filepath = 'weather_files/'
    file = filepath + filename
    if "NREL" in filename:
        new = pd.read_csv(file, skiprows = 2)
        new = new.loc[:, ~new.columns.str.contains('^Unnamed')]
        df['Year'] = new['Year']
        df['Month'] = new['Month']
        df['Day'] = new['Day']
        df['Minute'] = new['Minute']
        df['Dry Bulb Temperature'] = new['Temperature']
        df['Dew Point Temperature'] = new['Dew Point']
        df['Wind Speed'] = new['Wind Speed']
        df['Relative Humidity'] = new['Relative Humidity']
        df['Global Horizontal Radiation'] = new['GHI']
        df['Direct Normal Radiation'] = new['DNI']
        df['Diffuse Horizontal Radiation'] = new['DHI']
        df['Atmospheric Station Pressure'] = new['Pressure'] * 100
    
    elif "solcast" in filename:
        new = pd.read_csv(file)
        df['Year'] = (new.PeriodStart.str[0:4]).astype(int)
        df['Month'] = (new.PeriodStart.str[5:7]).astype(int)
        df['Day'] = (new.PeriodStart.str[8:10]).astype(int)
        df['Minute'] = (new.PeriodStart.str[-3:-1]).astype(int)
        df['Dry Bulb Temperature'] = new['AirTemp']
        df['Dew Point Temperature'] = new['WindSpeed10m']
        df['Wind Speed'] = new['DewpointTemp']
        df['Relative Humidity'] = new['RelativeHumidity']
        df['Global Horizontal Radiation'] = new['Ghi']
        df['Direct Normal Radiation'] = new['Dni']
        df['Direct Horizontal Radiation'] = new['Dhi']
        df['Atmospheric Station Pressure'] = new['SurfacePressure'] * 100
    name =  output + '_epw_file.epw'
    a.write(name)
    
if __name__ == '__main__':
        
    weather_conversion('NREL_2019_Centergy.csv','centergy_2019')