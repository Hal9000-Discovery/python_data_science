"""
File Name: M2_Table_Manipulation_and_Chaining.py
Author: David Sanghara
Date Created: 2025-09-08
p
Description :
A script to show the basics of Data Science
M1. Python & Pandas - An unexpected Friendship

License:

"""


# Import pandas library
#from hashlib import sha1
#import test_assignment2 as t
import pandas as pd
#import altair as alt


#################################################
print('-------------------------')
print('Dataframes')
print('-------------------------')
print('')
################################################

# reads the file candy.csv into a DataFrame
candy = pd.read_csv("data/candybars.csv")   # reads the CSV file into a DataFrame
#print(candy.head())                                   # prints the first 5 rows of the DataFrame
print("")

#Read in the data
hockey_players = pd.read_csv("data/projections_20202021.csv")   # reads the CSV file into a DataFrame
print(hockey_players)
#print(hockey_players .head())                                   # prints the first 5 rows of the DataFrame
print("")


#################################################
print('-------------------------')
print('Filtering Data')
print('-------------------------')
print('')
################################################

print('position == C')
hockey_players_filtered = hockey_players[hockey_players['position'] == 'C']  # Filters the DataFrame to include only rows where the 'position' column is 'C'
print(hockey_players_filtered)  
print("")


print('goals > 24')
goals_over_24 = hockey_players[hockey_players['goals'] > 24]  # Filters the DataFrame to include only rows where the 'goals' column is greater than 20
print(goals_over_24)    

print("")

print('goals > 20 and age < 30')
goals_over_20_and_under_30 = hockey_players[(hockey_players['goals'] > 20) & (hockey_players['goals'] < 30)]  # Filters the DataFrame to include only rows where the 'goals' column is greater than 20 and 'age' column is less than 30
print(goals_over_20_and_under_30)  
print("")


print("goals > 20 and age < 30 and position == 'C'")
print('Using a mask')
mask = (hockey_players['goals'] > 20) & (hockey_players['goals'] < 30) & (hockey_players['position'] == 'C')  # Creates a boolean mask for the filtering conditions
goals_over_20_and_under_30_and_position_is_c = hockey_players[mask]  # Applies the mask to filter the DataFrame
print(goals_over_20_and_under_30_and_position_is_c) 

print("")

print("not using a mask")
goals_over_20_and_under_30_and_position_is_c = hockey_players[(hockey_players['goals'] > 20) 
                                            & (hockey_players['goals'] < 30)  # Filters the DataFrame to include only rows where the 'goals' column is greater than 20 and 'age' column is less than 30
                                            & (hockey_players['position'] == 'C')] # Filters the DataFrame to include only rows where the 'position' column is 'C'


print(goals_over_20_and_under_30_and_position_is_c)  
print("")



print("goals > 20 and goals < 24 or position == 'C'")
print('Using a mask')
masked = (hockey_players['goals'] > 20) & (hockey_players['goals'] < 24) | (hockey_players['position'] == 'C')  # Creates a boolean mask for the filtering conditions
goals_over_20_and_under_24_or_position_is_c = hockey_players[masked]  # Applies the mask to filter the DataFrame
print(goals_over_20_and_under_24_or_position_is_c) 

print("")

print('tilda masked')
goals_over_20_and_under_24_or_position_is_c = hockey_players[~masked]  # Applies the negated mask to filter the DataFrame
print(goals_over_20_and_under_24_or_position_is_c)  
print("")


print('Replace values - using assign() will create a new dataframe without modifying the original dataframe')
hockey_players_replaced = hockey_players[hockey_players['goals'] > 24].assign(goals = 'High Scorer')    # Filters the DataFrame to include only rows where the 'goals' column is greater than 20 and replaces the 'goals' column values with 'High Scorer'
print(hockey_players_replaced)
print("")


print('Conditional value replacement')
print('Replace values using loc to modify the original dataframe')
print('loc is used to access a group of rows and columns by labels or a boolean array')

#hockey_players[hockey_players['position'] > 24]

print('Step 1 - Use loc to find rows where position is C')
print(hockey_players['position']=='C')
print("")
print('Step 2 - Use loc to replace values in the position column where position is C')

print(hockey_players.loc[hockey_players['position'] == 'C', 'position'])
print("")
print('Step 3 - Assign a new value to the position column where position is C')

#1 )Update the DataFrame in place   
hockey_players.loc[hockey_players['position'] == 'C', 'position'] = 'Center'

# 2) If you want a variable with the filtered rows/column, create it separately
a = hockey_players.loc[hockey_players['position'] == 'Center', 'position']  # a is a Series


print(a)

print(a.head())


# 2) If you want a variable with the filtered rows/column, create it separately
a = hockey_players.loc[hockey_players['position'] == 'Center', ['name','position']]  # a is a Series
print(a)
print("")
print(hockey_players)
print("")

print('Step 4 - Assign a new value to multiple columns where goals is between 20 and 30')
mask = (hockey_players['goals'] > 20) & (hockey_players['goals'] < 30) 
hockey_players.loc[mask, ['good goals']] = 'goodish'  # a is a Series
print(hockey_players)
print("")



print('do this instead')
mask = (hockey_players['goals'] > 20) & (hockey_players['goals'] < 30)

# optional: add the flag column
hockey_players.loc[mask, 'good goals'] = 'goodish'

# display only masked rows (and a few columns)
print(hockey_players.loc[mask, ['name', 'goals', 'good goals']])
print("")


