import pandas as pd

def load_csv_optimized(file_path: str, chunksize: int = 100000, **kwargs) -> pd.DataFrame:
    """
    Loads a large CSV file in an optimized way, leveraging high RAM capacity.

    Args:
        file_path (str): The path to the CSV file.
        chunksize (int): Number of rows to read at a time. Adjust based on available RAM and file size.
        **kwargs: Additional keyword arguments to pass to pandas.read_csv.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    print(f"Loading CSV: {file_path} with chunksize: {chunksize}")
    df_list = []
    for chunk in pd.read_csv(file_path, chunksize=chunksize, low_memory=False, **kwargs):
        df_list.append(chunk)
    return pd.concat(df_list, ignore_index=True)

if __name__ == "__main__":
    # Example usage (replace with your actual file path)
    # Create a dummy large CSV for testing
    dummy_data = {
        "col1": range(1000000),
        "col2": [f"text_{i}" for i in range(1000000)],
        "col3": [i * 1.5 for i in range(1000000)],
    }
    dummy_df = pd.DataFrame(dummy_data)
    dummy_csv_path = "large_dummy.csv"
    dummy_df.to_csv(dummy_csv_path, index=False)
    print(f"Dummy CSV created at: {dummy_csv_path}")

    # Load the dummy CSV using the optimized function
    df = load_csv_optimized(dummy_csv_path)
    print(f"DataFrame loaded with {len(df)} rows and {len(df.columns)} columns.")
    print(df.head())
