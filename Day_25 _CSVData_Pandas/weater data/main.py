#-------------------------------------
import pandas
# using the csv library to read .csv files
#import csv
#with open('weather_data.csv') as weather_data_csv:

    #data = csv.reader(weather_data_csv)

    #temperatures: list[int] = []

    #Getting the row with the temperatures
    #for row in data:
        #if row[1]!= 'temp':
            #temperatures.append(int(row[1]))

#Printing a list of temperatures as ints.
#print(temperatures)

#-------------------------------------

#Using the Pandas library

import pandas as pd

data = pd.read_csv('weather_data.csv')
#print(type(data))
#print(data['temp'])

#Example to convert dataframe to dictionary
#data_dict = data.to_dict()
#print(data_dict)

#Example to convert Series to a List
#temp_list = data['temp'].tolist()

#Getting the average value of the Series "Temp" using python's sum()
#average_temp = sum(temp_list)/len(temp_list)
#print(f"Average temperature: {average_temp}")

#Getting the average value of the Series "Temp" using Pandas mean()
#print(f"Average temperature: {data['temp'].mean()}")

##Getting the Max value of the Series "Temp" using Pandas Max()
#print(f"The Maximum temperature: {data['temp'].max()}")


#Alternative to work with series "condition", sensible to capital letters
#data.condition

#Get data in row where the day is Monday
#print(data[data.day == 'Monday'])

#Get row there the temperature was at the maximum
#print(data[data.temp == data.temp.max()])

#Get Monday Temp on Fahrenheit
#monday_temp = data[data.day == 'Monday']
#monday_celsius = monday_temp.temp[0]
#monday_fahrenheit = (monday_celsius*(9/5))+32
#print(f" Monday Temperature in Fahrenheit: {monday_fahrenheit}f")

#Create a dataframe from scratch
#data_dict = {
    #'Students':["Amy", "James", "Angela"],
    #'Scores':[76, 56, 65],
#}
#new_data = pd.DataFrame(data_dict)

#To access a piece of data in a row. You can tap into its attributes with .dot notation.
#data[data.series == value].series.item()
#item() returns the single value of the series