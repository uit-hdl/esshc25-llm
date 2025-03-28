#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(
        description='Parse a CSV file, count records by cause of death (cod_ori), '
                    'and produce a cumulative distribution plot.'
    )
    parser.add_argument('input_file', help='Path to the input CSV file.')
    parser.add_argument('output_file', help='Path for the output plot image (e.g., .png).')
    args = parser.parse_args()

    # 1. Read the CSV file (adjust delimiter if necessary)
    #    If your file is tab-delimited, use sep='\t'
    df = pd.read_csv(args.input_file, sep=',')
    
    # 2. Count how many records there are for each cause of death (cod_ori)
    cause_counts = df['cod_ori'].value_counts().sort_values(ascending=False)
    
    # 3. Print out the cause of death and how many records
    print("Cause of Death (cod_ori) : Record Count")
    for cause, count in cause_counts.items():
        print(f"{cause} : {count}")
    
    # 4. Create a cumulative distribution plot
    #    - We’ll make a bar plot of counts
    #    - Then add a line plot for the cumulative sum on a secondary y-axis

    cumulative_counts = cause_counts.cumsum()

    # Set up the figure
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Bar plot for raw counts
    ax1.bar(cause_counts.index, cause_counts.values, color='skyblue')
    ax1.set_xlabel('Cause of Death (cod_ori)')
    ax1.set_ylabel('Count')
    ax1.set_xticks(range(len(cause_counts)))
    ax1.set_xticklabels(cause_counts.index, rotation=90)

    # Line plot for cumulative distribution on secondary axis
    ax2 = ax1.twinx()
    ax2.plot(range(len(cause_counts)), cumulative_counts.values, color='red', marker='o')
    ax2.set_ylabel('Cumulative Count')

    plt.title('Causes of Death Distribution (cod_ori)')
    plt.tight_layout()

    # Save the figure to the specified output file
    plt.savefig(args.output_file)
    plt.close()

if __name__ == '__main__':
    main()
