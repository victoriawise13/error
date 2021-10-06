#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.


import csv
import os

csvfile = os.path.join("Resources","election_data.csv")

cand_list = {}


with open(csvfile) as f:
    reader = csv.reader(f, delimiter=",")

    header = next(reader)


    total_vote = 0
    for row in reader:
        total_vote += 1
        name = row[2]
        if name in cand_list:
            cand_list[name] += 1
        else:
            cand_list[name] = 1
    
cand_list["Khan Percent"] = round((cand_list["Khan"]/total_vote) * 100, 2)
cand_list["Correy Percent"] = round((cand_list["Correy"]/total_vote) * 100, 2)
cand_list["Li Percent"] = round((cand_list["Li"]/total_vote) * 100, 2)
cand_list["O'Tooley Percent"] = round((cand_list["O'Tooley"]/total_vote) * 100, 4)


cand_winner = max(cand_list, key=cand_list.get)

print("Election Results")
print(f'-------------------------')
print("Total Vote: " + str(total_vote))
print(f'-------------------------')
print("Khan: " + str(cand_list["Khan Percent"]) + "% " + str(cand_list["Khan"])) 
print("Correy: " + str(cand_list["Correy Percent"]) + "% " + str(cand_list["Correy"]))
print("Li: " + str(cand_list["Li Percent"]) + "% " + str(cand_list["Li"]))
print("O'Tooley: " + str(cand_list["O'Tooley Percent"]) + "% " + str(cand_list["O'Tooley"]))
print(f'-------------------------')
print("Winner: " + str(cand_winner))
print(f'-------------------------')


with open('analysis.txt', 'w') as text:
    text.write(f"\n")
    text.write("Election Results" + "\n")
    text.write(f'-------------------------' + "\n")
    text.write("Total Vote: " + str(total_vote) + "\n")
    text.write(f'-------------------------' + "\n")
    text.write("Khan: " + str(cand_list["Khan Percent"]) + "% " + str(cand_list["Khan"]) + "\n") 
    text.write("Correy: " + str(cand_list["Correy Percent"]) + "% " + str(cand_list["Correy"]) + "\n")
    text.write("Li: " + str(cand_list["Li Percent"]) + "% " + str(cand_list["Li"]) + "\n")
    text.write("O'Tooley: " + str(cand_list["O'Tooley Percent"]) + "% " + str(cand_list["O'Tooley"]) + "\n")
    text.write(f'-------------------------' + "\n")
    text.write("Winner: " + str(cand_winner) + "\n")
    text.write(f'-------------------------' + "\n")
