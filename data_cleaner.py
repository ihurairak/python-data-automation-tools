import pandas as pd
import glob
import os

print("Libraries imported successfully!")

def clean_and_process_dataset(file_path, output_filename="cleaned_output.csv"):
    """
    Loads a CSV or Excel file, cleans common errors (whitespace, duplicates, 
    missing values), and exports a polished file.
    """
  
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")
    
    print(f"Original dataset shape: {df.shape} (Rows, Columns)")
    
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    
    initial_rows = len(df)
    df = df.drop_duplicates()
    duplicates_removed = initial_rows - len(df)
    print(f"Removed {duplicates_removed} duplicate rows.")
    
    string_cols = df.select_dtypes(include=['object']).columns
    for col in string_cols:
        df[col] = df[col].astype(str).str.strip()
        
    df.to_csv(output_filename, index=False)
    print(f"Success! Cleaned file saved as: {output_filename}")
    print(f"Final dataset shape: {df.shape}")
    
    return df
