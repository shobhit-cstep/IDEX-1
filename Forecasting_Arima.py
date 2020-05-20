import sys

from Arima import ArimaModel
from Dataset import Dataset
from utils import plot_fig, print_observation_against_actual

item_code = str(sys.argv[1])
forecast_parameter = sys.argv[2]

train_end_year = 2015

dataset = Dataset()
df_train, df_test = dataset.equipment_train_test_split(item_code, train_end_year)

arima_model = ArimaModel(5, 1, 0)
arima_forecast, arima_error_rmse = arima_model.forecast(df_train, df_test, forecast_parameter)

print_observation_against_actual(df_test[forecast_parameter].reset_index(drop=True), arima_forecast)

desc = "Arima_" + str(item_code) + "_" + str(train_end_year) + "_onwards"
plot_fig(desc, df_test['Year'].reset_index(drop=True), [df_test[forecast_parameter].reset_index(drop=True), arima_forecast])

print("Error", arima_error_rmse)
