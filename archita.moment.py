import csv
import os
import requests

# Set the path to the CSV file
csv_file_path = '/Users/lexhariepisco/coding_practice/archita.moments.csv'
# Set the directory where images will be saved
output_dir = '/Users/lexhariepisco/coding_practice/archita_images'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Function to download an image from a URL
def download_image(url, output_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(output_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded: {output_path}")
        else:
            print(f"Failed to download {url}: Status code {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Open the CSV file and read each row
with open(csv_file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row_idx, row in enumerate(reader):
        for col_idx, cell in enumerate(row):
            # Skip empty cells
            if not cell.strip():
                continue

            # Extract the file name from the URL
            file_name = os.path.basename(cell)
            # Create the full output path
            output_path = os.path.join(output_dir, f"{row_idx}_{col_idx}_{file_name}")

            # Download the image
            download_image(cell, output_path)
