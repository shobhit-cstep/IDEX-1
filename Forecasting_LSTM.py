import sys

from LSTM import LSTMModel
from utils import plot_fig, print_observation_against_actual
from Dataset import Dataset

equipment_id = int(sys.argv[1])
forecast_parameter = sys.argv[2]
location_name = sys.argv[3]

train_end_year = 2015

dataset = Dataset(location_name)
df_train, df_test = dataset.equipment_train_test_split(equipment_id, train_end_year)
x_train, y_train, time_train, x_test, y_test, time_test = dataset.windowed_sequences(equipment_id)

lstm_model = LSTMModel()
lstm_model.build()
lstm_model.fit(x_train, y_train)
lstm_forecast, lstm_error_rmse = lstm_model.forecast(x_test, y_test)

print_observation_against_actual(y_test, lstm_forecast)

desc = "LSTM_"+location_name+"_"+str(equipment_id)+"_"+str(train_end_year)+"_onwards"
plot_fig(desc, time_test, [y_test, lstm_forecast])
print("Error", lstm_error_rmse)