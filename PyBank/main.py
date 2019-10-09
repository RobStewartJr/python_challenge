import os
import csv

pybank_csv = os.path.join("budget_data.csv")
output_file = os.path.join("PyBank_Output.txt")

#Total Months
with open(pybank_csv, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     header = next(csvreader)

     totalmonths = 0
     for row in csv.reader(csvfile):
         totalmonths += 1

#Total Income 
with open(pybank_csv, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     header = next(csvreader)

     totalincome = 0
     for row in csv.reader(csvfile):
         totalincome += int(row[1])

#Average Change
def Average(list):
    return sum(list)/len(list)

with open(pybank_csv, newline="") as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     header = next(csvreader)

     mtd_profit = []

     for column in csv.reader(csvfile):
         mtd_profit.append(column[1])
      
     pnl_change = []

     for index in range(1,len(mtd_profit)):
         pnl_change.append(int(mtd_profit[index])-int(mtd_profit[index-1]))        


print()
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {str(totalmonths)}")
print(f"Total: ${str(totalincome)}")
print(f"Average Change: ${str(Average((pnl_change)))}")
print("Greatest Increase in Profit: $" + str(max(pnl_change)))
print("Greatest Increase in Profit: $" + str(min(pnl_change)))

with open(output_file, "w") as txt_file:
     txt_file.write("Financial Analysis")
     txt_file.write("\n")
     txt_file.write("----------------------------------------")
     txt_file.write("\n")
     txt_file.write(f"Total Months: {str(totalmonths)}")
     txt_file.write("\n")
     txt_file.write(f"Total: ${str(totalincome)}")
     txt_file.write("\n")
     txt_file.write(f"Average Change: ${str(Average((pnl_change)))}")
     txt_file.write("\n")
     txt_file.write("Greatest Increase in Profit: $" + str(max(pnl_change)))
     txt_file.write("\n")
     txt_file.write("Greatest Increase in Profit: $" + str(min(pnl_change)))