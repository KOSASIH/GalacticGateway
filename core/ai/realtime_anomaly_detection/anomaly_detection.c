// anomaly_detection.c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define THRESHOLD 3.0

void detect_anomalies(double* data, int size) {
    double mean = 0.0;
    double stddev = 0.0;

    // Calculate mean and standard deviation
    for (int i = 0; i < size; i++) {
        mean += data[i];
    }
    mean /= size;
    for (int i = 0; i < size; i++) {
        stddev += pow(data[i] - mean, 2);
    }
    stddev = sqrt(stddev / size);

    // Identify anomalies
    for (int i = 0; i < size; i++) {
        if (fabs(data[i] - mean) > THRESHOLD * stddev) {
            printf("Anomaly detected at index %d: %f\n", i, data[i]);
        }
    }
}
