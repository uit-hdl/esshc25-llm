#!/usr/bin/env python3
import csv
import sys

def safe_open(filename, mode, encoding="utf-8"):
    """
    Open a file using the specified encoding. If a UnicodeDecodeError occurs,
    retry using 'latin-1'.
    """
    try:
        return open(filename, mode, encoding=encoding, newline='')
    except UnicodeDecodeError:
        sys.stderr.write(f"Warning: Failed to decode {filename} using {encoding}. Trying fallback encoding 'latin-1'.\n")
        return open(filename, mode, encoding="latin-1", newline='')

def load_mapping(mapping_filename, has_header=False):
    """
    Load the mapping file (CSV, comma-separated).
    This file should have at least two columns:
      - First column: original CoD
      - Second column: cleaned CoD
    Since the mapping file does not have a header by default, the function
    does not skip any rows unless 'has_header' is set to True.
    """
    mapping = {}
    with safe_open(mapping_filename, 'r') as f:
        # Specify comma as delimiter for the mapping file.
        reader = csv.reader(f, delimiter=',')
        if has_header:
            next(reader, None)  # Skip header row if present.

        rowNum = 1
        for row in reader:
            if len(row) < 2:
                sys.stderr.write("Skip: " + str(row) + "\n")
                continue  # Skip incomplete rows.
            original, cleaned = row[0].strip(), row[1].strip()
            #print("Mapping", str(rowNum), ":", original, "->", cleaned + "\n")
            mapping[str.lower(original)] = cleaned
            rowNum = rowNum + 1

    return mapping

def process_file(mapping, input_filename, output_filename):
    """
    Process the input file:
      - The input file is expected to be tab-separated and include a header.
      - It must include the column 'cod_ori'.
      - For each row, the script uses the 'cod_ori' value to look up a cleaned version in the mapping.
      - If no mapping is found for a given 'cod_ori', an error is output and the script exits.
      - A new output file (tab-separated) is written with the same header,
        but with the 'cod_ori' column replaced by its cleaned value.
    """
    with safe_open(input_filename, 'r') as infile, \
         open(output_filename, 'w', encoding='utf-8', newline='') as outfile:
        
        reader = csv.DictReader(infile, delimiter=',')
        if not reader.fieldnames:
            sys.stderr.write("Error: Input file has no header.\n")
            sys.exit(1)
        
        if "cod_ori" not in reader.fieldnames:
            sys.stderr.write("Error: Input file does not contain the 'cod_ori' column.\n")
            sys.exit(1)
        
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames, delimiter=',')
        writer.writeheader()
        
        for line_num, row in enumerate(reader, start=2):  # start=2 to account for header row.
            cod_ori = row.get("cod_ori", "").strip()
            cod_ori = str.lower(cod_ori)
            if not cod_ori:
                sys.stderr.write(f"Error: Missing 'cod_ori' value in row {line_num}.\n")
                sys.stderr.write(str(row) + "\n\n")
                #sys.exit(1)
                #continue
            if cod_ori not in mapping:
                sys.stderr.write(f"Error: No mapping found for cod_ori '{cod_ori}' in row {line_num}.\n")
                sys.stderr.write(str(row) + "\n\n")
                if cod_ori == "!!":
                    sys.stderr.write(f"Fixing !! \n")
                else:
                    sys.exit(1)
                #continue
            else:
                row["cod_ori"] = mapping[cod_ori]
            writer.writerow(row)
            print("wrote", line_num)

def main():
    # Usage: python update_cod.py mapping_file input_file output_file [has_header: True/False]
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        sys.stderr.write("Usage: {} mapping_file input_file output_file [has_header: True/False]\n".format(sys.argv[0]))
        sys.exit(1)
    
    mapping_filename = sys.argv[1]
    input_filename = sys.argv[2]
    output_filename = sys.argv[3]
    
    # For the mapping file, default to False since it does not have a header.
    has_header = False
    if len(sys.argv) == 5:
        has_header = sys.argv[4].lower() in ("true", "1", "yes")
    
    mapping = load_mapping(mapping_filename, has_header=has_header)
    process_file(mapping, input_filename, output_filename)

if __name__ == '__main__':
    main()
