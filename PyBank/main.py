# The total number of months included in the dataset
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period



import csv
import os

csvfile = os.path.join("Resources","budget_data.csv")

totalmonths = []
total_months = 0
total_net = 0
monthly_change = 0
monthly_change_total = 0
initial_profit = 0
monthly_change_profit = []

with open(csvfile) as f:
    reader = csv.reader(f, delimiter=",")

    header = next(reader)


    for row in reader:
        print(row)
        total_months = total_months + 1
        totalmonths.append(row[0])
        total_net = total_net + int(row[1])

        profit_for_month = int(row[1])
        monthly_change=float(profit_for_month)
        monthly_change_total = monthly_change_total + monthly_change
        initial_profit = int(row[1])
        monthly_change_profit.append(monthly_change)
        max_profit = max(monthly_change_profit)
        min_profit = min(monthly_change_profit)
        max_index = (monthly_change_profit.index(max_profit))
        min_index = (monthly_change_profit.index(min_profit))
    

        
        average_change = round(total_net/total_months)


print(f'Financial Analysis')
print(f'------------------')
print (f"Total Months: {total_months}")
print (f"Total: {total_net}")
print (f"Average Change: {average_change}")
print (f'Greatest Increase in Profits: {totalmonths[max_index]} ${max_profit}')
print (f'Greatest Increase in Profits: {totalmonths[min_index]} ${min_profit}')


with open('analysis.txt', 'w') as text:
    text.write(f"\n")
    text.write(f"Financial Analysis"+ "\n")
    text.write(f"----------------------------------------------------------\n")
    text.write(f"Total Months: {total_months}" + "\n")
    text.write(f"Total: {total_net}" + "\n")
    text.write(f"Average Change: {average_change}" + "\n")
    text.write(f'Greatest Increase in Profits: {totalmonths[max_index]} ${max_profit}'+ "\n")
    text.write(f'Greatest Increase in Profits: {totalmonths[min_index]} ${min_profit}'+ "\n")



