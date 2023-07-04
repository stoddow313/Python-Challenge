# Import Dependencies

import os 
import csv
import collections


# Define variables 

total_votes = []
votes_per_candidate = ()
output = '''Election Results
-------------------------
Total Votes: '''

# Path to data file 

election_data = os.path.join("..", r"C:\Users\wstod\OneDrive\Desktop\Python-Challenge\PyPoll\Resources\election_data.csv")

with open(election_data) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    for row in csv_reader:
    
        total_votes.append(row[2])

# Calculate total votes, candidate votes, and percentage
total_count = len(total_votes)
output = output + str(total_count) + "\n" + "-----------------" + "\n"
candidates = list(set(total_votes))
votes_per_candidate = []
percentage = []

for candidate in candidates:
    votes_per_candidate.append(total_votes.count(candidate))

for i in range(len(candidates)):
    percentage = votes_per_candidate[i]/total_count*100
    output = output + f'{candidates[i]}: {round(percentage, 3)}% ({votes_per_candidate[i]}) \n'

# Find winner, and print results 
winner_index = votes_per_candidate.index(max(votes_per_candidate))
output = output + f"--------------------\nWinner: {candidates[winner_index]}\n----------------"

print(output)
csvpath = os.path.join("..",r"C:\Users\wstod\OneDrive\Desktop\Python-Challenge\PyPoll\Analysis\analysis.txt")
with open(csvpath, 'w') as textfile:
    textfile.write(output)