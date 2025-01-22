import pandas as pd

# Function to compare files and clean all columns
def compare_files():
    # Prompt user for file paths
    file1 = input("Enter the path to the first CSV file: ").strip()
    file2 = input("Enter the path to the second CSV file: ").strip()

    # Load the CSV files into DataFrames
    file1_df = pd.read_csv(file1)
    file2_df = pd.read_csv(file2)

    # Clean all columns: strip whitespace and remove extra newlines
    file1_df = file1_df.applymap(lambda x: x.strip().replace('\n', ' ') if isinstance(x, str) else x)
    file2_df = file2_df.applymap(lambda x: x.strip().replace('\n', ' ') if isinstance(x, str) else x)

    # Display available columns in each file
    print("\nColumns in File 1:", list(file1_df.columns))
    print("Columns in File 2:", list(file2_df.columns))

    # Prompt user for columns to compare (comma-separated)
    cols_to_compare = input("\nEnter the column names to compare (comma-separated): ").strip().split(",")

    # Validate the columns
    for col in cols_to_compare:
        col = col.strip()
        if col not in file1_df.columns or col not in file2_df.columns:
            print(f"Column '{col}' not found in both files. Please check and try again.")
            return

    # Extract relevant columns for comparison
    file1_data = file1_df[cols_to_compare].drop_duplicates()
    file2_data = file2_df[cols_to_compare].drop_duplicates()

    # Find differences: rows in file1 not in file2
    differences = pd.concat([file1_data, file2_data]).drop_duplicates(keep=False)

    # Save the differences to a CSV file
    output_file = input("\nEnter the path to save the differences CSV file: ").strip()
    differences.to_csv(output_file, index=False)

    print(f"\nDifferences saved to {output_file}")
    print(differences)

# Call the function
if __name__ == "__main__":
    compare_files()
