import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.optimize import minimize
import pygad
import xgboost as xgb

def objective(x_0,df):
    x = np.array(df.CDD*x_0[0] + df.HDD*x_0[1])
    x = x.reshape((-1,1))
    y = np.array(df["Y_adj"])
    y = y.reshape((-1,1))
    model = LinearRegression()
#     model = xgb.XGBRegressor(random_state = 4)
#     xgb_base.fit(X_train,y_train)
    model.fit(x,y)
    r_sq = model.score(x, y)
    return 1 / r_sq

def true(x_0,df):
    x = np.array(df.CDD*x_0[0] + df.HDD*x_0[1])
    x = x.reshape((-1,1))
    y = np.array(df["Y_adj"])
    y = y.reshape((-1,1))
    model = LinearRegression()

#     model = xgb.XGBRegressor(random_state = 4)
#     xgb_base.fit(X_train,y_train)
    model.fit(x,y)
#     print(model.intercept_)
#     print(model.coef_)
    r_sq = model.score(x, y)
    return r_sq, model


def predict(filename):
    df = pd.read_csv("C:/Users/Windows/Documents/BEM_Dashboard/backend/New_BEM_Code/Input/" + str(filename))
    df.dropna(axis=1, inplace=True)

    # where that month is dropped and saved for testing the result of the regression model
    test = df.iloc[0, :]
    df.drop([0], axis=0, inplace=True)

    bnds = ((0, 1), (0, 1))
    x_0 = (1, 0)
    result = minimize(lambda x_0: objective(x_0, df), (1, 0), method='trust-constr', bounds=bnds, tol=1e-10)
    r_sq, model = true(np.array([result.x[0], result.x[1]]), df)

    x_prime = test.CDD * result.x[0] + test.HDD * result.x[1]
    y_est = model.predict(np.array(x_prime).reshape(-1, 1))[0][0]
    cost_est = y_est / 30.437 * test.Days * test['$/kWh']
    error = abs(cost_est - test['$']) / test['$'] * 100
    # print(
    #     f"The estimated cost is ${round(cost_est, 2)} with a difference of ${round(abs(cost_est - test['$']))} and an error of {round(error, 2)}%")
    return round(cost_est, 2), error