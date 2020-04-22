# Data Analysis Bootcamp Assignment 3: Py Me Up, Charlie (PyPoll)

# Import dependencies
import os
import csv

# Initialize variables
total_votes = 0
votes = []
count = []
candidates = []
percent_votes = []

# Set the file path
input_file = os.path.join('.', 'Resources', 'election_data.csv')

# Open & read the file
with open(input_file, newline = '') as csvfile:

    # Initialize CSV reader
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvfile)

    # Loop through the rows
    for row in csvreader:
        
        # Increment the total number of votes cast
        total_votes = total_votes + 1
        
        # Append the list of unique candidates
        if row[2] not in candidates:
            candidates.append(row[2])
        
        # Append the list of votes
        votes.append(row[2])
    
    # Loop through candidates
    for candidate in candidates:
        count.append(votes.count(candidate))
        percent_votes.append(round(votes.count(candidate) / total_votes * 100, 3))
    
    # Determine winner based on whoever has the most votes
    election_winner = candidates[count.index(max(count))]

    # Print election analysis
    print(f"Election Results")
    print(f"------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"------------------------------")
    for i in range(len(candidates)):
        print(f'{candidates[i]}: {percent_votes[i]}% {count[i]}')
    print(f"------------------------------")
    print(f"The Winner is: {election_winner}")
    print(f"------------------------------")

    # Specify the file to write to
    output_file = os.path.join('.', 'Output', 'election_data_revised.text')

    # Open the file using "write" mode
    with open(output_file, 'w') as writetxt:
        # Print out the new data
        writetxt.write(f"Election Results\n")
        writetxt.write(f"---------------------------\n")
        writetxt.write(f"Total Votes: {total_votes}\n")
        writetxt.write(f"---------------------------\n")
        for i in range(len(candidates)):
            writetxt.write(f'{candidates[i]}: {percent_votes[i]}% {count[i]}\n')
        writetxt.write(f"---------------------------\n")
        writetxt.write(f"Winner: {election_winner}\n")
        writetxt.write(f"---------------------------\n")