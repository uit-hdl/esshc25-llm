import sys
import re
import pandas as pd

def normalize_cause(cause):
    """
    Normalize a cause-of-death string:
      - Strip leading/trailing whitespace.
      - Convert to lowercase.
      - Replace semicolons with commas.
      - Collapse multiple spaces into one.
    """
    cause = cause.strip().lower()
    cause = cause.replace(";", ",")
    cause = re.sub(r'\s+', ' ', cause)
    return cause

def main():
    # Require at least a results file and one ICD10 code.
    if len(sys.argv) < 3:
        print("Usage: python script.py <results_file.txt> <ICD10_code1> [<ICD10_code2> ...]")
        sys.exit(1)
    
    results_filename = sys.argv[1]
    icd10_codes_input = set(sys.argv[2:])
    
    # Process the results file.
    # Build a set of valid normalized cod_ori values found in the results file.
    found_cod_ori = set()
    
    try:
        with open(results_filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # Expect the line format to be: "<cause> | ICD10: <icd10 code>"
                if " | ICD10: " in line:
                    parts = line.split(" | ICD10: ")
                    if len(parts) == 2:
                        norm_cause = normalize_cause(parts[0])
                        found_cod_ori.add(norm_cause)
                    else:
                        print("Unexpected format:", line)
                else:
                    # Print any error or non-matching lines as-is.
                    print(line)
    except FileNotFoundError:
        print(f"Error: File '{results_filename}' not found.")
        sys.exit(1)
    
    # Read the cleaned CSV file.
    try:
        df = pd.read_csv("icd10h_v3-cleaned.csv")
    except FileNotFoundError:
        print("Error: File 'icd10h_v3-cleaned.csv' not found.")
        sys.exit(1)
    
    found_count = 0
    not_found_count = 0
    
    # Iterate over each row in the CSV.
    # We now use the "icd10" column for lookup.
    for _, row in df.iterrows():
        if row["icd10"] in icd10_codes_input:
            cod_ori_value = str(row["cod_ori"])
            norm_cod_ori = normalize_cause(cod_ori_value)
            if norm_cod_ori in found_cod_ori:
                found_count += 1
            else:
                not_found_count += 1
                print(f"Not found: cod_ori = '{cod_ori_value}', icd10 = {row['icd10']}")
    
    total_rows = found_count + not_found_count
    print("\nSummary:")
    print(f"Total rows with icd10 in input set: {total_rows}")
    print(f"Found count: {found_count}")
    print(f"Not found count: {not_found_count}")

if __name__ == "__main__":
    main()