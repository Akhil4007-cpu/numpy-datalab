from data.dataset_generator import generate_dataset
from analysis.statistics_engine import analyze_dataset
from analysis.normalization_engine import normalize_dataset
from analysis.data_filter_engine import filter_high_income, filter_experienced_people
from analysis.linear_algebra_engine import matrix_operations
from analysis.benchmark_engine import benchmark_vectorization




data = generate_dataset(10)

print("Generated Dataset:")
print(data)

mean, std, minimum, maximum = analyze_dataset(data)

print("\nDataset Statistics")
print("Mean:", mean)
print("Std:", std)
print("Min:", minimum)
print("Max:", maximum)

normalized_data = normalize_dataset(data)

print("\nNormalized Dataset:")
print(normalized_data)

high_income = filter_high_income(data)

print("\nPeople with High Income:")
print(high_income)

experienced = filter_experienced_people(data)

print("\nHighly Experienced People:")
print(experienced)

multiplication, transpose_A, determinant_A, inverse_A = matrix_operations()

print("\nMatrix Multiplication Result:")
print(multiplication)

print("\nTranspose of Matrix A:")
print(transpose_A)

print("\nDeterminant of Matrix A:")
print(determinant_A)

print("\nInverse of Matrix A:")
print(inverse_A)


python_time, numpy_time = benchmark_vectorization()

print("\nPerformance Benchmark")

print("Python loop time:", python_time)
print("NumPy vectorized time:", numpy_time)

image = create_random_image()

print("\nOriginal Image:")
print(image)

bright_image = increase_brightness(image)

print("\nBrightened Image:")
print(bright_image)

inverted = invert_image(image)

print("\nInverted Image:")
print(inverted)