## IDEX RPQ Prediction Project
#### How to run 
##### For Forecasting
Run the Forecasting.py using the below command
###### LSTM Forecast 
`python Forecasting_LSTM.py <item_code> <forecast_paramenter>`

Sample command

`python Forecasting_LSTM.py Item_1 Consumption`

###### ARIMA Forecast
Run the Forecasting.py using the below command

`python Forecasting_Arima.py <item_code> <forecast_paramenter>`

Sample command

`python Forecasting_Arima.py Item_2 Consumption`

##### For Barplot
Run the Visualize.py file using the below command

`python Visualize.py <item_code> <forecast_paramenter> <start_year> <end_year>`

Sample command

`python Visualize.py Item_18 Consumption 2010 2019`