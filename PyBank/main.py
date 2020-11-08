import os
import csv

# Path to collect data from the Resources folder
budget_csv_path = os.path.join(".", "Resources", "budget_data.csv")

totalMonths = 0
netTotal = 0
AvgChange = 0.0

MostIncreaseAmt = 0
MostIncreaseMonth = "" 

MostDecreaseAmt = 0
MostDecreaseMonth = ""

with open(budget_csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        totalMonths += 1
        netTotal += float(row[1])
        if float(row[1])  > MostIncreaseAmt:
            MostIncreaseAmt = float(row[1])
            MostIncreaseMonth = row[0]
        if float(row[1]) < MostDecreaseAmt:
            MostDecreaseAmt = float(row[1]) 
            MostDecreaseMonth = row[0] 

            
#print to screen
AvgChange = "{:.2f}".format(netTotal/totalMonths)
netTotal = "{:.2f}".format(netTotal)
MostIncreaseAmt = "{:.2f}".format(MostIncreaseAmt)           
MostDecreaseAmt = "{:.2f}".format(MostDecreaseAmt)
print("Financial Analysis")  
print("------------------------------------------")
print(f"Total: ${netTotal}")
print(f"Average Change: ${AvgChange}")
print(f"Greatest Increase in Profits: {MostIncreaseMonth} (${MostIncreaseAmt})")
print(f"Greatest Decrease in Profits: {MostDecreaseMonth} (${MostDecreaseAmt})")
#output to file
output_path = os.path.join(".", "analysis", "BankAnalysis.txt")
text_file = open(output_path, "w")
text_file.write("Financial Analysis\n")
text_file.write("------------------------------------------\n")
text_file.write(f"Total: ${netTotal}\n")
text_file.write(f"Average Change: ${AvgChange}\n")
text_file.write(f"Greatest Increase in Profits: {MostIncreaseMonth} (${MostIncreaseAmt})\n")
text_file.write(f"Greatest Decrease in Profits: {MostDecreaseMonth} (${MostDecreaseAmt})\n")
#playing around
#with open("Output.txt", "w") as alt_text_file:
 #   print(f"Total: ${netTotal}", file=alt_text_file)



