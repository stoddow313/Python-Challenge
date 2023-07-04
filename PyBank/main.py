# Import dependencies
import os 
import csv

# Define variables 
month = []
profit_loss_changes = []
count_months = 0
net_profit_loss = 0
current_profit_loss = 0 
previous_profit_loss = 0
profit_loss_change = 0

# Path to data 
budget_data_csv = os.path.join('..', r'C:\Users\wstod\OneDrive\Desktop\Python-Challenge\PyBank\Resources\budget_data.csv')

# Open and read csv
with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csv_reader:
        count_months += 1

        current_profit_loss = int(row[1])
        net_profit_loss += current_profit_loss

        if (count_months == 1):

            previous_profit_loss = current_profit_loss
            continue

        else:

            profit_loss_change = current_profit_loss - previous_profit_loss

            month.append(row[0])

            profit_loss_changes.append(profit_loss_change)

            previous_profit_loss = current_profit_loss
    
    # Calculate net total profit loss, average change, greatest and smallest change, best/worst month.
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    greatest_change = max(profit_loss_changes)
    smallest_change = min(profit_loss_changes)

    highest_index = profit_loss_changes.index(greatest_change)
    lowest_index = profit_loss_changes.index(smallest_change)

    bestmonth = month[highest_index]
    worstmonth = month[lowest_index]

#Print to the terminal

print("Financial Analysis")
print("-------------------")
print(f"Total Months: {count_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_profit_loss}")
print(f"Greatest Profit Increase: {bestmonth} (${greatest_change})")
print(f"Greatest Profit Decrease: {worstmonth} (${smallest_change})")

# Export text file with results to Analysis folder

budget_file = os.path.join(r"C:\Users\wstod\OneDrive\Desktop\Python-Challenge\PyBank\Analysis\analysis.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("-------------------\n")
    outfile.write(f"Total Months: {count_months}\n")
    outfile.write(f"Total: ${net_profit_loss}\n")
    outfile.write(f"Average Change: ${average_profit_loss}\n")
    outfile.write(f"Greatest Profit Increase: {bestmonth} (${greatest_change})\n")
    outfile.write(f"Greatest Profit Decrease: {worstmonth} (${smallest_change})\n")