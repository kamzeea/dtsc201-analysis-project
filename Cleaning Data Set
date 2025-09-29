import pandas as pd
data_set = pd.read_csv('ai_assistant_usage_student_life.csv')

#examining the data
data_set.info() #gets number of columns, number of entries, etc.
description = data_set.describe() #gets numerical values such as mean and standard deviation for columns with numerical values
print(description)

#cleaning the data
null_sum = data_set.isnull().sum() #check for null values and records the total number
print(null_sum)
duplicates_sum = data_set.duplicated(subset = ['SessionID']).sum() #checks for duplicate values and records the total number
print(f'The number of duplicate sessions in this data set is {duplicates_sum}')
#subset parameter specifies that we want to check for duplicates in the SessionID only to make sure no session was recorded twice
data_set.drop_duplicates(subset = ['SessionID']) #removes any duplicate rows and outputs the cleaned data set
