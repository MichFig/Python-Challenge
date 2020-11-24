# import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
import datetime
csvpath = os.path.join('budget_data.csv')
total_pl =0
# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)  
# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    for row in csvreader:
        print(row)
        montht = row[0]
        profit_loss = int(row[1])
        total_pl += profit_loss
# set the dates to find the total number of months in the dataset
import datetime
end_date = datetime.datetime(2017,2,28)
start_date = datetime.datetime(2009,12, 31)
num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
print (f"Total Months: {num_months}")
print (f"Total: ${total_pl}")

