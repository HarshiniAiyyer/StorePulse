#importing pandas
import pandas as pd

#choose start and end date
start_date = '2014-01-01'
end_date = '2024-12-31'

#generate date range
date_range = pd.date_range(start = start_date, end = end_date)
print(date_range)

#convert these dates to a dataframe
datedf = pd.DataFrame(date_range, columns = ['Date'])
print(datedf)

#add new columns to our dataframe
datedf['DayofWeek'] = datedf['Date'].dt.dayofweek
datedf['Month'] = datedf['Date'].dt.month
datedf['Year'] = datedf['Date'].dt.year
datedf['Quarter'] = datedf['Date'].dt.quarter
datedf['isWeekend'] = datedf['DayofWeek'].isin([5,6])
datedf['DateID'] = datedf['Date'].dt.strftime('%Y%m%d').astype(int)

#reorder data so that dateid becomes the first column
datedf = datedf[['DateID', 'Date', 'DayofWeek', 'Month', 'Year', 'Quarter', 'isWeekend']]
print(datedf)

#save the dataframe to a csv file
datedf.to_csv('DimDate.csv', index = False)

#print success message
print("Success!")



