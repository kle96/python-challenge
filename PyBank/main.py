# Import os and csv to read file paths and csv files
import os
import csv

# Import budget_data.csv
output_path = os.path.join('Resources', 'budget_data.csv')
# print(output_path)
with open(output_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # First row are the headers Date and Profit/Losses
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Initiate aggregated variables
    total_month = 0
    net_income = 0
    chng = 0
    chng_income = []
    p_row = 0 # this will be the profit/loss from the previous data row
    sum_change = 0 # this is used to calculate the total change in income for calculating the average
    avg_chng_income = 0

    g_incr = []
    g_decr = []
    for row in csvreader:
        total_month += 1
        net_income += int(row[1])
        chng = (int(row[1])-p_row)
        sum_change += chng
        p_row = int(row[1])

        chng_income.append([row[0], chng])

# Greatest Increase 
g_r = 0 # this is the row index with the greatest increase
g_d_r = 0 # this is the row index with the greatest decrease
avg_change = 0
for r in range(1, len(chng_income)):
    avg_change += chng_income[r][1]
    if chng_income[r][1] > chng_income[g_r][1]:
        g_r = r
    elif chng_income[r][1] < chng_income[g_d_r][1]:
        g_d_r = r

print(f"Total Months: {total_month}")
print(f"Total: ${net_income}")
print(f"Average Change: ${avg_change/len(chng_income)}")
print(f"Greatest increase: {chng_income[g_r][0]} (${chng_income[g_r][1]})")
print(f"Greatest decrease: {chng_income[g_d_r][0]} (${chng_income[g_d_r][1]})")