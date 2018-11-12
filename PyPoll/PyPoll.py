import os
import csv
import numpy as np


row = []
row_count = 0
candidates = []
res =[]
perc = []

csvpath = os.path.join('./Resources/', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        row_count = row_count+1
        candidates.append(row[2])
        

        lst_cand = np.unique(candidates)

    for cand in lst_cand:
        perc = (list(candidates).count(cand)/row_count)
        z=[cand,list(candidates).count(cand),"{:.1%}".format(perc)]
        res.append(z)

    l = sorted(res, key=lambda st:st[1], reverse =True)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {row_count}")
print("-------------------------")
print(f"{l[0][0]}: {l[0][2]} ({l[0][1]})")
print(f"{l[1][0]}: {l[1][2]} ({l[1][1]})")
print(f"{l[2][0]}: {l[2][2]} ({l[2][1]})")
print(f"{l[3][0]}: {l[3][2]} ({l[3][1]})")
print("-------------------------")
print(f"Winner: {l[0][0]}")
print("-------------------------")

with open("output.txt", "w+") as output:
    output.write("Election Results\n")
    output.write("-------------------------\n")
    output.write(f"Total Votes: {row_count}\n")
    output.write("-------------------------\n")
    #output.write('\n'.join(lst_cand))
    output.write(f"{l[0][0]}: {l[0][2]} ({l[0][1]})\n")
    output.write(f"{l[1][0]}: {l[1][2]} ({l[1][1]})\n")
    output.write(f"{l[2][0]}: {l[2][2]} ({l[2][1]})\n")
    output.write(f"{l[3][0]}: {l[3][2]} ({l[3][1]})\n")
    output.write("-------------------------\n")
    output.write(f"Winner: {l[0][0]}\n")
    output.write("-------------------------\n")
