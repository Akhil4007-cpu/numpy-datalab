
import numpy as np

def normalize_dataset(data):

    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)

    normalized = (data - mean) / std

    return normalized