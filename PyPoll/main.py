# Dependencies
import os
import csv
candidate_name_list = []
candidate_vote_list = []
candidate_index = 0
totalVoteCount = 0
csvpath = os.path.join(".", "Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        #check if candidate is in the name list
        totalVoteCount += 1
        try:
            candidate_index=candidate_name_list.index(row[2])
        except ValueError:
            # add candidate to list
            candidate_name_list.append(row[2])
            #add vote to candidate's vote list
            candidate_vote_list.append(1)
        else:
            candidate_vote_list[candidate_index] +=1

print("Election Results")
print("---------------------------------------")
print(f"Total Votes: {totalVoteCount}")
print("---------------------------------------")
candidate_index = 0
for candidate in candidate_name_list:
    candidate_vote_share = "{:.0%}".format(candidate_vote_list[candidate_index]/totalVoteCount)
    print(f"{candidate}: {candidate_vote_share} ({candidate_vote_list[candidate_index]})")
    candidate_index += 1
print("---------------------------------------")
maxVotes = max(candidate_vote_list)
candidate_index = candidate_vote_list.index(maxVotes)
print(f"Winner: {candidate_name_list[candidate_index]}")

print("---------------------------------------")