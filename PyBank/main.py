# Modules
import os
import csv


# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

#variables
total_months = 0
total_amount = 0
previous_p_l = 0
monthly_changes = []
greatest_inc = {"Date": "", "Amount": 0}
greatest_dec = {"Date": "", "Amount": 0}

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    for row in csvreader:
        date = row[0]
        p_l = int(row[1])
        
        
        total_months += 1
        total_amount += p_l
        
        if previous_p_l != 0:
            change = p_l - previous_p_l
            monthly_changes.append(change)
            
            if change > greatest_inc["Amount"]:
                greatest_inc["Date"] = date
                greatest_inc["Amount"] = change
            if change < greatest_dec["Amount"]:
                greatest_dec["Date"] = date
                greatest_dec["Amount"] = change
        
        previous_p_l = p_l

average_change = sum(monthly_changes)/ len(monthly_changes)


output = (
 "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_amount}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_inc['Date']} (${greatest_inc['Amount']})\n"
    f"Greatest Decrease in Profits: {greatest_dec['Date']} (${greatest_dec['Amount']})\n"
)
print(output)

with open(os.path.join("analysis", "result1.txt"), "w") as txtfile:
    txtfile.write(output)