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
    l_candidates = [] # Initialized the list to keep track of all the unique candidates that were voted
    for r in csvreader:
        # print(1)
        t_votes += 1
        if len(l_candidates) > 0:

            for l_r in range(0, len(l_candidates)):
                if r[2] != l_candidates[l_r]:
                    l_candidates.append(r[2])
        else: l_candidates.append(r[2])
    
print(t_votes)
print(l_candidates)
