# Import Dependencies

import os 
import csv
import collections
from collections import Counter

# Define variables 

voters_candidates = []
voters_per_candidate = []

# Path to data file 

election_data = os.path.join("..", r"C:\Users\wstod\OneDrive\Desktop\Python-Challenge\PyPoll\Resources\election_data.csv")

with open(election_data) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    for row in csv_reader:

        voters_candidates.append(row[2])

    sorted_list = sorted(voters_candidates)

    arrange_list = sorted_list

    count_candidate = Counter(arrange_list)
    voters_per_candidate.append(count_candidate.most_common())

    for item in voters_per_candidate:

        first = format((item[0][1])*100/(sum(count_candidate.values())), '.3f')
        second = format((item[1][1]*100)/(sum(count_candidate.values())), '.3f')
        third = format((item[2][1]*100)/(sum(count_candidate.values())), '.3f')

#Print analysis to terminal

print("Election Results")
print("-----------------")
print(f"Total Votes: {sum(count_candidate.values())}")
print("-----------------")
print(f"{voters_candidates[0][0][0]}: {first}% ({voters_per_candidate[0][0][1]})")
print(f"{voters_candidates[0][1][0]}: {second}% ({voters_per_candidate[0][1][1]})")
print(f"{voters_candidates[0][2][0]}: {third}% ({voters_per_candidate[0][2][1]})")
print("-----------------")
print(f"Winner: {voters_per_candidate[0][0][0]}")
print("-----------------")

# Export text file with results
election_file = os.path.join(r"C:\Users\wstod\OneDrive\Desktop\Python-Challenge\PyPoll\Analysis\analysis.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-----------------\n")
    outfile.write(f"Total Votes: {sum(count_candidate.values())}\n")
    outfile.write("-----------------\n")
    outfile.write(f"{voters_candidates[0][0][0]}: {first}% ({voters_per_candidate[0][0][1]})\n")
    outfile.write(f"{voters_candidates[0][1][0]}: {second}% ({voters_per_candidate[0][1][1]})\n")
    outfile.write(f"{voters_candidates[0][2][0]}: {third}% ({voters_per_candidate[0][2][1]})\n")
    outfile.write("-----------------\n")
    outfile.write(f"Winner: {voters_per_candidate[0][0][0]}\n")
    outfile.write("-----------------\n")