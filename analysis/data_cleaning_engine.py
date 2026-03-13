import numpy as np
import csv


def detect_delimiter(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        sample = file.read(1024)

    try:
        dialect = csv.Sniffer().sniff(sample)
        return dialect.delimiter
    except:
        return ","


def load_and_clean_dataset(file_path):

    delimiter = detect_delimiter(file_path)

    rows = []

    with open(file_path, "r", encoding="utf-8") as file:

        reader = csv.reader(file, delimiter=delimiter)

        headers = next(reader)

        for row in reader:

            if len(row) == 0:
                continue

            rows.append(row)

    raw_data = np.array(rows, dtype=object)

    numeric_columns = []

    missing_values = 0

    for col in range(raw_data.shape[1]):

        column = raw_data[:, col]

        cleaned = []

        for value in column:

            try:
                cleaned.append(float(value))

            except:
                cleaned.append(np.nan)

        numeric_col = np.array(cleaned, dtype=float)

        missing_values += np.isnan(numeric_col).sum()

        if np.all(np.isnan(numeric_col)):
            continue

        mean_val = np.nanmean(numeric_col)

        numeric_col = np.where(np.isnan(numeric_col), mean_val, numeric_col)

        numeric_columns.append(numeric_col)

    if len(numeric_columns) == 0:
        print("No numeric columns found in dataset.")
        return None, None, None

    numeric_matrix = np.column_stack(numeric_columns)

    return numeric_matrix, raw_data, missing_values