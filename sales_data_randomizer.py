import random
import csv
import time
import shutil
import os
import logging
from datetime import datetime

# Configure logging
log_file = '/Users/nelsonespiritu/Desktop/tuomas/shuffle_backup_log.log'
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Define paths for backup and original file
backup_dir = '/Users/nelsonespiritu/Desktop/tuomas/backup'
orig_file = '/Users/nelsonespiritu/Desktop/tuomas/sales_data.csv'

# Create the backup directory if it doesn't exist
os.makedirs(backup_dir, exist_ok=True)

# Define the number of repetitions and the delay between each
repetitions = 3  # Adjust the number of repetitions as needed
delay_seconds = 10  # Wait for 10 seconds between each repetition

for i in range(repetitions):
    try:
        # Step 1: Backup the original file
        backup_file = shutil.copy(orig_file, backup_dir)
        logging.info(f'Backup created at {backup_file}')

        # Step 2: Open and read the original file, excluding the header for shuffling
        with open(orig_file, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')  # Adjust delimiter if needed
            header = next(reader)  # Extract header
            rows = list(reader)  # Load all rows into a list

        # Step 3: Shuffle the rows (excluding the header)
        random.shuffle(rows)

        # Step 4: Write the shuffled data back to the original file
        with open(orig_file, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"')
            writer.writerow(header)  # Write the header first
            writer.writerows(rows)   # Write the shuffled rows

        # Log successful shuffle and write operation
        logging.info(f'Shuffled data has been written back to {orig_file}')

    except Exception as e:
        # Log any errors that occur
        logging.error(f"An error occurred: {e}")

    # Step 5: Wait for the specified duration before the next repetition
    print(f"Waiting for {delay_seconds} seconds before the next iteration...\n")
    time.sleep(delay_seconds)  # Pause for the specified duration
