
import re
import csv
from US_AreaCodes import area_codes
from CountryAreaCodes import country_area_codes
import os
from datetime import datetime

# Get the current directory
current_directory = os.getcwd()

# Define the path to your logs file
logs_file = os.path.join(current_directory, "Meech_Moto-5G-ACE_FullLogs-6-20-23.txt")

# Regular expression pattern to match the date
date_pattern = r'(\d{2}-\d{2})'

# Regular expression pattern to match the timestamp
timestamp_pattern = r'(\d{2}:\d{2}:\d{2})'

# Regular expression pattern to match phone numbers
phone_number_pattern = r'\b(?:\+?1[-.\s]?)?(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{4})\b'

# Combine the patterns into one regular expression
combined_pattern = rf'{date_pattern}.*?{timestamp_pattern}.*?{phone_number_pattern}'

# Define the current date and time
current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")

# Define the output file name with the current date and time
output_file_name = f"phoneLogs_extraction-{current_datetime}.csv"

# Define the path to the output CSV file
csv_file_path = os.path.join(current_directory, "phoneLogExtractions" , output_file_name)

# Open the logs file with the appropriate encoding (e.g., 'utf-8')
with open(logs_file, 'r', encoding='utf-8') as file:
    # Read the file contents
    logs = file.read()

    # Find all occurrences of phone numbers in the logs
    phone_numbers = re.findall(combined_pattern, logs)

    # Sort the phone numbers by area code
    sorted_phone_numbers = sorted(phone_numbers, key=lambda x: x[2])

    # Store the output in a list
    output = []

    # Add the header row to the output list
    output.append(["Date", "Timestamp", "Phone number", "Area code", "Location"])

    # Add each phone number entry to the output list
    for entry in sorted_phone_numbers:
        date = entry[0]
        timestamp = entry[1]
        area_code = entry[2]
        formatted_number = '-'.join(entry[2:])
        location = area_codes.get(area_code, country_area_codes.get(area_code, 'Unknown'))

        # Add the entry to the output list
        output.append([date, timestamp, formatted_number, area_code, location])

    # Open the CSV file to write data
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write the data from the output list to the CSV file
        writer.writerows(output)

# Print the output to the terminal
for entry in output:
    print(f"Date: {entry[0]}, Timestamp: {entry[1]}, Phone number: {entry[2]}, Area code: {entry[3]}, Location: {entry[4]}")

print("Data has been written to the CSV file.")
