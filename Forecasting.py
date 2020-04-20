import sys

from Arima import ArimaModel
from Dataset import Dataset
equipment_id = int(sys.argv[1])
forecast_parameter = sys.argv[2]
location_name = sys.argv[3]

train_end_year = 2015

equipment_data_file = 'MO_'+location_name+'_Equipment_Data.csv'
consumption_data_file = 'MO_'+location_name+'_Consumption_Data.csv'

dataset = Dataset(equipment_data_file, consumption_data_file)
df_train,df_test = dataset.equipment_train_test_split(equipment_id, train_end_year)

arima_model = ArimaModel(5, 1, 0)
RPQ_arima, error_arima = arima_model.forecast(df_train,df_test, forecast_parameter)

for yhat, obs in zip(df_test[forecast_parameter].reset_index(drop=True), RPQ_arima):
    print('predicted=%f, expected=%f' % (yhat, obs))

print(error_arima)