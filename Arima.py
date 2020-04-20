from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt


class ArimaModel(object):
    def __init__(self, p=5, d=1, q=0):
        self.p = p
        self.d = d
        self.q = q

    def forecast(self, df_train, df_test, forecast_parameter):
        train = df_train[forecast_parameter].reset_index(drop=True)
        test = df_test[forecast_parameter].reset_index(drop=True)
        history = [x for x in train]
        predictions = list()
        for t in range(len(test)):
            model = ARIMA(history, order=(self.p, self.d, self.q))
            model_fit = model.fit(disp=0)
            output = model_fit.forecast()
            yhat = output[0]
            predictions.append(yhat)
            obs = test[t]
            history.append(obs)
        error = sqrt(mean_squared_error(test, predictions))
        return predictions, error
