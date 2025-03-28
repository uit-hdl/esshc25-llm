import sys
import pandas as pd

def main():
    if len(sys.argv) != 2:
        print("Usage: python verify_results.py <results_file.txt>")
        sys.exit(1)

    results_filename = sys.argv[1]
    results_data = []  # List to hold tuples: (cause, result_icd)

    # Read the results file (assumed to be tab-delimited)
    try:
        with open(results_filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                # Expecting two fields separated by a tab.
                parts = line.split("\t")
                if len(parts) < 2:
                    print("Skipping line with unexpected format:", line)
                    continue
                # Replace semicolons with commas in the cause string.
                cause = parts[0].replace(";", ",").strip()
                result_icd = parts[1].strip()
                results_data.append((cause, result_icd))
    except FileNotFoundError:
        print(f"Error: Results file '{results_filename}' not found.")
        sys.exit(1)

    # Load the cleaned CSV file.
    try:
        df = pd.read_csv("icd10h_v3-cleaned.csv")
    except FileNotFoundError:
        print("Error: File 'icd10h_v3-cleaned.csv' not found.")
        sys.exit(1)

    # Build a lookup dictionary from the cleaned table:
    # Key: lower-case cod_ori (cause-of-death string), Value: ICD10h code from the table.
    table_lookup = {}
    for _, row in df.iterrows():
        cod_ori = str(row["cod_ori"]).strip().lower()
        icd10h_table = str(row["ICD10h"]).strip()  # use the correct column here
        table_lookup[cod_ori] = icd10h_table

    total = 0
    matches = 0
    mismatches = 0

    # For each result, lookup the cause in the table and compare ICD10 codes.
    for cause, result_icd in results_data:
        total += 1
        lookup_key = cause.lower()
        if lookup_key in table_lookup:
            table_icd = table_lookup[lookup_key]
            if result_icd == table_icd:
                matches += 1
            else:
                mismatches += 1
                print(f"Mismatch: Cause '{cause}': LLM ICD10h = {result_icd}, Table ICD10h = {table_icd}")
        else:
            mismatches += 1
            print(f"Not found in table: Cause '{cause}', Result ICD10 = {result_icd}")

    # Report summary counts.
    print("\nSummary:")
    print(f"Total results processed: {total}")
    print(f"Matches: {matches}")
    print(f"Mismatches: {mismatches}")

if __name__ == "__main__":
    main()