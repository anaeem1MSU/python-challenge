import csv
import os
pathtoload = "Resources/budget_data.csv"
Total_Profit = 0
Total_Months = 0
with open(pathtoload) as budget_data:
   file_reader = csv.reader(budget_data)
   header = next(file_reader)
   
   First_Date = next(file_reader)
   profit_list = []
   Months = []
   Monthly_Change = []
   Profit = int (First_Date[1]) 

   print(Profit)

   


   Total_Months = Total_Months + 1
   Total_Profit = Total_Profit + Profit
   for row in file_reader:
      Total_Months = Total_Months +1
      Total_Profit = Total_Profit + Profit
      
      profit_list.append(int(row["Profit/Losses"]) )

      Months.append(row["Date"])


      #Total_Profit.append(int(sum("profit_list")(row)))

   

     # Total_Profit = sum(profit_list)

   #for row in file_reader(len(Total_Profit)-1):
         #Monthly_Change.append(Total_Profit[row+1]-Total_Profit(row))

   #max_increase_value = max(Monthly_Change)
   #max_decrease_value = min(Monthly_Change)    

   #Best_month = Monthly_Change.index(max(Monthly_Change)) + 1
   #Worst_month = Monthly_Change.index(min(Monthly_Change)) + 1

print(Total_Months)
