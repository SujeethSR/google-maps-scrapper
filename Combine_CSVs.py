import os
import pandas as pd
from bose.launch_tasks import launch_tasks
from src import tasks_to_be_run
from src.scrape_google_maps_links_task import ScrapeGoogleMapsLinksTask

# Function to remove duplicates from a DataFrame
def remove_duplicates(df):
    return df.drop_duplicates(subset=['link'], keep='first')

def main():
    # Launch the scraping tasks
    launch_tasks(*tasks_to_be_run)
    
    # Wait for the scraping tasks to finish (you might need to implement this)
    # You can add code to check if scraping is completed, e.g., by monitoring a flag in LocalStorage
    
    # Merge CSVs
    folder_path = "/Users/sujeeth/Projects/Uncode/google-maps-scrapper/output"  # Update this to your folder path

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

    # Remove duplicates
    merged_data = remove_duplicates(merged_data)

    # Save the merged data to a new CSV file without duplicates
    merged_data.to_csv(os.path.join(folder_path, "All_merged_file.csv"), index=False)

    # Notify when the task is complete
    print("Scraping and merging completed.")

if __name__ == "__main__":
    main()