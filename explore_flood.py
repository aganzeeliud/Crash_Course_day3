import pandas as pd

try:
    df = pd.read_excel('floodarchive.xlsx', engine='openpyxl')
    print("Columns in the file:")
    print(df.columns.tolist())
    print("\nFirst 5 rows:")
    print(df.head())
except Exception as e:
    print(f"Error reading file: {e}")
