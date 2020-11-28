# import the os module
import os
import csv
csvpath = os.path.join('election_data.csv')
# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)  
# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
# Read each row of data after the header
# for row in csvreader:

