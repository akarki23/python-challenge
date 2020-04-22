# Data Analysis Bootcamp Assignment 3: Py Me Up, Charlie (PyBank)

# Import dependencies
import os
import csv

# Set the file path
input_file = os.path.join('.', 'Resources', 'budget_data.csv')

# Define a function to analyze the data
def financial_analysis(data):

    # Initialize variables
    months_count = 0
    profit = 0
    months = []
    profit_months = 0
    change = 0
    changes = []
    
    # Loop through rows
    for row in data:
       
        # Increment the count of months
        months_count = months_count + 1

        # Increment profit
        profit = profit + int(row[1])
        
        # Append each month into months
        months.append(str(row[0]))
        
        # If there is previous data
        if change != 0:
            
            # Set profit
            profit_months = int(row[1])

            # Calculate change
            change = profit_months - change
            
            # Append each change into changes
            changes.append(change)
            change = int(row[1])
            
        # No previous data *applies once for the first row
        elif change == 0:
            change = int(row[1])  
            
    # Remove 1st month from months since there is no change
    months.pop(0)
    
    # Greatest increase in profits
    maximum = changes.index(max(changes))

    # Greatest decrease in profits
    mimimum = changes.index(min(changes))

    # use index positions to find the month that corresponds with max and min values from the changeList
    max_change = (months[int(maximum)], max(changes))
    min_change = (months[int(mimimum)], min(changes))
    
    # take average of the changeList
    average = sum(changes) / float(len(changes))
    average = round(average, 2)
    
    # print the results
    print(f'Financial Analysis')
    print(f'-------------------------------------------')
    print(f'Total Months: {months_count}')
    print(f'Total: ${profit}')
    print(f'Average Change: ${average:.2f}')
    print(f'Greatest Increase in Profits: {max_change}')
    print(f'Greatest Loss In Profits: {min_change}')

    # Set the file to write to
    output_file = os.path.join('.', 'Output', 'budget_data_revised.txt')    
    
    # Write the results to a text file
    with open(output_file, 'w') as writetxt:
        writetxt.write('Financial Analysis')
        writetxt.write('\n------------------------------------')
        writetxt.write(f'\nTotal Months: {months_count}')
        writetxt.write(f'\nTotal: ${profit}')
        writetxt.write(f'\nAverage Change: ${average:.2f}')
        writetxt.write(f'\nGreatest Increase In Profits: {max_change}')
        writetxt.write(f'\nGreatest Loss In Profits: {min_change}')

# Open & read the file
with open(input_file, 'r', newline='') as csvfile:

    # Initialize CSV reader
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    
    # Call the function with the file as it's parameter
    financial_analysis(csvreader)