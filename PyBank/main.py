# Data Analysis Bootcamp Assignment 3: Py Me Up, Charlie (PyBank)

# Import dependencies
import os
import csv

# Initialize the variables
total_months = 0
net_total = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Set the file path
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Open & read the CSV file
with open(csvpath, newline = '') as csvfile:
    
    # Initialize CSV reader
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # Skips reading the header
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Calculate the variables
    previous_row = int(row[1])
    total_months += 1
    net_total += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Loop through the rows
    for row in csvreader:
        
        # Total number of months included in the dataset
        total_months += 1
        
        # Net amount of profit & losses
        net_total += int(row[1])

        # Change from the current month to the previous month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Greatest decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # Calculate the average & the date
    average_change = sum(monthly_change) / len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print financial analysis
print(f"------------------------------")
print(f"Financial Analysis")
print(f"------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# Specify the file to write to
output_file = os.path.join('.', 'Resources', 'budget_data_revised.text')

# Open the file using "write" mode
with open(output_file, 'w') as txtfile:

# Print out the new data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")