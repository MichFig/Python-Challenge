# import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('budget_data.csv')
total_months = 1
total_revenue = 0
sum_net_change = 0
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)  
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    first_row = next(csvreader)
    month = first_row[0]
    revenue = int(first_row[1])
    total_revenue += revenue
    previous_row_revenue = int(first_row[1])
    # Read each row of data after the header
    for row in csvreader:
        month = row[0]
        revenue = int(row[1])
        total_months += 1
        total_revenue += revenue
        print(f"Months: {month}")
        print(f"Revenue: {revenue}")
        print(f"Previous Row Revenue: {previous_row_revenue}")
        net_change = revenue - previous_row_revenue
        print(f"Net Change: {net_change}")
        previous_row_revenue = revenue
        sum_net_change += net_change
        average_change = sum_net_change / (total_months -1)
# Print total months and print total revenue
print (f"Total Months: {total_months}")
print (f"Total: ${total_revenue}")
print('Average Change: $%3.2f' % average_change)

