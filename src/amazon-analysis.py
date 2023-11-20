import pandas as pd

# Load the CSV file
csv_file_path = '../data/amazon.csv'
df = pd.read_csv(csv_file_path)

# Get the column titles
column_titles = df.columns.tolist()

# Grouping by 'Title', 'Month', and 'Year'
grouped_data = df.groupby(['Year','Month', 'Item Name'])[['Sales Price (Marketplace Currency)', 'Estimated Earnings (Marketplace Currency)']].sum().reset_index()

# Display the grouped data
print(grouped_data)

# Outputting the combined data to a CSV file
output_csv_path = 'amazon-analysis.csv' 
grouped_data.to_csv(output_csv_path, index=False)