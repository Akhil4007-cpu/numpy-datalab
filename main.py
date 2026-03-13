import sys

from analysis.data_cleaning_engine import load_and_clean_dataset
from analysis.dataset_summary_engine import dataset_summary
from analysis.statistics_engine import analyze_dataset
from analysis.normalization_engine import normalize_dataset
from analysis.linear_algebra_engine import matrix_operations
from analysis.benchmark_engine import benchmark_vectorization


def main():

    if len(sys.argv) < 2:
        print("Usage: python main.py <dataset.csv>")
        return

    file_path = sys.argv[1]

    numeric_matrix, raw_data, missing_values = load_and_clean_dataset(file_path)

    if numeric_matrix is None:
        return

    dataset_summary(raw_data, numeric_matrix, missing_values)

    print("\nCleaned Numeric Dataset:")
    print(numeric_matrix)

    mean, std, minimum, maximum = analyze_dataset(numeric_matrix)

    print("\nDataset Statistics")

    print("Mean:", mean)
    print("Std:", std)
    print("Min:", minimum)
    print("Max:", maximum)

    normalized_data = normalize_dataset(numeric_matrix)

    print("\nNormalized Dataset:")
    print(normalized_data)

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


if __name__ == "__main__":
    main()