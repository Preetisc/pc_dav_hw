import os
import csv

candidates=[]
votes=[]
per_votes=[]

os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join('','Resources','election_data.csv')
print("\n"+ file_path)
with open(file_path,'r',newline='') as csvfiledata:
    csvrow =csv.reader(csvfiledata,delimiter=',')
    header = next(csvrow)
    first_row=next(csvrow)
    total_voters = 1
    #tot_pl =float(first_row[1])
    #prev_profit = float(first_row[1])
    #prev_loss  = float(first_row[1])
    #percentage_previous=float(first_row[1])
    #print("prev_profit  "+str(prev_profit))
    #print(first_row)
    for row in  csvrow:
        total_voters += 1
        #tot_pl += float(row[1])
        if row[2] not in candidates:
            candidates.append(row[2])
            i = candidates.index(row[2])
            #print(i)
            votes.append("1")
        else:
            i = candidates.index(row[2])
            votes[i]=str(int(votes[i]) +1)

winner_index=0
winner_max = int(votes[0])
for i in votes:
    j = round((int(i )/total_voters *100),5)
    per_votes.append(str(j))
    if winner_max <= int(i):
        winner_index = votes.index(i)
        winner_max  = int(i)


#print(candidates)
#print(votes)
#print(per_votes)

print("Election Results")
print("-------------------------")
print("Total Votes: "+str(total_voters))
print("-------------------------")
for i  in range(0,len(candidates)):
    print(candidates[i] +" : "+ per_votes[i] +"% ("+ votes[i]+")")

print("-------------------------")
print("Winner: "+candidates[winner_index])
print("-------------------------")

output_path = os.path.join(".","Resources","Poll_Analysis.txt")
with open(output_path,'w',newline='') as writefile:
    write_lines = csv.writer(writefile)
    
    write_lines.writerow(["Financial Analysis"])   
    write_lines.writerow(["Election Results"])
    write_lines.writerow(["-------------------------"])
    write_lines.writerow(["Total Votes: "+str(total_voters)])
    write_lines.writerow(["-------------------------"])
    for i  in range(0,len(candidates)):
        write_lines.writerow([candidates[i] +" : "+ per_votes[i] +"% ("+ votes[i]+")"])

    
    write_lines.writerow(["-------------------------"])
    write_lines.writerow(["Winner: "+candidates[winner_index]+"hfg"])
    write_lines.writerow(["-------------------------"])     
