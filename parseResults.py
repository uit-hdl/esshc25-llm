import re
import sys

def parse_line(line):
    """
    Parse the line and return a tuple (cause, description) if the line matches the expected format.
    Expected format:
      Cause of death: <CAUSE OF DEATH>, ICD-10 code: <ICD-10 CODE> <ICD-10 Description>
    """
    pattern = r"^Cause of death:\s*(.+?),\s*ICD-10 code:\s*\S+\s+(.+)$"
    match = re.match(pattern, line)
    if match:
        cause = match.group(1).strip()
        description = match.group(2).strip()
        return cause, description
    return None

def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_icd10_desc.py <input_file> <output_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    output_lines = []
    with open(input_filename, "r", encoding="utf-8") as infile:
        for lineno, line in enumerate(infile, 1):
            line = line.strip()
            if not line:
                continue  # Ignore empty lines
            parsed = parse_line(line)
            if parsed is None:
                sys.stderr.write(f"Warning: Line {lineno} could not be parsed: {line}\n")
            else:
                cause, description = parsed
                output_lines.append(f"{cause}; {description}")
    
    with open(output_filename, "w", encoding="utf-8") as outfile:
        for out_line in output_lines:
            outfile.write(out_line + "\n")
    
    print(f"Processing complete. {len(output_lines)} lines written to '{output_filename}'.")

if __name__ == "__main__":
    main()
