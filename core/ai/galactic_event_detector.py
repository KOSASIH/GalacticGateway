import numpy as np
from sklearn.svm import OneClassSVM

class GalacticEventDetector:
    def __init__(self, data_stream, anomaly_threshold):
        self.data_stream = data_stream
        self.anomaly_threshold = anomaly_threshold
        self.ocsvm = OneClassSVM(kernel='rbf', gamma=0.1, nu=0.1)

    def detect_anomalies(self):
        anomalies = []
        for data_point in self.data_stream:
            prediction = self.ocsvm.predict(data_point.reshape(1, -1))
            if prediction == -1:
                anomalies.append(data_point)
        return anomalies
