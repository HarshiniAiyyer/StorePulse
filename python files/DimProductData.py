#import the necessary libraries
import pandas as pd
import random
import csv




#user input the number of rows the csv file shud have
numrows = int(input("Enter the number of rows for the csv file: "))
#input the name of the csv file 
csvfile = input("Enter the name of the csv file: ")

#details of the excel file
xlpath = r"D:\dwbi\LookupFile.xlsx"

#raw product data sheet
prodsheet = "Raw Product Names"
prodcol = "Product Name"

#category data sheet
catsheet = "Product Categories"
catcol = "Category Name"


#fetch this sheet data in a dataframe
prodf = pd.read_excel(xlpath, sheet_name=prodsheet)
catdf = pd.read_excel(xlpath, sheet_name=catsheet)

#open the csv file
with open(csvfile, "w", newline="") as file:
    writer = csv.writer(file)

#create the header
    header = ["ProductName", "Category", "BrandName", "UnitPrice"]

    writer.writerow(header)

#generate multiple rows
    for i in range(numrows):
        

#generate a single row
        row = [

            prodf['Product Name'].sample(n = 1).values[0], #random product name
            catdf['Category Name'].sample(n = 1).values[0], #random category name
            random.choice(['UrbanAura', 'LuxeGlow', 'Ethereal Edge',
                           'VelvetVista', 'ZenithStyle']),
            random.randint(100, 1000)        
        ]
#write a row to the csv file
        writer.writerow(row)
#print succcess statement
print("Success!")