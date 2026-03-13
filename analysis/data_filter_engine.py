import numpy as np

def filter_high_income(data, threshold=60000):

    # Income column index = 1
    filtered = data[data[:, 1] > threshold]

    return filtered


def filter_experienced_people(data, years=10):

    # Experience column index = 2
    filtered = data[data[:, 2] > years]

    return filtered