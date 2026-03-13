import numpy as np


def load_dataset(file_path):

    try:
        data = np.genfromtxt(
            file_path,
            delimiter=",",
            skip_header=1
        )

        return data

    except Exception as e:

        print("Error loading dataset:", e)
        return None