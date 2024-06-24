import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class MachineLearningModel:
    def __init__(self, input_shape: tuple, output_shape: tuple):
        self.model = Sequential()
        self.model.add(Dense(64, activation='relu', input_shape=input_shape))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(output_shape[1], activation='softmax'))
        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    def train(self, X_train: np.ndarray, y_train: np.ndarray, epochs: int = 10):
        self.model.fit(X_train, y_train, epochs=epochs)

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        return self.model.predict(X_test)

    def evaluate(self, X_test: np.ndarray, y_test: np.ndarray) -> float:
        return self.model.evaluate(X_test, y_test)

# Example usage:
# model = MachineLearningModel((10,), (2,))
# X_train = np.random.rand(100, 10)
# y_train = np.random.rand(100, 2)
# model.train(X_train, y_train)
