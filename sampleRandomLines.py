#!/usr/bin/env python3

import sys
import random

def main():
    if len(sys.argv) != 4:
        print("Usage: python random_lines.py <input_file> <output_file> <num_lines>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    num_lines_to_select = int(sys.argv[3])

    # Read lines from the input file
    with open(input_file, 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()

    # Ensure we don't request more lines than exist in the file
    if num_lines_to_select > len(lines):
        print(f"Requested {num_lines_to_select} lines, but the file only has {len(lines)} lines.")
        sys.exit(1)

    # Select random lines
    selected_lines = random.sample(lines, num_lines_to_select)

    # Write them to the output file
    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.writelines(selected_lines)

    print(f"Successfully wrote {num_lines_to_select} randomly selected lines to '{output_file}'.")


if __name__ == "__main__":
    main()