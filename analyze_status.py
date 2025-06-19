#!/usr/bin/env python3
"""
Script to analyze the Status of Re-deployment from a CSV export.
This script reads a CSV file and provides counts and percentages for each status.

Usage:
    python3 analyze_status.py

The script expects 'export-7.csv' in the same directory with UTF-16 encoding and tab separation.
"""

import pandas as pd
import sys

def analyze_deployment_status(file_path='export-7.csv'):
    """
    Analyze the Status of Re-deployment column from the CSV file.
    
    Args:
        file_path (str): Path to the CSV file to analyze
        
    Returns:
        None: Prints the analysis results to stdout
    """
    try:
        # Read the CSV file with UTF-16 encoding and tab separator
        df = pd.read_csv(file_path, encoding='utf-16', sep='\t')
        
        # The exact column name for Status of Re-deployment
        status_column = '(J) Status of Re-DeploymentOPENNOT APPLICABLEIN PROGRESSBLOCKEDCOMPLETED'
            
        # Clean up the status values
        df[status_column] = df[status_column].astype(str).str.strip()
        df[status_column] = df[status_column].replace('nan', 'Not Specified')
        
        # Count the number of items in each status
        status_counts = df[status_column].value_counts().sort_index()
        
        print("\nStatus of Re-deployment Counts:")
        print("===============================")
        for status, count in status_counts.items():
            print(f"{status}: {count}")
        
        # Calculate and show percentages
        print("\nStatus of Re-deployment Percentages:")
        print("===================================")
        percentages = df[status_column].value_counts(normalize=True).sort_index() * 100
        for status, percentage in percentages.items():
            print(f"{status}: {percentage:.1f}%")
        
        print(f"\nTotal number of items: {len(df)}")

    except Exception as e:
        print(f"Error processing the CSV file: {str(e)}")
        print("Please check if the file exists and is properly formatted")
        sys.exit(1)

if __name__ == "__main__":
    analyze_deployment_status() 