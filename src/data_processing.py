import pandas as pd

def load_and_process_data(input_path, output_path):
    """Load Data, Cleaning Data, drop columns name =  'Id' and save to ['iris_cleaned.csv']"""
    
    df = pd.read_csv(input_path)
    
    df.dropna(inplace=True)

    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df = df[df[col] >= 0]

    if 'Id' in df.columns:
        df.drop(columns=['Id'], inplace=True)

    if "Species" in df.columns:
        df["Species"] = df["Species"].astype("category")

    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to: {output_path}")

if __name__ == "__main__":
    input_csv = "../data/raw/Iris.csv"
    output_csv = "../data/processed/iris_cleaned.csv"
    
    load_and_process_data(input_csv, output_csv)
