# import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('budget_data.csv')
total_months = 1
total_revenue = 0
sum_net_change = 0
greatest_increase = ['', 0]
greatest_decrease = ['', 999999999999999999]

# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
  
    first_row = next(csvreader)
    months = first_row[0]
    revenues = int(first_row[1])
    total_revenue += revenues
    previous_row_revenue = int(first_row[1])
    # Read each row of data after the header
    for row in csvreader:
        months = row[0]
        revenues = int(row[1])
        total_months += 1
        total_revenue += revenues
        net_change = revenues - previous_row_revenue
        previous_row_revenue = revenues
        sum_net_change += net_change
        average_change = sum_net_change / (total_months -1)
        greatest_increase = net_change >= net_change 
print(greatest_increase)
#Greatest Increase in Profits


			
# Print to terminal
print (f"Total Months: {total_months}")
print (f"Total: ${total_revenue}")
print('Average Change: $%3.2f' % average_change)
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decrease in Profits: ") 

