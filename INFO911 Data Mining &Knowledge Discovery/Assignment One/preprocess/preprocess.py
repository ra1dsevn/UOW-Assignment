import pandas as pd

# Assuming the data is stored in a file named 'taxi.txt' in the current working directory
file_path = 'taxi.txt'

# Read the data into a pandas dataframe
# The separator is semicolon and we explicitly pass the column names
df = pd.read_csv(file_path, sep=';', names=['ID', 'DateTime', 'Location'])

# Extract latitude and longitude from the Location column into their own separate columns
df[['Latitude', 'Longitude']] = df['Location'].str.extract(r'POINT\(([^ ]+) ([^ ]+)\)')

# Drop the original Location column as we now have Latitude and Longitude
df.drop('Location', axis=1, inplace=True)

# Save the dataframe to a CSV file in the current working directory
output_file_path = 'taxi.csv'
df.to_csv(output_file_path, index=False)
print(f'Data saved to {output_file_path}')