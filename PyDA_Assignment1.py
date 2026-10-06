import numpy as np

temp_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])

print("Shape of array :",temp_w1.shape)
print("Data type of array :",temp_w1.dtype)
print("No. of elements in array :",temp_w1.size)

fahrenheit = (temp_w1 * 9 / 5) + 32
print("Temperature in Fahrenheit :",fahrenheit)
print("Maximum F :",np.max(temp_w1))
print("Minimum F :",np.min(temp_w1))
print("Average F :",np.mean(temp_w1))

print("Temperature of first 3 days :",temp_w1[:3])
print("Temperature of last 2 days :",temp_w1[:-2])
print("Temperature of middle 3 days :",temp_w1[2:5])

temp_w1 = np.array([[22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],
                   [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]])
print("Shape of array :",temp_w1.shape)
print("Data type of array :",temp_w1.dtype)
print("No. of elements in array :",temp_w1.size)
print("Temperature of week1",temp_w1[0])
print("Temperature of week2",temp_w1[1])
print("Temperature of last 2 days of week1,2",temp_w1[:,-2:])

import pandas as pd

marks = pd.Series([95, 92, 89, 85, 80],
                index=['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5'])
print("Marks=",marks)

print("Rank 1:",marks.iloc[0])
print("Top 3 Ranks:",marks.loc[['Rank1','Rank2','Rank3']])
print("Rank 2:",marks.iloc[2])
print("Marks greater than 90:",marks[marks > 90])

marks.loc['Rank1'] = 100
marks = marks.drop('Rank5')

cgpa = marks/10
print("Updated marks:",marks)
print("CGPA :",cgpa)

transactions = pd.DataFrame({'TransID':[101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
                             'ProdCate':['Electronics', 'Clothing', 'Electronics', 'Furniture',
'Clothing', 'Electronics', 'Furniture', 'Clothing', 'Furniture', 'Electronics'],
                             'Region':['North', 'South', 'North', 'East', 'West', 'North', 'East', 'West',
'South', 'North'],
                             'Amount':[200, 150, 300, 450, 200, 250, 300, 180, 350, 400]})

print(transactions)
print(transactions.head())
print(transactions.tail())
print("Shape :",transactions.shape)
print("Data type of array :",transactions.dtypes)
print(transactions[['ProdCate','Amount']])
print(transactions.iloc[:-3])

print(transactions[(transactions['Region'] == 'North') &
                   (transactions['Amount'] > 200)])

print("Value counts for ProdCate :",transactions['ProdCate'].value_counts())
print("Unique values in Region :",transactions['Region'].unique())
print("Grouped by Region and its mean amount:",transactions.groupby('Region')['Amount'].mean())

transactions.loc[transactions['TransID'] == 102, 'Amount'] = 165

transactions['Discount'] = transactions['Amount']/10

transactions = transactions[transactions['TransID'] != 109]

transactions.drop('Discount', axis=1, inplace=True)

print(transactions)