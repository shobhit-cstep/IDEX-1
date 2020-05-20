import sys

from LSTM import LSTMModel
from utils import plot_fig, print_observation_against_actual
from Dataset import Dataset

item_code = str(sys.argv[1])
forecast_parameter = sys.argv[2]

train_end_year = 2015

dataset = Dataset()
df_train, df_test = dataset.equipment_train_test_split(item_code, train_end_year)
x_train, y_train, time_train, x_test, y_test, time_test = dataset.windowed_sequences(item_code)

lstm_model = LSTMModel()
lstm_model.build()
lstm_model.fit(x_train, y_train)
lstm_forecast, lstm_error_rmse = lstm_model.forecast(x_test, y_test)

print_observation_against_actual(y_test, lstm_forecast)

desc = "LSTM_" + str(item_code) + "_" + str(train_end_year) + "_onwards"
plot_fig(desc, time_test, [y_test, lstm_forecast])
print("Error", lstm_error_rmse)