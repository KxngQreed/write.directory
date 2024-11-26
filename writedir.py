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
directory_path = r"C:\Users\Reagan\Desktop\Sonar\NOV STMTS"
output_excel_path = r"C:\Users\Reagan\Desktop\Sonar\NOV STMTS\output.xlsx"
list_directory_contents_to_excel(directory_path, output_excel_path)
