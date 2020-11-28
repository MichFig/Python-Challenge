# import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('budget_data.csv')
#Set your variables:
total_months = 1
total_revenue = 0
sum_net_change = 0
greatest_increase = 0
greatest_decrease = 0

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
        month = row[0]
        revenue = int(row[1])
        total_months += 1
        total_revenue += revenue
        net_change = revenue - previous_row_revenue
        previous_row_revenue = revenue
        sum_net_change += net_change
        average_change = sum_net_change / (total_months -1)
        
        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_month = month
        
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_month = month
            

       
# Print to terminal 
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print('Average Change: $%3.2f' % average_change)
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

hwfile = open("analysis.txt", "w")
hwfile.write("Financial Analysis\n")
hwfile.write(f"Total Months: {total_months}\n")
hwfile.write(f"Total: ${total_revenue}\n")
hwfile.write('Average Change: $%3.2f' % average_change)
hwfile.write('\n'f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
hwfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
hwfile.close()



   
        