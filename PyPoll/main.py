import os
import csv

pypoll_csv = os.path.join("election_data.csv")
output_file = os.path.join("PyPoll_Output.txt")

#PART 1: TOTAL VOTES
with open(pypoll_csv, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     header = next(csvreader)

     totalvotes = 0

     for row in csv.reader(csvfile):
         totalvotes += 1

#PART TWO: CANDIDATE RESULTS
with open(pypoll_csv, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     header = next(csvreader)
     
     #Creating lists for unique candidate names and adding a vote to each subsequent instance
     candidate_names = []
     candidate_votes = []
     for row in csv.reader(csvfile):
         candidate = (row[2])
         if candidate in candidate_names:
             list_of_candidates = candidate_names.index(candidate)
             candidate_votes[list_of_candidates] = candidate_votes[list_of_candidates] + 1
         else:
            candidate_names.append(candidate)
            candidate_votes.append(1)


sum_votes = candidate_votes[0]
number_votes = 0
percentage = []
for x in range(len(candidate_names)):
    #Looping "x" to get percentages
    percentage_votes = round(candidate_votes[x]/totalvotes*100, 3)
    percentage.append(percentage_votes)
    
election_winner = candidate_names[number_votes]

print()
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(totalvotes)}")
print("-------------------------")
for x in range(len(candidate_names)):
    print(f"{candidate_names[x]} : {percentage[x]}% ({candidate_votes[x]})")
print("-------------------------")
print(f"Winner: {election_winner}")
print("-------------------------")

with open(output_file, "w") as txt_file:
     txt_file.write("Election Results")
     txt_file.write("\n")
     txt_file.write("----------------------------------------")
     txt_file.write("\n")
     txt_file.write(f"Total Votes: {str(totalvotes)}")
     txt_file.write("\n")
     for x in range(len(candidate_names)):
         txt_file.write(f"{candidate_names[x]} : {percentage[x]}% ({candidate_votes[x]})")
     txt_file.write("\n")
     txt_file.write("-------------------------")
     txt_file.write("\n")
     txt_file.write(f"Winner: {election_winner}")
