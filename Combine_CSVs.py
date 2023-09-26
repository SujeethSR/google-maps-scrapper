import os
import pandas as pd

# Folder containing the CSV files
folder_path = "/Users/sivasai/Projects/Work/Uncode/Python/google-maps-scrapper/Merge CSV/merge"

# Create an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Loop through each CSV file
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # Construct the complete filepath
        filepath = os.path.join(folder_path, filename)
        
        # Read the CSV file into a DataFrame
        data = pd.read_csv(filepath)
        
        # Merge data into the merged_data DataFrame
        merged_data = pd.concat([merged_data, data])

# Save the merged data to a new CSV file
merged_data.to_csv(os.path.join(folder_path, "new_merged_file.csv"), index=False)
