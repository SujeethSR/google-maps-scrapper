import csv
import os
 
# Determine the directory where this config.py file is located
dir_path = os.path.dirname(os.path.realpath(__file__))
csv_file_path = os.path.join(dir_path, 'pincodes.csv')
 
# Read the ZIP codes from the CSV file
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header
    zip_codes = [row[0] for row in csv_reader]
 
# Construct the queries list using a list comprehension
queries = [{
    "keyword": f"{zip_code}",
    "select": ["place_id", "title", "link", "main_category", "rating", "reviews", "website",
    "phone", "address", "place_id", "status", "price_range", "description",
    "reviews_per_rating", "reviews_link", "thumbnail", "images", "hours", "menu",
    "order_online_links", "reservations", "owner", "categories", "coordinates",
    "plus_code", "complete_address", "time_zone", "about", "user_reviews", "cid",
    "data_id"]
} for zip_code in zip_codes]
 
 
number_of_scrapers = 10
 
 
# "keyword": f"Liquor stores in {zip_code}",
 