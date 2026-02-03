"""
TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) Implementation

This module implements the TOPSIS multi-criteria decision analysis method.
TOPSIS ranks alternatives based on their distance from the ideal positive solution
and distance from the ideal negative solution.

Author: Harsh Tanwar
Roll Number: 102303812
Email: htanwar_be23@thapar.edu
"""

import sys
import pandas as pd
import numpy as np
import os


def check_numeric(df):
    """
    Validates that all columns from the 2nd column onwards contain numeric values.
    
    Args:
        df (pd.DataFrame): Input dataframe to validate
        
    Returns:
        bool: True if all columns (from 2nd onwards) are numeric, False otherwise
    """
    try:
        # Check from 2nd column (index 1) to the end
        df.iloc[:, 1:].astype(float)
        return True
    except ValueError:
        return False


def topsis(input_file, weights, impacts, result_file):
    """
    Implements the TOPSIS algorithm to rank alternatives based on multiple criteria.
    
    The algorithm follows these steps:
    1. Load and validate input data
    2. Normalize the decision matrix using vector normalization
    3. Apply weights to the normalized matrix
    4. Determine ideal best and ideal worst solutions
    5. Calculate Euclidean distances from ideal solutions
    6. Compute performance scores and rank alternatives
    
    Args:
        input_file (str): Path to CSV file containing alternatives and criteria values
        weights (str): Comma-separated string of weights for each criterion
        impacts (str): Comma-separated string of impacts ('+' for beneficial, '-' for non-beneficial)
        result_file (str): Path for output CSV file with TOPSIS scores and ranks
        
    Returns:
        None: Writes results to the specified output file
    """
    try:
        # Step 1: Load Data
        try:
            df = pd.read_csv(input_file)
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found.")
            return

        # Step 2: Input Validation
        if len(df.columns) < 3:
            print("Error: Input file must contain three or more columns.")
            return

        if not check_numeric(df):
            print("Error: From 2nd to last columns must contain numeric values only.")
            return

        # Calculate number of criteria (excluding the first column which contains alternative names)
        cols = len(df.columns) - 1
        
        # Parse weights and impacts from comma-separated strings
        weights = [float(w) for w in weights.split(',')]
        impacts = impacts.split(',')

        # Validate that weights, impacts, and criteria count match
        if len(weights) != cols or len(impacts) != cols:
            print("Error: The number of weights, number of impacts and number of columns (from 2nd to last columns) must be the same.")
            return

        # Validate impact values are either '+' or '-'
        if not all(i in ['+', '-'] for i in impacts):
            print("Error: Impacts must be either +ve or -ve.")
            return

        # Step 3: TOPSIS Algorithm Implementation
        
        # 3.1 Vector Normalization
        # Create a copy of numeric columns for calculations to preserve original data
        df_calc = df.iloc[:, 1:].copy().astype(float)
        
        # Calculate root sum of squares for each criterion
        rss = np.sqrt((df_calc**2).sum())
        
        # Normalize the decision matrix using vector normalization
        df_norm = df_calc / rss

        # 3.2 Weighted Normalization
        # Apply criterion weights to the normalized matrix
        df_weighted = df_norm * weights

        # 3.3 Determine Ideal Best and Ideal Worst Solutions
        ideal_best = []
        ideal_worst = []

        for i in range(cols):
            if impacts[i] == '+':
                # For beneficial criteria: maximum is ideal best, minimum is ideal worst
                ideal_best.append(df_weighted.iloc[:, i].max())
                ideal_worst.append(df_weighted.iloc[:, i].min())
            else:
                # For non-beneficial criteria: minimum is ideal best, maximum is ideal worst
                ideal_best.append(df_weighted.iloc[:, i].min())
                ideal_worst.append(df_weighted.iloc[:, i].max())

        # 3.4 Calculate Euclidean Distances
        # Distance from ideal positive solution (best)
        s_plus = np.sqrt(((df_weighted - ideal_best) ** 2).sum(axis=1))
        
        # Distance from ideal negative solution (worst)
        s_minus = np.sqrt(((df_weighted - ideal_worst) ** 2).sum(axis=1))

        # 3.5 Calculate Performance Score
        # Performance score = distance from worst / (distance from best + distance from worst)
        # Higher score indicates better performance
        total_dist = s_plus + s_minus
        performance_score = s_minus / total_dist
        
        # Step 4: Generate Output
        # Add TOPSIS score and rank columns to the original dataframe
        df['Topsis Score'] = performance_score
        
        # Rank alternatives in descending order of TOPSIS score (higher score = better rank)
        df['Rank'] = df['Topsis Score'].rank(ascending=False).astype(int)

        # Write results to output CSV file
        df.to_csv(result_file, index=False)
        print(f"Result file '{result_file}' created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main entry point for command-line execution of TOPSIS algorithm.
    
    Parses command-line arguments and calls the topsis function.
    Expected arguments:
        - InputDataFile: Path to input CSV file
        - Weights: Comma-separated weights string
        - Impacts: Comma-separated impacts string
        - OutputResultFileName: Path to output CSV file
    """
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")
        print('Example: python topsis.py data.csv "1,1,1,2,1" "+,+,+,-,+" result.csv')
        return

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result_file = sys.argv[4]

    # Additional file existence check before processing
    if not os.path.exists(input_file):
         print(f"Error: File '{input_file}' not found.")
         return

    topsis(input_file, weights, impacts, result_file)


if __name__ == "__main__":
    main()
