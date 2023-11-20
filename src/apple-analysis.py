import pandas as pd

# Load the CSV file
csv_file_path = '../data/apple.csv'
df = pd.read_csv(csv_file_path)

# Get the column titles
column_titles = df.columns.tolist()
print(column_titles)

# Grouping by 'Title', 'Month', 'Year', and 'Customer Currency'
df['Customer Price'] = pd.to_numeric(df['Customer Price'], errors='coerce')
grouped_data = df.groupby(['Year', 'Month', 'Title', 'Customer Currency'])['Customer Price'].sum().reset_index()


# Display the grouped data
print(grouped_data)


# Outputting the combined data to a CSV file
output_csv_path = 'apple-analysis.csv' 
grouped_data.to_csv(output_csv_path, index=False)