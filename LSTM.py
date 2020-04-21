from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from sklearn.metrics import mean_squared_error


class LSTMModel(object):
    def __init__(self,):
        self.model = None

    def build(self, layer1_parameters=50, layer2_parameters=50, input_shape_n_steps=3, input_shape_n_features=1, loss='mse', metrics='mae'):
        # define model
        self.model = Sequential()
        self.model.add(LSTM(layer1_parameters, activation='relu', return_sequences=True, input_shape=(input_shape_n_steps, input_shape_n_features)))
        self.model.add(LSTM(layer2_parameters, activation='relu'))
        self.model.add(Dense(1))
        self.model.compile(optimizer='adam', loss=loss, metrics=[metrics])

    def fit(self, x_train, y_train, epochs=200, verbose=1):
        # fit model
        self.model.fit(x_train, y_train, epochs=epochs, verbose=verbose)

    def forecast(self, x_test, y_test, verbose=0):
        y_hat = self.model.predict(x_test, verbose=verbose)
        mse_error = mean_squared_error(y_test, y_hat, squared=False)
        return y_hat, mse_error




