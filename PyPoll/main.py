# Import os and csv to read file paths and csv files
import os
import csv


# Import budget_data.csv
output_path = os.path.join('Resources', 'election_data.csv')
# print(output_path)
with open(output_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # First row are the headers Date and Profit/Losses
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # The headers are [0] = Ballot Id, [1] = County, [2] = Candidate

    # total amount of votes:
    t_votes = 0 #This will keep track of the vote counts
    l_candidates = {} # Initialized the dictionary to keep track of all the unique candidates that were voted and their total votes
    for r in csvreader:
        t_votes += 1
        if r[2] not in l_candidates:
            l_candidates[r[2]] = 0
        else:
            l_candidates[r[2]] = l_candidates[r[2]] + 1
    
    # Calculate each candidate's percentage of votes
    winner = "" # Initialize the winner variable which will hold the name of the winning candidate
    for c in l_candidates.keys():
        l_candidates[c] = [l_candidates[c], round(l_candidates[c]/t_votes*100, 3)]
        # Determine who the winner is
        if winner == "":
            winner = c
        else:
            if l_candidates[c][0] > l_candidates[winner][0]:
                winner = c
        

# Save the results as a string to display in the terminal and print to a text file
t_txt = f"Total Votes: {t_votes}"
w_txt = f"Winner: {winner}"
c_txt = (f"Charles Casper Stockham: {l_candidates['Charles Casper Stockham'][1]}% ({l_candidates['Charles Casper Stockham'][0]})\n"
f"Diana DeGette: {l_candidates['Diana DeGette'][1]}% ({l_candidates['Diana DeGette'][0]})\n"
f"Raymon Anthony Doane: {l_candidates['Raymon Anthony Doane'][1]}% ({l_candidates['Raymon Anthony Doane'][0]})")

display = ("Election Results\n----------------------\n"
f"{t_txt}\n----------------------\n{c_txt}\n----------------------\n{w_txt}\n----------------------")

print(display)
with open('./Analysis/election_results.txt', 'w') as file:
    writer = display
    file.write(writer)
    file.close()
