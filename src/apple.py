import os
import pandas as pd

# Path to the directory containing the Excel files
folder_path = '../data/apple'  # All the apple files

# Initialize an empty DataFrame to hold all the data
all_data = pd.DataFrame()

# Iterate through each file in the directory
for filename in os.listdir(folder_path):
    
    if filename.endswith('.xlsx'):  # Check if the file is an Excel file
        
        file_path = os.path.join(folder_path, filename)
        
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Convert the filename into month and year columns
        parts = filename.replace('.xlsx', '').split('-')
        
        # Add new columns with the parts of the filename
        df['Month'], df['Year'] = parts

        # Append the data to the main DataFrame
        all_data = pd.concat([all_data, df], ignore_index=True)

# Outputting the combined data to a CSV file
output_csv_path = '../data/apple.csv'  # Replace with your desired output file path
all_data.to_csv(output_csv_path, index=False)