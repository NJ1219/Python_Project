# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path
Path.cwd()

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list

with open(menu_filepath, 'r') as menufile:
    csvreader=csv.reader(menufile, delimiter=',')
    
    header = next(csvreader)
    print(f"{header}, 'profit'")
 # to directly create list of lists menu =list(csvreader)
 # to print the csv file as list  print(menu)
    for line in csvreader:
       # To view the contents of the csvfile print(line)
        
        
        item = line[0]
        category= line[1]
        description= line[2]
        price= float(line[3])
        cost= float(line[4])
    # @TODO: Calculate profit of each item in the menu data
        profit = price - cost
        
        line.append(profit)
        menu.append(line)
        
       
        
 #to print the menu list of lists   
    print(menu)
    print("\n")
    




# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0



# @TODO: Read in the sales data into the sales list

with open(sales_filepath, 'r') as salesfile:
    csvreader=csv.reader(salesfile, delimiter=',')
    
    header = next(csvreader)
    print(header)
 
    for line in csvreader:
         # To view the contents of the csvfile print(line)
        
     # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
   
        line_num = int(line[0])
        date= line[1]
        cc_num= int(line[2])
        quantity= float(line[3])
        menu_item= line[4]
        sales.append(line)
        
 #   print(sales[:10])



    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
        if menu_item not in report.keys():
            report[menu_item] = {"01-count": quantity, "02-revenue" :price * quantity, "03-cogs": quantity * cost, "04-profit": quantity * profit}
        else:
            report[menu_item]["01-count"] += quantity
            report[menu_item]["02-revenue"] += price* quantity
            report[menu_item]["03-cogs"] += cost * quantity
            report[menu_item]["04-profit"] += profit * quantity
        
    for a, b in report.items():
        print (a,b)
            
      
# output file with metrics
output_path = Path("../../PyRamen/PyRamen.txt")
    
with open(output_path, 'w') as file:
    file.write("Report for PyRamen.\n")
    for key in report:
        file.write(f"{key} {report[key]} \n")
    

    # @TODO: For every row in our sales data, loop over the menu records to determine a match


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables

cogs = 0
revenue = 0

    
        

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
   # for key, values in report.items():
    #    for item in menu:
            
     #       if key == item[0]:
      #          report[menu_item] = {'01-count': quantity, '02-revenue': quantitiy*price, '03-cogs':quantity*cost, '04-profit':quantity*profit}
                # if menu_item not in report.keys():
               #     report[menu_item] = {"01-count": quantity}
               # else:
               #     report[menu_item]["01-count"] += quantity
                
                 
       #         report[key] = {'01-count': quantity, '02-revenue': quantity*item[], '03-cogs':quantity*cost, '04-profit':quantity*profit}
                             
        #    else:
         #       continue
            
            
               
   # print (report)
            
           
            

            # @TODO: Print out matching menu data






            # @TODO: Cumulatively add up the metrics for each item key





        # @TODO: Else, the sales item does not equal any of the item in the menu data, therefore no match



    # @TODO: Increment the row counter by 1


# @TODO: Print total number of records in sales data




# @TODO: Write out report to a text file (won't appear on the command line output)
