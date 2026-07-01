import pandas as pd

def load_data(file_Path):
    """
    Reads a csv fiel and retur dataframe
    """
    try:
        df = pd.read_csv(file_Path)
        return df
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
