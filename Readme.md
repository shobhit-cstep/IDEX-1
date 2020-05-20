## IDEX RPQ Prediction Project
#### How to run 
##### For Forecasting
Run the Forecasting.py using the below command
###### LSTM Forecast 
`python Forecasting_LSTM.py <equipment_id> <forecast_paramenter> <station_name>`

Sample command

`python Forecasting_LSTM.py 2 Demand Mumbai`

###### ARIMA Forecast
Run the Forecasting.py using the below command

`python Forecasting_Arima.py <equipment_id> <forecast_paramenter> <station_name>`

Sample command

`python Forecasting_Arima.py 2 Demand Mumbai`

##### For Barplot
Run the Visualize.py file using the below command

`python Visualize.py <equipment_id> <forecast_paramenter> <station_name> <start_year> <end_year>`

Sample command

`python Visualize.py 18 Demand Kochi 2010 2019`