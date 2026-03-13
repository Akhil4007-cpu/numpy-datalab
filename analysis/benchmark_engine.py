import numpy as np
import time

def benchmark_vectorization():

    size = 1000000

    # Python list
    python_list = list(range(size))

    # NumPy array
    numpy_array = np.array(python_list)

    # Python loop timing
    start = time.time()

    squared_python = [x**2 for x in python_list]

    python_time = time.time() - start

    # NumPy vectorized timing
    start = time.time()

    squared_numpy = numpy_array ** 2

    numpy_time = time.time() - start

    return python_time, numpy_time