# Unit 3 | Assignment - Py Me Up, Charlie (PyPoll)

# Import dependencies
import os
import csv

# Initialize variables
vote_count = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Set the file path
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Open & read the CSV file
with open(csvpath, newline = '') as csvfile:

    # Initialize CSV reader
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # Skips reading the header
    csv_header = next(csvfile)

    # Loop through the rows
    for row in csvreader:
        
        # Total number of cast votes
        vote_count += 1
        
        # Total number of votes each candidate has won
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            
    # Percentage of votes each candidate has won
    kahn_percent = khan_votes / vote_count
    correy_percent = correy_votes / vote_count
    li_percent = li_votes / vote_count
    otooley_percent = otooley_votes / vote_count
    
    # Winner of the election based on the popular vote
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# Print election analysis
print(f"Election Results")
print(f"------------------------------")
print(f"Total Votes: {vote_count}")
print(f"------------------------------")
print(f"Kahn: {kahn_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"------------------------------")
print(f"The Winner is: {winner_name}")
print(f"------------------------------")

# Specify the file to write to
output_file = os.path.join('.', 'Resources', 'election_data_revised.text')

# Open the file using "write" mode
with open(output_file, 'w') as txtfile:

# Print out the new data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {vote_count}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {kahn_percent:.3%} ({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%} ({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%} ({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%} ({otooley_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")