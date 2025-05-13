 ## Using only last day's sales data to store in the OLTP database

DATEID = '20241230'

landing = r"D:\dwbi\landing"

import pandas as pd
import numpy as np
import random
import datetime
import os



for i in range(1,101):
    numrows = np.random.randint(100,1000)

    data = {
    'DateID':[DATEID] * numrows,
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

    #dynamic filename
    filename = f"Store_{i}_{DATEID}.csv"

    filepath = os.path.join(landing, filename)

    #if file exists, delete it and write a new one

    if os.path.exists(filepath):
        os.remove(filepath)

    df.to_csv(filepath, index = False)

#print success message
print("Success!")

