
import csv
import os

file_to_load = "budget_data.csv"
file_to_output = "budget_analysis.txt"

#defining
total_months = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0

# Read and convert it into a list 
with open(file_to_load) as revenue_data:
    
    #reader = csv.DictReader(revenue_data)
    
    reader = csv.reader(revenue_data)
    header = next(reader)
    firstrow = next(reader)
    total_months = total_months + 1
    prev_revenue = int(firstrow[1])
    total_revenue = total_revenue + int(firstrow[1])
    
    for row in reader:
        
        # The total
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])

        revenue_change = int(row[1]) - prev_revenue
        prev_revenue = int(row[1])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row[0]]

    # The greatest increase
        if revenue_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = revenue_change
    
    # The greatest decrease
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = revenue_change

            #Average Revenue Change
revenue_avg =  sum(revenue_change_list) / len(revenue_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print output
print(output)

# Explort to .txt
with open(file_to_output,"w") as txt_file:
    txt_file.write(output)

