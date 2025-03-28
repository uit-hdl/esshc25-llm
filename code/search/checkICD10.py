import pandas as pd
import sys

def main():
    # Ensure the causes file is provided as a command-line argument.
    if len(sys.argv) != 2:
        print("Usage: python script.py <causes_file.txt>")
        sys.exit(1)

    causes_file = sys.argv[1]

    # Read the causes of death from the provided file, one per line.
    try:
        with open(causes_file, 'r', encoding='utf-8') as f:
            causes_input = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{causes_file}' not found.")
        sys.exit(1)

    # Load the CSV file containing ICD10 data.
    try:
        df = pd.read_csv("icd10h_v3-cleaned.csv")
    except FileNotFoundError:
        print("Error: File 'icd10h_v3-cleaned.csv' not found.")
        sys.exit(1)
    
    # Process each cause from the file.
    for cause in causes_input:
        # Replace ";" with "," in the cause string
        cause_modified = cause.replace(";", ",")
        
        # Find rows where the 'cod_ori' column matches the modified cause (ignoring case)
        matches = df[df['cod_ori'].str.lower() == cause_modified.lower()]
        
        if matches.empty:
            print(f"Cause of death '{cause_modified}' not found.")
        else:
            # If multiple matches exist, print them all.
            for _, row in matches.iterrows():
                icd10_code = row['icd10']
                print(f"{cause_modified} | ICD10: {icd10_code}")

if __name__ == "__main__":
    main()