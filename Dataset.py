import pandas as pd
from utils import split_sequence


class Dataset(object):
    def __init__(self, df):
        self.df = pd.read_csv(df)

    def equipment_train_test_split(self, equipment_id, train_end_year):
        df_equipment_id = self.df[self.df['Equipment ID'] == equipment_id][['Year', 'Demand']].reset_index(drop=True)
        df_train = df_equipment_id[df_equipment_id['Year'] < train_end_year]
        df_test = df_equipment_id[df_equipment_id['Year'] >= train_end_year]
        return df_train, df_test

    def equipment_year_split(self, equipment_id, start_year, end_year):
        df_bar_plot = self.df[(self.df['Year'] >= start_year) & (self.df['Year'] <= end_year) & (self.df['Equipment ID'] == equipment_id)].reset_index(drop=True)
        df_bar_plot = df_bar_plot[['Year', 'Demand', 'RPQ', 'Consumption']]
        return df_bar_plot

    def windowed_sequences(self, equipment_id, forecasting_parameter="Demand", time_parameter="Year", n_steps=3, split_index=25, n_features=1):
        raw_seq = self.df[self.df['Equipment ID'] == equipment_id][forecasting_parameter].to_numpy()
        raw_time = self.df[self.df['Equipment ID'] == equipment_id][time_parameter].to_numpy()
        train_seq = raw_seq[:split_index]
        test_seq = raw_seq[split_index - n_steps:]
        x_train, y_train = split_sequence(train_seq, n_steps)
        x_test, y_test = split_sequence(test_seq, n_steps)
        x_train = x_train.reshape((x_train.shape[0], x_train.shape[1], n_features))
        x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], n_features))
        time_train = raw_time[:split_index]
        time_test = raw_time[split_index:]

        return x_train, y_train, time_train, x_test, y_test, time_test
