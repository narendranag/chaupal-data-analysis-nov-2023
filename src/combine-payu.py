import os
import pandas as pd

def analyse_folder_and_output_csv(folder_path, output_csv_path) :
    # Initialize an empty DataFrame to hold all the data
    all_data = pd.DataFrame()

    # Iterate through each file in the directory
    for filename in os.listdir(folder_path):
        
        if filename.endswith('.xlsx'):  # Check if the file is an Excel file
            
            file_path = os.path.join(folder_path, filename)
            
            print(f"Attempting to read {filename} ...")

            # Read the Excel file
            df = pd.read_excel(file_path)

            # Convert the filename into month and year columns
            parts = filename.replace('.xlsx', '').split(' ')
            
            # Add new columns with the parts of the filename
            df['Month'], df['Year'] = parts

            # Append the data to the main DataFrame
            all_data = pd.concat([all_data, df], ignore_index=True)

    # Outputting the combined data to a CSV file
    all_data.to_csv(output_csv_path, index=False)


analyse_folder_and_output_csv('../data/payu', '../data/payu.csv')

