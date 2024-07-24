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