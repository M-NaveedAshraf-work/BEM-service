import pandas as pd
import numpy as np
from datetime import datetime
import json

def combine(file1, file2):
    today = str(datetime.now())

    # ofile = pd.read_excel("./Input/BEM_Optimization_Input_v2_park_center_2019.xlsx", sheet_name="Calibration_Hourly_Data")
    ofile = pd.read_excel("./Input/" + file1,
                          sheet_name="Calibration_Hourly_Data")
    ofile = ofile.iloc[1:]
    ofile['Time'] = [i.round(freq="h") for i in ofile['Time']]
    ofile = ofile.fillna(0)

    # nfile = pd.read_excel("./Input/BEM_Optimization_Input_v2_park_center_2019.xlsx", sheet_name="Calibration_Hourly_Data")
    nfile = pd.read_excel("./Input/" + file2,
                          sheet_name="Calibration_Hourly_Data")
    nfile = nfile.iloc[1:]
    nfile['Time'] = [i.round(freq="h") for i in nfile['Time']]
    nfile = nfile.fillna(0)

    ofile['Day'] = [i.to_pydatetime().date().day for i in ofile['Time']]
    ofile['Month'] = [i.to_pydatetime().date().month for i in ofile['Time']]
    ofile['Hour'] = [i.to_pydatetime().time().hour for i in ofile['Time']]

    nfile['Day'] = [i.to_pydatetime().date().day for i in nfile['Time']]
    nfile['Month'] = [i.to_pydatetime().date().month for i in nfile['Time']]
    nfile['Hour'] = [i.to_pydatetime().time().hour for i in nfile['Time']]

    omonth = (ofile.groupby(['Month'], sort=False).sum()).reset_index()
    nmonth = (nfile.groupby(['Month'], sort=False).sum()).reset_index()

    odaily = ofile.groupby(['Month','Day'],sort=False).sum().reset_index()
    ndaily = nfile.groupby(['Month','Day'],sort=False).sum().reset_index()

    # Input Month Day Hour

    temp = ofile.loc[ofile["Month"] == int(today[5:7])]
    temp = temp.loc[ofile["Day"] == int(today[8:10])]
    temp = temp.loc[ofile["Hour"] == int(today[11:13])]

    ofile = ofile.iloc[temp.index.values[0]:]
    nfile = nfile.iloc[: temp.index.values[0]]
    mfile = pd.concat([nfile,ofile])
    mfile = mfile[['Time','Timestep','Electricity','Natural Gas']]
    mfile['Tempo'] = temp.index.values[0]
    # mfile['Time'] = mfile['Time'].astype(str)

    y = odaily.loc[odaily['Month'] > temp['Month'].values[0]]
    x = odaily.loc[odaily['Month'] == temp['Month'].values[0]]
    x = x.loc[x['Day'] > temp['Day'].values[0]]
    odaily = pd.concat([x,y])

    y = ndaily.loc[ndaily['Month'] < temp['Month'].values[0]]
    x = ndaily.loc[ndaily['Month'] == temp['Month'].values[0]]
    x = x.loc[x['Day'] <= temp['Day'].values[0]]
    ndaily = pd.concat([y,x])

    mdaily = pd.concat([ndaily,odaily])

    tm = mdaily.loc[mdaily['Month'] == temp['Month'].values[0]]
    tm = tm.loc[tm['Day'] == temp['Day'].values[0]]
    mdaily = mdaily[['Electricity','Natural Gas']]
    mdaily['Date'] = tm.index.values[0]

    omonth = omonth.loc[omonth['Month'] > temp["Month"].values[0]]
    nmonth = nmonth.loc[nmonth['Month'] <= temp["Month"].values[0]]
    mmonth = pd.concat([nmonth,omonth])
    mmonth = mmonth.rename(columns={"Month":"Time"})
    mmonth = mmonth[['Time','Electricity','Natural Gas']]
    mmonth['Month'] = temp['Month'].values[0]

    # result = mfile.to_json(orient="index",date_format='iso')
    # parsed = json.loads(result)
    # with open("hourly_data.json", 'w', encoding='utf-8') as f:
    #     json.dump(parsed, f, ensure_ascii=False, indent=1)
    #
    # result = mmonth.to_json(orient="index",date_format='iso')
    # parsed = json.loads(result)
    # with open("monthly_data.json", 'w', encoding='utf-8') as f:
    #     json.dump(parsed, f, ensure_ascii=False, indent=1)
    #
    # result = mdaily.to_json(orient="index",date_format='iso')
    # parsed = json.loads(result)
    # with open("daily_data.json", 'w', encoding='utf-8') as f:
    #     json.dump(parsed, f, ensure_ascii=False, indent=1)

    combo_data = {}
    combo_data["hourly"] = mfile.to_dict("index")
    combo_data["daily"] = mdaily.to_dict("index")
    combo_data["monthly"] = mmonth.to_dict("index")

    month = temp['Month'].values[0]
    day = tm.index.values[0]
    hour = temp.index.values[0]

    return combo_data, month, day, hour

if __name__ == '__main__':
    data, m_index, d_index, h_index = combine("BEM_Optimization_Input_v2_centergy_BEM_2019.xlsx", "BEM_Optimization_Input_v2_centergy_BEM_2019.xlsx")
    data_sheet = data['hourly']
    monthly = data['monthly']
    daily = data['daily']
    hourlyData = np.zeros((8760, 2))
    print(daily)

    for i in range(1, 8760):
        hourlyData[i, 0] = data_sheet[i]["Electricity"]
        hourlyData[i, 1] = data_sheet[i]["Natural Gas"]
