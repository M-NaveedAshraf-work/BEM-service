import pandas as pd
import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import percentileofscore

class Energystar():

    def score(self, non_gfa,data_gfa, office_gfa, wkhrs,workers,cpus,pctcooled,cdd,hdd, site_eui = None, source_eui = None, site = None, source = None):
"""A function that finds the energy star score for buildings that use Electricity as their sole energy source
    Inputs:
        - non_gfa: non-scoreable gross floor area (GFA)
        - data_gfa: data center GFA
        - office_gfa: scorable GFA
        - whrs: weekly operating hours
        - workers: number of workers on main shift
        - cpus: number of computers
        - pctcooled: percent of the building that can be cooled (if >50% then it defaults as 1)
        - cdd: cooling degree days
        - hdd: heating degree days
        - site_eui: EUI of site
        - source_eui: EUI of source
        - site: energy consumption of site in kBTU
        - source: energy consumption of source in kBTU
    Outputs:
        - score: Energy star score
        - predict_eui: predicted source EUI
        - adjusted_eui: adjusted score eui"""
        if site:
            source = site * 2.8
        if source_eui:
            source = source_eui * (non_gfa + data_gfa + office_gfa)
        elif site_eui:
            source = site_eui * 2.8 * (non_gfa + data_gfa + office_gfa)
        centered = [12342, 54.09, 2.056, 3.028, 6.332, 924]
        coeff = [0.0006768,0.6130, 15.90, 10.13, 4.529, 0.004693]
        workers = workers / office_gfa * 1000
        cpus = cpus / office_gfa *1000
        pctcooled = pctcooled / 100
        if office_gfa > 100000:
            adj_office_gfa = 100000
        if hdd >= 924:
            predict_eui = (adj_office_gfa - centered[0])*coeff[0] + (wkhrs - centered[1])* coeff[1] + (workers - centered[2]) * coeff[2] + (cpus - centered[3])*coeff[3] + ((pctcooled * np.log(cdd) - centered[4]))*coeff[4] + (hdd - centered[5])*coeff[5] + 143.1
        else:
            predict_eui = (afj_office_gfa - centered[0])*coeff[0] + (wkhrs - centered[1])* coeff[1] + (workers - centered[2]) * coeff[2] + (cpus - centered[3])*coeff[3] + ((pctcooled * np.log(cdd) - centered[4]))*coeff[4] + 143.1
        if data_gfa != 0:
            data_est = data_gfa * 2000
            adjusted_source = source - data_est
        else:
            adjusted_source = source
        adjusted_eui = adjusted_source / (non_gfa + data_gfa + office_gfa)
        ratio = adjusted_eui / predict_eui
        df = pd.read_csv('estarscore.csv')
        score = df[(ratio >= df['Min_ratio']) & (df['Max_ratio'] >= ratio)]['Score'].values[0]
        return score, predict_eui, adjusted_eui
    def target_score(self,target,current_eui,predicted_eui, area, unit = 'kWh'):
"""A function that outputs the kwh in savings needed to for a certain target energy star score
    Inputs:
        - target: target energy star score
        - current_eui: Current source EUI
        - predicted_eui: predicted source EUI (output from score function)
        - area: scorable GFA
        - unit: converts units from kBTU to kWh
    Outputs:
        - usage: energy that needs to be saved to reach target score
        - target_eui: target source EUI needed to reach target score"""
        df = pd.read_csv('estarscore.csv')
        target_eui = max(df[df.Score == target].to_numpy()[0][1:3] * predicted_eui)
        usage = (current_eui - target_eui) * area / 2.8
        if unit == 'kWh' or unit == 'kwh':
            usage /= 3.4121416331
        return usage, target_eui
    def benchmark(self,current_eui, min_sqft, max_sqft, year = None):
"""A function that plots a distribution graph of source EUIs and plots a red line
    of the source EUI of the building in question
    Inputs:
        - current_eui: current source EUI of building
        - min_sqft: the minimum sqft each building in the benchmark data needs to be over
        - max_sqft: the max sqft that the benchmark data needs to be lower than
        - year: the minimum year that the buildings in the database have to be built
    Output:
        - a json file of the source EUI of the benchmark data
"""
        df = pd.read_csv('2012_public_use_data_aug2016.csv')
        test = df.loc[(df.SQFTC >= min_sqft) & (df.SQFTC <= max_sqft)& (df.PBA == 2)]
        if year:
            test.loc[test.YRCON >= year]
        sqft = test.SQFT * test.FINALWT
        elec = test.ELBTU * test.FINALWT
        eui = elec / sqft
        plt.figure(figsize = (12,8))
        sns.set_style("dark")
        sns.distplot(eui, bins = 100)
        plt.axvline(current_eui, 0,.85, color = 'r', label = f'Your building = {current_eui} $kBtu/ft^{2}$')
        plt.xlabel('Site EUI', fontsize = 'x-large')
        plt.ylabel('Frequency',fontsize = 'x-large')
        plt.title('')
        plt.legend(loc='upper center', bbox_to_anchor=(0.4, .8), fontsize = 'x-large')
        plt.show()
        data = {'EUI values': list(eui.values) }
        with open('benchmark_data.json', 'w') as f:
            json.dump(data, f)
        return data
