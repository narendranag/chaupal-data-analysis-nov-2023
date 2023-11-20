import os
import pandas as pd

def analyse_folder_and_output_csv(folder_path, output_csv_path) :
    # Initialize an empty DataFrame to hold all the data
    all_data = pd.DataFrame()

    # Iterate through each file in the directory
    for filename in os.listdir(folder_path):
        
        if filename.endswith('.csv'):  # Check if the file is an Excel file
            
            file_path = os.path.join(folder_path, filename)
            
            # Read the Excel file
            df = pd.read_excel(file_path)

            # Convert the filename into month and year columns
            parts = filename.replace('.csv', '').split(' ')
            
            # Add new columns with the parts of the filename
            df['Month'], df['Year'] = parts

            # Append the data to the main DataFrame
            all_data = pd.concat([all_data, df], ignore_index=True)

    # Outputting the combined data to a CSV file
    all_data.to_csv(output_csv_path, index=False)

# Path to the directories containing the Excel files
folders = []
# folders.append('../data/amazon')  
# folders.append( '../data/googleplay' )
folders.append('../data/payu')
# folders.append('../data/razorpay')
folders.append('../data/stripe')

for folder in folders:
    output_filename = folder + ".csv"
    analyse_folder_and_output_csv(folder, output_filename)
