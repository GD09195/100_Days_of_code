
#List comprehension structure
new_list = [item for item in list]

#conditional List comprehension structure
new_list = [item for item in list if test]

#Dictionary comprehensions structure
new_dict = {new_key: new_value for item in list}

new_dict = {new_key: new_value for (key, value) in dict.items()}

new_dict = {new_key: new_value for (key, value) in dict.items() if test}

#Looping through a Dictionary
for (key, value) in dictionary.items():
    print(f'{key} :  {value}')

#Loooping through Panda's Dataframes
panda_dataframe = pandas.Dataframe(dictionary)
#using For loop (not optimal)
for (key, value) in panda_dataframe.items():
    print(f'{key} :  {value}')

#Using Pdndas .iterrows()
#Loop through rows of a data frame. Each row is a Panda's Series
for (index, row) in panda_dataframe.iterrows()
    print(row.column_name)