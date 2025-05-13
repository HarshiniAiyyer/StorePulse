#import the necessary libraries
import csv
import random
from faker import Faker

#initialize
f = Faker()


#user input the number of rows the csv file shud have
numrows = int(input("Enter the number of rows the csv shud have"))


#input the name of the csv file 
csvfile = input("Enter the file name pls")

#open the csv file

with open(csvfile, mode = 'w', newline = '') as file:
    writer = csv.writer(file)   

#create the header
    header = ['CustomerID', 'FirstName', 'LastName', 'Gender', 'DOB', 'Email', 'Address', 'City', 'State', 'ZipCode', 'LoyaltyInfoID']


    writer.writerow(header)

#generate multiple rows

    for _ in range(numrows):
        row = [
            f.first_name(),
            f.last_name(),
            random.choice(['M','F','Others','Not Specified']),
            f.date(),
            f.email(),
            f.phone_number(),
            f.address().replace(","," ").replace("\n",""),
            f.city(),
            f.state(),
            f.postcode(),
            random.randint(1,5)
        ]
        
        writer.writerow(row)


#generate a single row


#write a row to the csv file

#print succcess statement
print("Success!")