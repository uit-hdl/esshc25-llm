import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python map_icd10.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Keep track of pairs we've already seen
    seen_pairs = set()

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            # Read and discard header
            header = next(f, None)
            
            for line in f:
                # Strip newline and split on tabs
                columns = line.strip().split('\t')
                if len(columns) < 6:
                    # Not enough columns, skip
                    continue

                icd10_code = columns[4].strip()  # 5th column (zero-index)
                icd10_desc = columns[5].strip()  # 6th column (zero-index)

                # Split the icd10_desc by "|"
                parts = icd10_desc.split("|")

                # We want the second part if it exists; otherwise, use the first part
                if len(parts) > 1:
                    desc_second_part = parts[1].strip()
                else:
                    desc_second_part = parts[0].strip()

                # Form the pair
                pair = (desc_second_part, icd10_code)

                # Only print if we haven't seen this pair before
                if pair not in seen_pairs:
                    print(f"{desc_second_part} -> {icd10_code}")
                    seen_pairs.add(pair)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except StopIteration:
        print("Error: The file seems to be empty or has no valid lines.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

