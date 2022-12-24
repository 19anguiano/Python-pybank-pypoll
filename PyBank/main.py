#Import modules

import os
import csv

#Create path to budget csv

csv_pybank = os.path.join("Resources/budget_data.csv")


profit = []
mChanges = []
months = []


count = 0
totalProfit = 0
tProfitChange = 0
firstProfit = 0

#Open csv

with open(csv_pybank, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
  
    #Use for loop to go through rows
    for row in csvreader:
        
        #Establish ticker
        count = count + 1
        
        #Add values to months list
        months.append(row[0])
        
        #Add values to profit list and calculate total profit
        profit.append(row[1])
        totalProfit = totalProfit + int(row[1])
        
        #Define next month's profit, as well as monthly changes in profit
        nextProfit = int(row[1])
        monthlyProfitChange = nextProfit - firstProfit
        
        #Add monthly changes in profit to mChanges list
        mChanges.append(monthlyProfitChange)
        
        #Set firstProfit to next cell
        firstProfit = nextProfit
        

#Calculate total change in profits/losses. Exclude first index
tProfitChange = sum(mChanges[1:])
        
#Calculate number of changes in profits/losses
nChanges = count - 1
        
#Calculate average change in profits 
averageProfitChange = round((tProfitChange / nChanges), 2)
        
#Find max and min in mChanges
greatest_increase = max(mChanges)
greatest_decrease = min(mChanges)
    
#Find months for max and min above
increase_month = months[mChanges.index(greatest_increase)]
decrease_month = months[mChanges.index(greatest_decrease)]


print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {count}")

print(f"Total: ${totalProfit}")

print(f"Average Change: ${averageProfitChange}")

print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")


#Export text file to Analysis folder

with open("financialAnalysis.txt", "w") as text:
    text.write("Financial Analysis" + "\n")
    text.write("---------------------------------" + "\n")
    text.write(f"Total Months: {count}" + "\n")
    text.write(f"Total: ${totalProfit}" + "\n")
    text.write(f"Average Change: ${averageProfitChange}" + "\n")
    text.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})" + "\n")
    text.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})" + "\n")


#Note to grader: I'm not sure why it doesn't run in VS Code. It gives me "[Errno 2] No such file or directory: 'Resources\\budget_data.csv"  
#It executed perfectly in Jupyter Notebooks and Git Bash.