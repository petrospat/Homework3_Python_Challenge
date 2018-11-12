#Your task is to create a Python script that analyzes the records to calculate each of the following:

import os
import csv
row_count = 0

csvpath = os.path.join('.\Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)pu
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
        row_count = row_count+1

#   The total number of months included in the dataset
print(f"Total Months: {row_count}")

#    The total net amount of "Profit/Losses" over the entire period

#   The average change in "Profit/Losses" between months over the entire period

#   The greatest increase in profits (date and amount) over the entire period

#   The greatest decrease in losses (date and amount) over the entire period