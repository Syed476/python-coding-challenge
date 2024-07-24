# Pandas

import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)

# Basic operations
print ("Here is the complete dataframe")
print(df.head())

# print(df.info())
# print(df.describe())


print ("Here is the filtered dataframe based on age greater than 30")
filtered_df = df[df['Age'] > 30]
print(filtered_df)

# List comprehension
print ("Here is list of even integers in the range of 10")
filtered_list = [x for x in range(10) if x % 2 == 0]
print(filtered_list)

# Pandas
sorted_df = df.sort_values('Age', ascending=False)
print ("Here is the sorted df based on age dsc")
print (sorted_df)

# List
sorted_list = sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
print ("Here is sorted list of number from a given list")
print (sorted_list)

# Pandas
grouped = df.groupby('City')['Age'].mean()
print ("Here is df mean age grouped by City ")
print (grouped)

# Using itertools
from itertools import groupby
data = [('A', 1), ('B', 2), ('A', 3), ('B', 4)]
grouped = {k: list(v for _, v in g) for k, g in groupby(sorted(data), key=lambda x: x[0])}
print ("The code groups the tuples in data by \ntheir first element and collects the second elements \nof these tuples into lists, resulting in a dictionary where the keys \nare the unique first elements from the tuples, and the values are lists of the \ncorresponding second elements.")
print (grouped)