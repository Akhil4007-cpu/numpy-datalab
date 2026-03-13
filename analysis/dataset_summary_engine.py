def dataset_summary(raw_data, numeric_matrix, missing_values):

    rows = raw_data.shape[0]
    cols = raw_data.shape[1]

    numeric_cols = numeric_matrix.shape[1]

    text_cols = cols - numeric_cols

    print("\nDataset Summary")
    print("----------------")

    print("Rows:", rows)
    print("Columns:", cols)
    print("Numeric Columns:", numeric_cols)
    print("Text Columns:", text_cols)
    print("Missing Values Filled:", int(missing_values))