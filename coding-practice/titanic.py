import pandas as pd

# Load the dataset
data = pd.read_csv('../data/titanic/train.csv')

# Display the first few rows to verify loading
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Fill missing values or drop rows/columns with missing values
data['Age'] = data['Age'].fillna(data['Age'].median())
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])
data = data.drop(columns=['Cabin'])  # Example of dropping a column with many missing values

# Convert data types if necessary
# Example: Convert the 'Survived' column to category
data['Survived'] = data['Survived'].astype('category')

# Verify changes
print ("Info about data after filling \n age NaN by avg age and \nembarked NaN by most common embarked \n and dropping cabin column which was not necessary")
print(data.info())

