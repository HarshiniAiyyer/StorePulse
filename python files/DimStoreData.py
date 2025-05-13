#import the necessary libraries
import pandas as pd
import random
from faker import Faker
import csv

#initialize
f = Faker()

#user input the number of rows the csv file shud have
numrows = int(input("Enter the number of rows for the csv file: "))
#input the name of the csv file 
csvfile = input("Enter the name of the csv file: ")

#details of the excel file
xlpath = r"D:\dwbi\ER.xlsx"
xlsheet = "storenames"
adj = "Adjective"
noun = "Nouns"

#fetch this sheet data in a dataframe
xldf = pd.read_excel(xlpath, sheet_name=xlsheet)

#open the csv file
with open(csvfile, "w", newline="") as file:
    writer = csv.writer(file)

#create the header
    header = ["StoreID", "StoreName", "StoreType", "StoreOpeningDate", 
              "Address", "City", "State", "Country", "Region", "ManagerName"]
    writer.writerow(header)

#generate multiple rows
    for i in range(numrows):
        ranadj = xldf['Adjectives'].sample(n = 1).values[0]
        rannoun = xldf['Nouns'].sample(n = 1).values[0]
        sname = f"The {ranadj} {rannoun}"
        print(sname)

#generate a single row
        row = [
            sname, random.choice(['Exclusive', 'MBO','SMB','Outlet Store']),
            f.date(),
            f.address().replace("/n"," ").replace(",",""),
            f.city(),
            f.state(),
            f.country(),
            random.choice(['North', 'South', 'East', 'West']),
            f.first_name()          
        ]
#write a row to the csv file
        writer.writerow(row)
#print succcess statement
print("Success!")
        




