import csv
import os
from datetime import datetime
from US_AreaCodes import area_codes

# Get the current directory
current_directory = os.getcwd()

# Define the path to the output directory
output_directory = os.path.join(current_directory, "callLogExtractions")

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Define the current date and time
current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")

# Define the output file name with the current date and time
output_file_name = f"callLogs_extraction-{current_datetime}.csv"

# Define the path to the output CSV file
csv_file_path = os.path.join(output_directory, output_file_name)

# List to store the extracted call data
call_data = []

# Define the path to your directory containing the .csv files
directory_path = os.path.join(current_directory, "Meech_Moto5GAce_Call-Logs-Data_6-21-23")

# Process each .csv file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory_path, filename)

        # Open the .csv file with the appropriate encoding (e.g., 'utf-8')
        with open(file_path, 'r', encoding='utf-8') as file:
            # Create a CSV reader object
            reader = csv.reader(file)

            # Skip the header row
            next(reader)

            # Extract the call data from each row
            for row in reader:
                name = row[0]
                address = row[1]
                direction = row[2]
                status = row[3]
                duration = row[4]
                date = row[5]

                # Extract the area code from the address
                area_code = address[2:5]

                # Determine the location based on the area code
                location = area_codes.get(area_code, "Unknown")

                # Add the entry to the call_data list
                call_data.append([name, address, direction, status, duration, date, area_code, location])

# Sort the call data by area code
sorted_call_data = sorted(call_data, key=lambda x: x[1])

# Write the data to the output CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(["Name", "Address", "Direction", "Status", "Duration", "Date", "Area code", "Location"])

    # Write the data rows
    writer.writerows(sorted_call_data)

# Print the output to the terminal
for entry in sorted_call_data:
    print(f"Name: {entry[0]}, Address: {entry[1]}, Direction: {entry[2]}, Status: {entry[3]}, "
          f"Duration: {entry[4]}, Date: {entry[5]}, Area code: {entry[6]}, Location: {entry[7]}")

print("Data has been written to the CSV file.")
