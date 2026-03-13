import numpy as np

def analyze_dataset(data):

    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    minimum = np.min(data, axis=0)
    maximum = np.max(data, axis=0)

    return mean, std, minimum, maximum