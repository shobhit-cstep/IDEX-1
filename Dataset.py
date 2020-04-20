import pandas as pd


class Dataset(object):
    def __init__(self, equipment_data_file, consumption_data_file):
        self.df_equipment = pd.read_csv(equipment_data_file)
        self.df_consumption = pd.read_csv(consumption_data_file)

    def equipment_train_test_split(self, equipment_id, train_end_year):
        df_equipment_id = self.df_consumption[self.df_consumption['Equipment ID'] == equipment_id][['Year', 'Demand']].reset_index(drop=True)
        df_train = df_equipment_id[df_equipment_id['Year'] < train_end_year]
        df_test = df_equipment_id[df_equipment_id['Year'] >= train_end_year]
        return df_train, df_test

    def equipment_year_split(self, equipment_id, start_year, end_year):
        df_bar_plot = self.df_consumption[(self.df_consumption['Year'] >= start_year) & (self.df_consumption['Year'] <= end_year) & (self.df_consumption['Equipment ID'] == equipment_id)].reset_index(drop=True)
        df_bar_plot = df_bar_plot[['Year', 'Demand', 'RPQ', 'Consumption']]
        return df_bar_plot
