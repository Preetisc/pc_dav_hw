import os
import csv


total_months=0
tot_pl =0
profit =0
grt_profit =0
get_profit_date =0
prev_profit =0

grt_loss =0
get_loss_date =0
prev_loss =0

percentage_change=0
percentage_change_avg=0
percentage_previous=0

os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join('','Resources','budget_data.csv')
print("\n"+ file_path)
with open(file_path,'r',newline='') as csvfiledata:
    csvrow =csv.reader(csvfiledata,delimiter=',')
    header = next(csvrow)
    #print(header)
    first_row=next(csvrow)
    total_months = 1
    tot_pl =float(first_row[1])
    prev_profit = float(first_row[1])
    prev_loss  = float(first_row[1])
    percentage_previous=float(first_row[1])
    #print("prev_profit  "+str(prev_profit))
    #print(first_row)
    for row in  csvrow:
        total_months += 1
        tot_pl += float(row[1])
        if ((float(row[1])-prev_profit) > grt_profit):
            #print(row )
            #print("prev_profit  "+str(prev_profit))
            grt_profit = float(row[1])-prev_profit
            #print("grt_profit "+str(grt_profit))
            get_profit_date=row[0]

        if ((float(row[1])-prev_loss) < grt_loss):
            #print(row )
            #print("prev_loss  "+str(prev_loss))
            grt_loss = float(row[1])-prev_loss
            #print("grt_loss "+str(grt_loss))
            get_loss_date=row[0]

        #percentage change
        percentage_change =float(row[1])-percentage_previous
        #print(" percentage_change ="+str(percentage_change))
        percentage_previous =float(row[1])
        percentage_change_avg += percentage_change
        prev_profit =float(row[1])
        prev_loss =float(row[1])
        #print("prev_profit  "+str(prev_profit))
       

    #for average percentage change sum of (currevt vale- previous value)/(total rows -1)
    percentage_change_avg =percentage_change_avg/(total_months -1)



output_path = os.path.join(".","Resources","Bank_Financial_Analysis.txt")

with open(output_path,'w',newline='') as writefile:
    write_lines = csv.writer(writefile)
    
    write_lines.writerow(["Financial Analysis"])
    write_lines.writerow(["----------------------------"])
    write_lines.writerow(["Total Months  : "+str(total_months)])      
    write_lines.writerow(["The net total amount of 'Profit/Losses' over the entire period  : "+str(tot_pl) ])
    write_lines.writerow(["The average of the changes in 'Profit/Losses' over the entire period : " + str(percentage_change_avg)])
    write_lines.writerow(["The greatest increase in profits (date and amount) over the entire period : "+get_profit_date+ "  " +str(grt_profit) ])
    write_lines.writerow(["The greatest increase in losses (date and amount) over the entire period : "+get_loss_date+ "  " +str(grt_loss) ])


    print("----------------------------")
    print("Total Months  : "+str(total_months)  )    
    print("The net total amount of 'Profit/Losses' over the entire period  : "+str(tot_pl) )
    print("The average of the changes in 'Profit/Losses' over the entire period : " + str(percentage_change_avg))
    print("The greatest increase in profits (date and amount) over the entire period : "+get_profit_date+ "  " +str(grt_profit) )
    print("The greatest increase in losses (date and amount) over the entire period : "+get_loss_date+ "  " +str(grt_loss) )    