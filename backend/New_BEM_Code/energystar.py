import pandas as pd
import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import percentileofscore

class Energystar():

    def __init__(self, non_gfa,data_gfa, office_gfa, wkhrs,workers,cpus,pctcooled,cdd,hdd, site_eui, source_eui, site, source, target, predicted_eui, area, unit, current_eui, min_sqft, max_sqft, year):
        self.non_gfa = float(non_gfa)
        self.data_gfa = float(data_gfa)
        self.office_gfa = float(office_gfa)
        self.wkhrs = int(wkhrs)
        self.workers = int(workers)
        self.cpus = int(cpus)
        self.pctcooled = float(pctcooled)
        self.cdd = int(cdd)
        self.hdd = int(hdd)
        self.site_eui = float(site_eui)
        self.source_eui = float(source_eui)
        self.site = int(site)
        self.source = int(source)
        self.target = int(target)
        self.current_eui = float(current_eui)
        self.predicted_eui = float(predicted_eui)
        self.area = float(area)
        self.unit = unit
        self.min_sqft = float(min_sqft)
        self.max_sqft = float(max_sqft)
        self.year = int(year)

    def score(self):
        # A function that finds the energy star score for buildings that use Electricity as their sole energy source
        #     Inputs:
        #     - non_gfa: non-scoreable gross floor area (GFA)
        #     - data_gfa: data center GFA
        #     - office_gfa: scorable GFA
        #     - whrs: weekly operating hours
        #     - workers: number of workers on main shift
        #     - cpus: number of computers
        #     - pctcooled: percent of the building that can be cooled (if >50% then it defaults as 1)
        #     - cdd: cooling degree days
        #     - hdd: heating degree days
        #     - site_eui: EUI of site
        #     - source_eui: EUI of source
        #     - site: energy consumption of site in kBTU
        #     - source: energy consumption of source in kBTU
        # Outputs:
        #     - score: Energy star score
        #     - predict_eui: predicted source EUI
        #     - adjusted_eui: adjusted score eui
        if self.site:
            self.source = self.site * 2.8
        if self.source_eui:
            self.source = self.source_eui * (self.non_gfa + self.data_gfa + self.office_gfa)
        elif self.site_eui:
            self.source = self.site_eui * 2.8 * (self.non_gfa + self.data_gfa + self.office_gfa)
        centered = [12342, 54.09, 2.056, 3.028, 6.332, 924]
        coeff = [0.0006768,0.6130, 15.90, 10.13, 4.529, 0.004693]
        self.workers = self.workers / self.office_gfa * 1000
        self.cpus = self.cpus / self.office_gfa *1000
        self.pctcooled = self.pctcooled / 100
        if self.office_gfa > 100000:
            self.adj_office_gfa = 100000
        else:
            self.adj_office_gfa = self.office_gfa
        if self.hdd >= 924:
            self.predict_eui = (self.adj_office_gfa - centered[0])*coeff[0] + (self.wkhrs - centered[1])* coeff[1] + (self.workers - centered[2]) * coeff[2] + (self.cpus - centered[3])*coeff[3] + ((self.pctcooled * np.log(self.cdd) - centered[4]))*coeff[4] + (self.hdd - centered[5])*coeff[5] + 143.1
        else:
            self.predict_eui = (self.adj_office_gfa - centered[0])*coeff[0] + (self.wkhrs - centered[1])* coeff[1] + (self.workers - centered[2]) * coeff[2] + (self.cpus - centered[3])*coeff[3] + ((self.pctcooled * np.log(self.cdd) - centered[4]))*coeff[4] + 143.1
        if self.data_gfa != 0:
            self.data_est = self.data_gfa * 2000
            self.adjusted_source = self.source - self.data_est
        else:
            self.adjusted_source = self.source
        self.adjusted_eui = self.adjusted_source / (self.non_gfa + self.data_gfa + self.office_gfa)
        ratio = self.adjusted_eui / self.predict_eui
        df = pd.read_csv('estarscore.csv')
        self.score = df[(ratio >= df['Min_ratio']) & (df['Max_ratio'] >= ratio)]['Score'].values[0]
        return self.score, self.predict_eui, self.adjusted_eui
    def target_score(self):
# """A function that outputs the kwh in savings needed to for a certain target energy star score
#     Inputs:
#         - target: target energy star score
#         - current_eui: Current source EUI
#         - predicted_eui: predicted source EUI (output from score function)
#         - area: scorable GFA
#         - unit: converts units from kBTU to kWh
#     Outputs:
#         - usage: energy that needs to be saved to reach target score
#         - target_eui: target source EUI needed to reach target score"""
        df = pd.read_csv('estarscore.csv')
        self.target_eui = max(df[df.Score == self.target].to_numpy()[0][1:3] * self.predicted_eui)
        self.usage = (self.current_eui - self.target_eui) * self.area / 2.8
        if self.unit == 'kWh' or self.unit == 'kwh':
            self.usage /= 3.4121416331
        return self.usage, self.target_eui

    def benchmark(self):
# """A function that plots a distribution graph of source EUIs and plots a red line
#     of the source EUI of the building in question
#     Inputs:
#         - current_eui: current source EUI of building
#         - min_sqft: the minimum sqft each building in the benchmark data needs to be over
#         - max_sqft: the max sqft that the benchmark data needs to be lower than
#         - year: the minimum year that the buildings in the database have to be built
#     Output:
#         - a json file of the source EUI of the benchmark data
# """
        df = pd.read_csv('2012_public_use_data_aug2016.csv')
        test = df.loc[(df.SQFT >= float(self.min_sqft)) & (df.SQFT <= float(self.max_sqft))& (df.PBA == 2)]
        if int(self.year):
            test.loc[test.YRCON >= int(self.year)]
        sqft = test.SQFT * test.FINALWT
        elec = test.ELBTU * test.FINALWT
        self.eui = elec / sqft
        # plt.figure(figsize = (12,8))
        # sns.set_style("dark")
        # sns.distplot(self.eui, bins = 100)
        # plt.axvline(self.current_eui, 0,.85, color = 'r', label = f'Your building = {self.current_eui} $kBtu/ft^{2}$')
        # plt.xlabel('Site EUI', fontsize = 'x-large')
        # plt.ylabel('Frequency',fontsize = 'x-large')
        # plt.title('')
        # plt.legend(loc='upper center', bbox_to_anchor=(0.4, .8), fontsize = 'x-large')
        # # plt.show()
        # data = {'EUI values': list(self.eui.values) }
        # with open('benchmark_data.json', 'w') as f:
        #     json.dump(data, f)
        # TODO: Fix

        build_index = []
        for i in range((len(self.eui.values))):
            update_data = i
            build_index.append(update_data)

        data_mid = pd.DataFrame(self.eui.values, columns=['Delivered'])
        data = data_mid.Delivered.values.tolist()
        # data = self.eui.values[0]
        return data, build_index

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

def runEnergystar(non_gfa,data_gfa, office_gfa, wkhrs,workers,cpus,pctcooled,cdd,hdd, site_eui, source_eui, site, source, target, predicted_eui, area, unit, current_eui, min_sqft, max_sqft, year):
    instance = Energystar(non_gfa,data_gfa, office_gfa, wkhrs,workers,cpus,pctcooled,cdd,hdd, site_eui, source_eui, site, source, target, predicted_eui, area, unit, current_eui, min_sqft, max_sqft, year)
    score, predict_eui, adjusted_eui = instance.score()
    usage, target_eui = instance.target_score()
    benchmark, build_index = instance.benchmark()

    A = []
    for i in range(len(benchmark)):
        A.append([])
        A[i].append(benchmark[i])

    return float(score), float(predict_eui), float(adjusted_eui), float(usage), float(target_eui), A, build_index

if __name__ == '__main__':
    print("Please execute the 'main.py' script.")