"""
File Name: panda.py
Author: David Sanghara
Date Created: 2025-08-24
p
Description :
A script to show the basics of Data Science
M1. Python & Pandas - An unexpected Friendship

License:

"""

# Import pandas library
import pandas as pd


#################################################
print('-------------------------')
print('Introduction to Dataframes')
print('-------------------------')
print('')
################################################

# reads the file candy.csv into a DataFrame
candy = pd.read_csv("data/candybars.csv")   # reads the CSV file into a DataFrame


candy_col = candy.columns                   # gets the column names of the DataFrame
print('Candy Column: ',candy_col)           # prints the column names of the DataFrame
print("")
candy_shape = candy.shape                   # gets the shape of the DataFrame (rows, columns)
print('Candy Shape: ',candy_shape)          # prints the shape of the DataFrame (rows, columns) 
print("")                                   # prints a blank line for better readability
candy_head = candy.head(2)                  # gets the first 2 rows of the DataFrame
print('Candy Head (2 rows):\n',candy_head)  # prints the first 2 rows of the DataFrame
print("")                                   # prints a blank line for better readability        
print('Candy.head:\n',candy.head())         # prints the first 5 rows of the DataFrame
print("")                                   # prints a blank line for better readability    


#################################################
print('-------------------------')
print('2.1. Excercises')
print('-------------------------')
print('')
################################################

#Read in the data
hockey_players = pd.read_csv("data/projections_20202021.csv")   # reads the CSV file into a DataFrame
print(hockey_players .head())                                   # prints the first 5 rows of the DataFrame
print("")
columns_hockey = hockey_players.columns                         # gets the column names of the DataFrame
print(columns_hockey)                                           # prints the column names of the DataFrame   

shape_hockey = hockey_players.shape                             # gets the shape of the DataFrame (rows, columns)
print(shape_hockey)                                             # prints the shape of the DataFrame (rows, columns)   
print("")




#################################################
print('-------------------------')
print('3.  Slicing with Pandas Using .loc[]')
print('-------------------------')
print('')
################################################


print(hockey_players.head()) 
print("")
print(hockey_players.head(15))                       # prints the first 15 rows of the DataFrame
print("")     
print(hockey_players.loc[5:10])                      # prints rows from index 5 to 10
print("")
print(hockey_players.loc[5:10,'name':'shots'])       # prints rows from index 5 to 10 and columns from 'name' to 'shots'
print("")
print(hockey_players.loc[:6])                        # prints rows from the start to index 6
print("") 
print(hockey_players.loc[:6,'name':])                # prints rows from the start to index 6 and columns from 'name' to 'team'

#################################################
print('-------------------------')
print('4. Slicing Columns Using .loc[]')
print('-------------------------')
print('')
################################################


print(hockey_players.loc[:,'name':'position'])                # prints all rows for the 'name' column


#################################################
print('-------------------------')
print('5. Selecting Using .loc[]')
print('-------------------------')
print('')
################################################

print(hockey_players.loc[[2,4,5,10],['name','position']])  # prints specific rows and columns    
print("")
print(hockey_players.loc[[10,5,4,2],['position','name']])  # prints specific rows and columns    


#################################################
print('-------------------------')
print('6. Obtaining Dataframe Values')
print('-------------------------')
print('')
################################################


print(hockey_players.loc[[63]])  # gets the row at index 63
print("")
print(hockey_players.loc[63,'name'])  # gets the value in the 'name' column for the row at index 63
print("")


#################################################
print('-------------------------')
print('7. Selecting a Single Column')
print('-------------------------')
print('')
################################################
print(hockey_players.loc[:,['name']])  # gets the 'name' column as a Series
print("")
print(hockey_players[['name']])

     #################################################
print('-------------------------')
print('8. Slicing and Selecting Using df.iloc[]')
print('-------------------------')
print('')
################################################                  

print(hockey_players.head(10))                      # prints rows from index 5 to 10
print("")
print(hockey_players.loc[5:10])                 # prints rows from index 5 to 10
print("")
print(hockey_players.iloc[5:10])                   # prints rows from index 5 to 10
print("")   
print(hockey_players.iloc[5:11]) 

print(hockey_players.iloc[:,0:6])

print("-------------------------------------------------") 

print(hockey_players.head(3))                       # prints the first 3 rows of the DataFrame
print("")
print(hockey_players.iloc[0:3])                    # prints the first 3 rows of the DataFrame
print("")
print(hockey_players.iloc[:3])               # prints the first 3 rows and first 6 columns of the DataFrame
print("")   

print("-------------------------------------------------") 

print(hockey_players.iloc[505:509])                    # prints rows from index 505 to 509 of the DataFrame
print("")   
print(hockey_players.iloc[-4:])


#################################################
print('-------------------------')
print('9. Sorting Dataframes')
print('-------------------------')
print('')
################################################


sorting_shots = hockey_players.sort_values(by='shots', ascending=False)  # sorts the DataFrame by the 'shots' column in descending order
print(sorting_shots.head(20))  # prints the first 10 rows of the sorted DataFrame
print("")

sorting_shots = hockey_players.sort_values(by='shots', ascending=True)  # sorts the DataFrame by the 'shots' column in ascending order
print(sorting_shots.head(20))  # prints the first 10 rows of the sorted DataFrame
print("")


#################################################
print('-------------------------')
print('10. Summary Statistics')
print('-------------------------')
print('')
################################################
hockey_players_desc = hockey_players.describe()  # generates summary statistics for numerical columns
print(hockey_players_desc)                        # prints the summary statistics       
print("")   

print("Mean: ", hockey_players['shots'].mean())          # prints the mean of the 'shots' column
print("Max: ", hockey_players['shots'].max())           # prints the maximum value of the 'shots' column
print("Min: ", hockey_players['shots'].min())           # prints the minimum value of the 'shots column
print("std: ",hockey_players['shots'].std())           # prints the standard deviation of the 'shots column
print("Median: ",hockey_players['shots'].median())        # prints the median of the 'shots column             
print("Sum: ", hockey_players['shots'].sum())           # prints the sum of the 'shots column
print("Count: ", hockey_players['shots'].count())         # prints the count of non-null values in the 'shots column
print("25%: ",hockey_players['shots'].quantile(0.25))  # prints the 25th percentile of the 'shots column
print("50%: ",hockey_players['shots'].quantile(0.5))   # prints the 50th percentile of the 'shots column
print("75%: ",hockey_players['shots'].quantile(0.75))  # prints the 75th percentile of the 'shots column
print("")       
print(hockey_players.describe(include='all'))  # generates summary statistics for object (string) columns



#################################################
print('-------------------------')
print('11. Frequency Tables and Writing CSVs')
print('-------------------------')
print('')
################################################


name_counts = hockey_players['name']
print(name_counts)  # counts the frequency of each unique value in the 'name' column
print("")
name_value_counts = hockey_players['name'].value_counts()  # counts the frequency of each unique value in the 'name' column
print(name_value_counts)  # prints the frequency counts 
print("")


#################################################
print('-------------------------')
print('Saving DataFrames to CSV')
print('-------------------------')
print('')
################################################


#name_value_counts.to_csv("data/name_value_counts.csv", index=False)  # saves the frequency counts to a CSV file
#hockey_players.to_csv("data/hockey_players_backup.csv", index = False)  # saves the entire DataFrame to a CSV file         
#print("DataFrames saved to CSV files.")
#print("")                                   # prints a blank line for better readability



#################################################
print('-------------------------')
print('altair - A Visualization Library')
print('-------------------------')
print('')
################################################

import altair as alt
import webbrowser
from pathlib import Path

chart0 = alt.Chart(hockey_players).mark_bar().encode(
    x='position',
    y='shots'
).properties(
    title='Shots by Position'       
)

#chart0.show()
#chart0.save('data/chart0.html')
#webbrowser.open('C:/Git/python_data_science/data/chart0.html')  # opens the saved HTML file in the default web browser 


p = Path('data/chart0.html').resolve()
webbrowser.open(p.as_uri())  # opens the saved HTML file in the default web browser


print("Chart 0 displayed")
print("")
