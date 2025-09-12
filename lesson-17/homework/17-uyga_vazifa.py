import pandas as pd
import numpy as np

# Dataset
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# 1. Rename columns
df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)

# 2. Print first 3 rows
print("First 3 rows:\n", df.head(3))

# 3. Mean age
print("\nMean age:", df['age'].mean())

# 4. Select and print 'first_name' and 'City'
print("\nName and City:\n", df[['first_name', 'City']])

# 5. Add random Salary column
np.random.seed(42)  
df['Salary'] = np.random.randint(4000, 10000, size=len(df))
print("\nDataFrame with Salary:\n", df)

# 6. Summary statistics
print("\nSummary statistics:\n", df.describe())



# Dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(data)

# 1. Maximum sales and expenses
print("Max Sales:", sales_and_expenses['Sales'].max())
print("Max Expenses:", sales_and_expenses['Expenses'].max())

# 2. Minimum sales and expenses
print("Min Sales:", sales_and_expenses['Sales'].min())
print("Min Expenses:", sales_and_expenses['Expenses'].min())

# 3. Average sales and expenses
print("Average Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())

# Dataset
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses = pd.DataFrame(data)

# Set index to Category
expenses = expenses.set_index('Category')

# 1. Maximum expense per category
print("Max per Category:\n", expenses.max(axis=1))

# 2. Minimum expense per category
print("\nMin per Category:\n", expenses.min(axis=1))

# 3. Average expense per category
print("\nAverage per Category:\n", expenses.mean(axis=1))
