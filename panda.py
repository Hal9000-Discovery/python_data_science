import pandas as pd

# reads the file candy.csv into a DataFrame
candy = pd.read_csv("data/candybars.csv")   # reads the CSV file into a DataFrame



#testing a push to git repository
print(candy.columns)                       # prints the column names of the DataFrame    

print("")
print(candy.shape)
print("")
print(candy.head(2))
print("")
print(candy.head())
print("")
print("")
print(candy)
print("")
print(candy.loc[5:10,'weight':'caramel'])
print("")

# prints the column names of the DataFrame
columns_candy = candy.columns               # gets the column names of the DataFrame
print(columns_candy)                        # prints the column names of the DataFrame

print("")
print("")
print(candy.head())                         # prints the first 5 rows of the DataFrame
print("")

print(candy.head(15))                       # prints the first 15 rows of the DataFrame
print(candy.loc[15:20])                     # prints rows from index 15 to 20
print("")

print(candy.loc[15:20,'weight':'caramel'])  # prints rows from index 15 to 20 and columns from 'weight' to 'caramel'
print("")
print(candy.loc[:6])                        # prints rows from the start to index 6





