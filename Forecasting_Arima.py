import sys

from Arima import ArimaModel
from Dataset import Dataset
from utils import plot_fig, print_observation_against_actual

equipment_id = int(sys.argv[1])
forecast_parameter = sys.argv[2]
location_name = sys.argv[3]

train_end_year = 2015

dataset = Dataset(location_name)
df_train, df_test = dataset.equipment_train_test_split(equipment_id, train_end_year)

arima_model = ArimaModel(5, 1, 0)
arima_forecast, arima_error_rmse = arima_model.forecast(df_train, df_test, forecast_parameter)

print_observation_against_actual(df_test[forecast_parameter].reset_index(drop=True), arima_forecast)

desc = "arima_"+location_name+"_"+str(equipment_id)+"_"+str(train_end_year)+"_onwards"
plot_fig(desc, df_test['Year'].reset_index(drop=True), [df_test[forecast_parameter].reset_index(drop=True), arima_forecast])

print("Error", arima_error_rmse)
