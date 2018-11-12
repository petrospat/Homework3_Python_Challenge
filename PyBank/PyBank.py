import os
import csv


csvpath = os.path.join('./Resources/', 'budget_data.csv')
row = []
row_count = 0
sum = 0
delta = 0
delta_sum = 0
lista = []

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    keep_value = 867884
    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        
        delta = int(row[1]) - keep_value     
        row_count = row_count+1
        sum = sum + int(row[1])
        delta_sum = delta_sum + delta
      
        keep_value = int(row[1])
        lista.append(row)

total = delta_sum/(int(row_count)-1)       
max_value =max(lista, key=lambda item: int(item[1]))
min_value =min(lista, key=lambda item: int(item[1]))



with open("output.txt", "w+") as output:
   
    print("Financial Ananlysis")
    output.write("Financial Ananlysis\n")
    print("----------------------------")
    output.write("----------------------------\n")
    print(f"Total Months: {row_count}")
    output.write(f"Total Months: {row_count}\n")
    print(f"Total Net Amount of profit/Losses: ${sum}")
    output.write(f"Total Net Amount of profit/Losses: ${sum}\n")
    print(f"Average Change: ${total}")
    output.write(f"Average Change: ${total}\n")
    print(f"Greatest Increase in Profits: {max_value[0]} (${max_value[1]})")
    output.write(f"Greatest Increase in Profits: {max_value[0]} (${max_value[1]})\n")
    print(f"Greatest Decrease in Profits: {min_value[0]} (${min_value[1]})")
    output.write(f"Greatest Decrease in Profits: {min_value[0]} (${min_value[1]})\n")

