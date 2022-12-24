#Import Dependencies
import os
import csv

#Create path to election data
electionData = os.path.join("Resources/election_data.csv")

candidateList = []
finalCandidates= []
votePercent = []
voteCount= []
count = 0

#Open the csv file
with open(electionData, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    #Loop through all rows
    for row in csvreader:
        
        #Establish ticker
        count = count + 1
        
        #Gather list of candidates
        candidateList.append(row[2])
        
    #Organize votes per candidate
    for i in set(candidateList):
        finalCandidates.append(i)
        
        #Count total votes per candidate
        j = candidateList.count(i)
        voteCount.append(j)
        
        #Calculate percentage of votes per candidate
        x = round((j/count) * 100, 3)
        votePercent.append(x)
        
        
#Calculate total votes          
totalVotes = sum(voteCount)
    
#Determine index of highest percentage
winnerP = votePercent.index(max(votePercent))
    
#Indicate winner by matching index to finalCandidates list
winner = finalCandidates[winnerP]

#Print results
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------------------")
print(f"{finalCandidates[0]}: {votePercent[0]}% ({voteCount[0]})")
print(f"{finalCandidates[1]}: {votePercent[1]}% ({voteCount[1]})")
print(f"{finalCandidates[2]}: {votePercent[2]}% ({voteCount[2]})")
print("-------------------------------------")
print(f"Winner: {winner}")
print("-------------------------------------")

with open("electionResults.txt", "w") as text:
    text.write("Election Results" + "\n"  + "\n")
    text.write("-------------------------------------" + "\n" + "\n")
    text.write(f"Total Votes: {totalVotes}" + "\n" + "\n")
    text.write("-------------------------------------" + "\n" + "\n")
    text.write(f"{finalCandidates[0]}: {votePercent[0]}% ({voteCount[0]})" + "\n" + "\n")
    text.write(f"{finalCandidates[1]}: {votePercent[1]}% ({voteCount[1]})" + "\n" + "\n")
    text.write(f"{finalCandidates[2]}: {votePercent[2]}% ({voteCount[2]})" + "\n" + "\n")
    text.write("-------------------------------------" + "\n" + "\n")
    text.write(f"Winner: {winner}" + "\n" + "\n")
    text.write("-------------------------------------" + "\n" + "\n")

