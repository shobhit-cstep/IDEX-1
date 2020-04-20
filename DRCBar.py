import sys

from Dataset import Dataset
equipment_id = int(sys.argv[1])
forecast_parameter = sys.argv[2]
location_name = sys.argv[3]
start_year = int(sys.argv[4])
end_year = int(sys.argv[5])

equipment_data_file = 'MO_'+location_name+'_Equipment_Data.csv'
consumption_data_file = 'MO_'+location_name+'_Consumption_Data.csv'

dataset = Dataset(equipment_data_file, consumption_data_file)
df_bar_plot = dataset.equipment_year_split(equipment_id,start_year,end_year)
fig = df_bar_plot.plot(kind='bar', x='Year', figsize=(15, 7)).get_figure()
fig.savefig('DRC_eq_{}_{}_{}.png'.format(equipment_id, start_year, end_year))
