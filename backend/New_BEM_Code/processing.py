from main import main
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import json
import seaborn as sns
import os

def processing(building, epw_file, min_sqft, max_sqft, year = None):
# """ This function takes in a building file and exports out the data needed in the form of a JSON file
# - Inputs:
#     - building: building file name in either csv or Json
#     - epw_file: weather file name
#     - min_sqft (category variable: check microbook):  the minimum sqft each building in the benchmark data needs to be over
#     - max_sqft (category variable: check microbook): the max sqft that the benchmark data needs to be lower than
#     - year: the minimum year that the buildings in the database have to be built
# Outputs:
#     -  benchmark_data_end_use.json: end use values of building in database
#     - delivered_data.json: kWh results of model by month
#     - need_data: cooling and heating need
#     - end_use.json: end use data of specific building in question"""
    delivered_energy, sum_delivered_energy, fuel_energy_use, overall, area = main(building_name = building, epw_file_name=epw_file)

    ##To group the data by month

    df = pd.DataFrame(delivered_energy,columns = ['heating energy',
                                             'cooling', 'light', 'fan',
                                             'pump','equipment', 'DHW',
                                             'PV', 'wind', 'Etotal'])
    df2 = pd.DataFrame(overall, columns = ['Heating Need','Cooling Need','Cooling Need after Natural Cooling'])
    df3 = df2.copy()
    df3.iloc[:,1:3] = df2.iloc[:,1:3]* -1
    data = pd.concat([df,df3], axis = 1)
    data['Month'] = 'blank'
    data.loc[:743,'Month'] = 'January'
    data.loc[744:1415, 'Month'] = 'February'
    data.loc[1416:2159, 'Month'] = 'March'
    data.loc[2160:2879, 'Month'] = 'April'
    data.loc[2880:3623, 'Month'] = 'May'
    data.loc[3624:4343, 'Month'] = 'June'
    data.loc[4344:5087, 'Month'] = 'July'
    data.loc[5088:5831, 'Month'] = 'August'
    data.loc[5832:6551, 'Month'] = 'Septemeber'
    data.loc[6552:7295, 'Month'] = 'October'
    data.loc[7296:8015, 'Month'] = 'November'
    data.loc[8016:8759, 'Month'] = 'December'
    grouped = data.groupby(['Month'],sort = False).sum()
    delivered = grouped.iloc[:,:10]
    need = grouped.iloc[:,10:13]

    # to create the heating and cooling need bar plot and end-use pie chart
    ax = delivered.plot.bar(y = 'Etotal')
    ax.set_xlabel("Month")
    ax.set_ylabel("Energy Consumption")
    # groups data by end-use values that are non-zero
    pie_data = np.array(delivered.iloc[:,:-1].sum())
    pie_names = ['Heating', 'Cooling', 'Lighting', 'Fans','Pumps','Plug Load', 'DHW','PV', 'Wind']
    data = [x for x in pie_data if x != 0]
    where = np.where(pie_data == 0)
    where = where[0].tolist()
    new_arr = np.delete(pie_names, where)
    fig = plt.figure(figsize =(12, 8))
    plt.pie(data, labels = new_arr, autopct='%1.1f%%')
    plt.tight_layout()

    ax2 = need.plot.bar(y = ['Heating Need','Cooling Need','Cooling Need after Natural Cooling'])
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Need")

    # creates the kWh consumption data
    consumption = delivered.loc[:,'Etotal'] / 1000 * area
    delivered.loc['Total',:]= delivered.sum(axis=0)
    need.loc['Total',:]= need.sum(axis=0)

    # creates eui and end-use of building to then benchmark it
    conversion = 3.4121416331/10.76391
    eui = delivered.loc['Total', 'Etotal'] / 1000 * conversion
    end_use = {}
    for name, value in zip(new_arr, data):
        print(value)
        end_use[name] = value / 1000 * conversion
    df2 = pd.read_csv('2012_public_use_data_aug2016.csv')
    print(df2)

    offices = df2[df2.PBA == 2]
    benchmark = offices.loc[(offices.SQFTC >= min_sqft) & (offices.SQFTC <= max_sqft)& (offices.PBA == 2) & offices.NGUSED == 2]
    if year:
        benchmark.loc[benchmark.YRCON >= year]
    benchmark = benchmark.loc[:,['SQFT','FINALWT','ELHTBTU','ELCLBTU','ELVNBTU','ELWTBTU','ELLTBTU','ELCKBTU','ELRFBTU','ELOFBTU','ELPCBTU','ELOTBTU']]
    benchmark['Heating'] = benchmark['ELHTBTU'] / benchmark['SQFT']
    benchmark['Cooling'] = benchmark['ELCLBTU'] / benchmark['SQFT']
    benchmark['Lighting'] = benchmark['ELLTBTU'] / benchmark['SQFT']
    benchmark['Plug Load'] = benchmark['ELOFBTU'] / benchmark['SQFT'] + benchmark['ELPCBTU'] / benchmark['SQFT']
    benchmark['Fans'] = benchmark['ELVNBTU'] / benchmark['SQFT']
    benchmark['DHW'] = benchmark['ELWTBTU'] / benchmark['SQFT']

    benchmark = benchmark.loc[:,['Heating','Cooling','Lighting','Fans','DHW','Plug Load']]
    bench_data = {}

    # benchmark data for end use
    for name in benchmark.columns:
        bench_data[name] = list(benchmark[name].values)

    #creates the json file
#    for name in ['Heating','Cooling','Lighting','Fans','DHW','Plug Load']:
#        plt.figure(figsize = (12,8))
#        sns.set_style("dark")
#        sns.distplot(benchmark[name], bins = 25)
#        label = f'Your building = {round(end_use[name],2)} $kBtu/ft^{2}$'
#        plt.axvline(end_use[name], 0,.85, color = 'r', label = label)
#        plt.xlabel('Energy Intensity of {}'.format(name), fontsize = 'xx-large')
#        plt.ylabel('Frequency',fontsize = 'xx-large')
#        plt.legend(loc='upper center', fontsize = 'xx-large')
#        plt.savefig(f'park_center{name}.jpg', bbox = 'Tight')
#        plt.show()

    os.chdir('output/')
    with open('benchmark_data_end_use.json', 'w') as z:
        json.dump(bench_data, z)
    result = consumption.to_json(orient="index")
    parsed = json.loads(result)
    with open('delivered_data.json', 'w') as f:
        json.dump(parsed, f)
    result2 = need.to_json(orient="index")
    parsed2 = json.loads(result2)
    with open('need_data.json', 'w') as d:
        json.dump(parsed2, d)
    with open('end_use.json', 'w') as g:
        json.dump(end_use, g)
    os.chdir('../')
    return eui, end_use, consumption, benchmark

if __name__ == '__main__':

    # Execute the code
    eui, end_use, consumption, benchmark = processing("park_center_2019.csv", "park_center_2019_epw_file.epw")
