# Dependencies
import os
import csv
import operator


file_input = "election_data.csv"

#define variables
total_votes = 0
winner_votes = 0
total_candidates = 0
#greatest_votes = ["", 0]
candidate_list= []
candidate_votes = {}

#open csv file 
with open(file_input) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
   
    csv_header= next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        #total_candidates = row[2]        

        #if candidate is not already in list, add candidate else, add vote to candidate tally
        if row[2] not in candidate_list:
            
            candidate_list.append(row[2])

            candidate_votes[row[2]] = 1
            
        else:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1
    
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(total_votes))
    print("-------------------------")
    
#calculate results
    
    for candidate in candidate_votes:
        percent_votes= ((candidate_votes[candidate]/total_votes)*100)
        print(candidate + ": " + str(round(percent_votes,3)) + "% " + "(" + str(candidate_votes[candidate]) +")")
        
# find winner by sorting dictionary in descending order 
winner = sorted(candidate_votes.items(), key=operator.itemgetter(1), reverse=True)

#results: print winner 
print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")

#output file as csv
file_output= os.path.join("election_analysis.csv")
with open(file_output, 'w', newline='') as csvfile:
    writer= csv.writer(csvfile)

    csvfile.write("Election Results")
    csvfile.write("\n")
    csvfile.write("-------------------------")
    csvfile.write("\n")
    csvfile.write("Total Votes " + str(total_votes))
    csvfile.write("\n")
    csvfile.write("-------------------------")
    for candidate in candidate_votes:
        percent_votes= ((candidate_votes[candidate]/total_votes)*100)
        csvfile.write("\n")
        csvfile.write(candidate + ": " + str(round(percent_votes,3)) + "% " + "(" + str(candidate_votes[candidate]) +")")
    csvfile.write("\n")
    csvfile.write("-------------------------")
    csvfile.write("\n")
    csvfile.write("Winner: " + str(winner[0]))
    csvfile.write("\n")
    csvfile.write("-------------------------")