import pandas as pd
import numpy as np
import random
import datetime


numrows = int(input("Enter the number of rows to generate: "))

#generate random dates
dateseries = np.random.choice(
    np.arange(np.datetime64('2014-01-01'), np.datetime64('2024-12-31')), 
    size=numrows
)

formatrows = pd.to_datetime(dateseries).strftime('%Y-%m-%d')
print(formatrows)

data = {
    'DateID':formatrows,
    'ProductID': np.random.randint(1,1001, size = numrows),
    'StoreID': np.random.randint(1,101, size = numrows),
    'CustomerID' : np.random.randint(1,1001, size = numrows),
    'QuantityOrdered' : np.random.randint(1,21, size = numrows),
    'OrderAmount' : np.random.randint(100,1001, size = numrows),
}

df = pd.DataFrame(data)
#df.head()

discperc = np.random.uniform(0.02, 0.15, size = numrows)
shippingcost = np.random.uniform(0.05, 0.15, size = numrows)

df['DiscountAmount'] = df['OrderAmount'] * discperc
df['ShippingCost'] = df['OrderAmount'] * shippingcost

df['TotalAmount'] = df['OrderAmount'] - (df['DiscountAmount'] + df['ShippingCost'])

print(df.head(5))

df.to_csv('factorders.csv', index = False)

#print success message
print("Success!")

