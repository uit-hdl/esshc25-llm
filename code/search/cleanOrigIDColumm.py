import pandas as pd

def main():
    # Load the CSV file containing ICD10 data.
    try:
        df = pd.read_csv("icd10h_v3.csv", encoding='utf-8')
    except UnicodeDecodeError:
        # If utf-8 fails, try a different encoding (e.g., latin1)
        df = pd.read_csv("icd10h_v3.csv", encoding='latin1')
    except FileNotFoundError:
        print("Error: File 'icd10h_v3.csv' not found.")
        return
    
    # Load the mapping file (orig2clean.txt), assuming it is tab-delimited.
    # Try using UTF-16; if that fails, fallback to latin1.
    try:
        mapping_df = pd.read_csv("orig2clean.txt", sep="\t", header=None, names=["original", "cleaned"], encoding='utf-16')
    except UnicodeDecodeError:
        mapping_df = pd.read_csv("orig2clean.txt", sep="\t", header=None, names=["original", "cleaned"], encoding='latin1')
    except FileNotFoundError:
        print("Error: File 'orig2clean.txt' not found.")
        return

    # Create a mapping dictionary from original to cleaned values.
    mapping_dict = dict(zip(mapping_df['original'], mapping_df['cleaned']))

    # Replace values in the 'cod_ori' column with the cleaned version.
    df['cod_ori'] = df['cod_ori'].apply(lambda x: mapping_dict.get(x, x))

    # Write the modified dataframe to a new CSV file.
    output_filename = "icd10h_v3-cleaned.csv"
    df.to_csv(output_filename, index=False)
    print(f"Created file: {output_filename}")

if __name__ == "__main__":
    main()