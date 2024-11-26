# Writedir

This Python script lists the contents of a specified directory and writes each file name to an individual cell in a continuous list in one column of an Excel file. 

## Features

- Lists all files in a specified directory.
- Writes the file names to an Excel file, each in a separate cell in one column.

## Requirements

- Python 3.x
- pandas library
-openpyxl library

## Installation

Install the required `pandas` and `openpyxl`libraries using pip:

```sh
pip install pandas openpyxl

Usage
To use the script, update the directory_path and output_excel_path variables with your desired paths and run the script.

Example
python
import os
import pandas as pd

def list_directory_contents_to_excel(directory_path, output_excel_path):
    # Get the list of files in the directory
    files = os.listdir(directory_path)
    
    # Create a DataFrame from the list of files
    df = pd.DataFrame(files, columns=["Files"])
    
    # Write the DataFrame to an Excel file
    df.to_excel(output_excel_path, index=False)
    
    print(f"Directory contents written to {output_excel_path}")

# Example usage
directory_path = r"C:\path\to\your\directory"
output_excel_path = r"C:\path\to\your\output.xlsx"
list_directory_contents_to_excel(directory_path, output_excel_path)
Script Details
Import Libraries:

from os import listdir: Used to list the contents of the specified directory.

import pandas as pd: Used to create a DataFrame and write to an Excel file.

Function list_directory_contents_to_excel:

Parameters:

directory_path: Path to the directory whose contents you want to list.

output_excel_path: Path to the output Excel file.

Process:

Lists the files in the specified directory.

Creates a Pandas DataFrame from the list of files.

Writes the DataFrame to an Excel file.

Example Usage:

Demonstrates how to call the list_directory_contents_to_excel function with example file paths.

Contributing
If you have any suggestions or improvements, feel free to contribute! Fork the repository and create a pull request with your changes.