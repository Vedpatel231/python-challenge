# Modules
import os
import csv


# Set path for file
csvpath = os.path.join("Resources","election_data.csv")

#variables
total_votes = 0
candidate_votes = {}
winner = ""

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1


# print((candidate_votes.keys(), candidate_votes.values()))

#zip function to combine 2 list(votes and candidate name) with corresponding positions
winner = max(zip(candidate_votes.values(), candidate_votes.keys()))[1]


output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
# print(output)

for candidate, votes in candidate_votes.items():
    percent = (votes / total_votes) * 100
    output += f"{candidate}: {percent:.3f}% ({votes})\n"
    # print(output)

output += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

print(output)
with open(os.path.join("analysis","result2.txt"), "w") as txtfile:
    txtfile.write(output)