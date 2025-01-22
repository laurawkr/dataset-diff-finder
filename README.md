# Dataset Difference Finder

A Python-based utility to compare two CSV files and find differences between them based on user-specified columns. This tool is ideal for identifying mismatched or missing rows in datasets.

## Features

- Cleans column data by stripping whitespace and removing newlines.
- Allows users to specify columns to compare.
- Displays differences in rows between two CSV files.
- Saves the differences into a new CSV file for easy access.

## Requirements

- Python 3.x
- pandas library

To install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Clone the Repository
```bash
git clone <repository_url>
cd dataset-diff-finder
```

### 2. Run the Script
```bash
python main.py
```

### 3. Follow the Prompts

1. Enter the path to the first CSV file (e.g., `path/to/data-set-1.csv`).
2. Enter the path to the second CSV file (e.g., `path/to/data-set-2.csv`).
3. View the available columns in both files and specify the columns to compare (comma-separated, e.g., `state,city`).
4. Enter the path to save the differences CSV file (e.g., `path/to/diffs.csv`).

### Example Input and Output

#### Input Files:

**data-set-1.csv**:
```
state,city,pop
NY,NYC,8.8
CA,LA,3.8
IL,CHI,2.5
```

**data-set-2.csv**:
```
state,city,pop
NY,NYC,8.8
CA,LA,3.8
```

#### Command Execution:
```
Enter the path to the first CSV file: path/to/data-set-1.csv
Enter the path to the second CSV file: path/to/data-set-2.csv
Columns in File 1: ['state', 'city', 'pop']
Columns in File 2: ['state', 'city', 'pop']
Enter the column names to compare (comma-separated): state,city
Enter the path to save the differences CSV file: path/to/diffs.csv
```

#### Output File:

**diffs.csv**:
```
state,city,pop
IL,CHI,2.5
```

## File Structure

```
dataset-diff-finder/
├── .venv/               # Virtual environment (optional)
├── tests/               # Directory for test files
├── venv/                # Virtual environment (if used)
├── .gitignore           # Git ignored files
├── main.py              # Main Python script
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
```

## Notes

- Ensure that both CSV files have the same structure (matching columns) for accurate comparisons.
- Only rows that differ between the two files will be saved in the output file.

## License

This project is open-source and available under the MIT License.