import os
import requests
import csv

# Set the directory where images will be saved
save_dir = "/Users/lexhariepisco/Downloads/archita-arts"

# Create the directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Path to your CSV file
csv_file = '/Users/lexhariepisco/Downloads/default.moments.csv'  # Replace with your actual CSV file path

# Read the CSV file and download images
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if row:  # Ensure the row is not empty
            url = row[0]
            try:
                response = requests.get(url)
                response.raise_for_status()  # Check if the request was successful
                # Save the image
                file_name = f"image_{i+1}.jpg"  # You can customize the file name
                file_path = os.path.join(save_dir, file_name)
                with open(file_path, 'wb') as img_file:
                    img_file.write(response.content)
                print(f"Downloaded {file_name}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download {url}: {e}")
