

import os 
import csv

file_input= os.path.join("budget_data.csv")


# Variables to Track
total_months = 0
net_amount = 0
prev_amount = 0
amount_change = 0
amount_changes = []
date_list=[]


with open (file_input, newline="") as csvfile: 
    csvreader= csv.reader(csvfile, delimiter=",")
   
    csv_header= next(csvreader)
    
    # Loop through all the rows of data in file 
    
    for row in csvreader:

        # use a counter to track the number of rows through loops == number of months
        total_months = total_months + 1
        
        #use a counter to add the amount in each for of position 1 ("Profit/Losses") in the list
        net_amount = net_amount + int(row[1])
        
        # Keep track of changes
        # amount change from current row minus the amount from previous ruun from loop
        amount_change = int(row[1]) - prev_amount
        #print(amount_change)

        # Reset the  prev_amount value to the value of the current cell. To be reference in  amount change
        prev_amount = int(row[1])
        #print(prev_amount)
        

        # Append  the amount_changes to amount_chnages list and the months to the date_list list
        
        amount_changes.append(amount_change)
        date_list.append(row[0])

    # find the amount average
    amount_total= sum(amount_changes[1:])
    amount_length= len(amount_changes[1:])
    
    amount_avg = amount_total / amount_length
    
    # find the maximum amount changes from the amount_changes list 
    max_chg = max(amount_changes)
    
    # find the minimum amount chang from the amount_changes list
    min_chg= min(amount_changes)

    #find the index position of the amount_changes max and min (use to find corresponding months)

    max_chgindex= amount_changes.index(max_chg)
    min_chgindex= amount_changes.index(min_chg)

    #use index of max and min amount_changes to return corresponding dates from date_List 
    max_date= date_list[max_chgindex]
    min_date= date_list[min_chgindex]

    #print outputs
    print("                  ")
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total amount: " + "$" + str(net_amount))
    print("Average Change: " + "$" + str(round(amount_avg,2)))
    print("Greatest Increase in Profits: " + str(max_date) + " ($" + str(max_chg) + ")") 
    print("Greatest Decreasein Profits: " +  str(min_date) + " ($" +  str(min_chg) + ")")
    
#output file as csv
file_output= os.path.join("budget_analysis.csv")
with open(file_output, 'w', newline='') as csvfile:
    writer= csv.writer(csvfile)
    
    csvfile.write("Financial Analysis")
    csvfile.write("\n")
    csvfile.write("-------------------------")
    csvfile.write("\n")
    csvfile.write("Total Months: " + str(total_months))
    csvfile.write("\n")
    csvfile.write("Total amount: " + "$" + str(net_amount))
    csvfile.write("\n")
    csvfile.write("Average Change: " + "$" + str(round(amount_avg,2)))
    csvfile.write("\n")
    csvfile.write("Greatest Increase in Profits: " + str(max_date) + " ($" + str(max_chg) + ")")
    csvfile.write("\n") 
    csvfile.write("Greatest Decreasein Profits: " +  str(min_date)+ " ($" +  str(min_chg) + ")")
