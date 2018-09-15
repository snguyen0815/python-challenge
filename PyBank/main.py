# Import

import os
import csv

# File Location

csvpath = os.path.join("budget_data.csv")

# Default Read mode

with open(csvpath,newline="", encoding="utf-8") as budget:

# Store contents

    csvreader = csv.reader(budget, delimiter=",")

# Skip Header

    header = next(csvreader)

# Empty List

    total_months = []
    total_profit = []
    monthly_profit_change = []

# Stored file contents
    for row in csvreader:
      #Append total months    
            total_months.append(row[0])
            total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):

        # Difference between months
            monthly_profit_change.append(total_profit[i+1]-total_profit[i])

# Max & Min of monthly profit change
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# List and index from the max and min so it goes to the right month

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1


# Printing Statements for the homework

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

#Output

output = os.path.join("Financial_Analysis_Summary.txt")

with open(output, "w") as file:

# Print to Financial_Analysis_Summary

    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


    