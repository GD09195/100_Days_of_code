FUR_COLOR_COLUMN_TITLE = "Primary Fur Color"

import pandas as pd

#Read .csv into a pandas' dataframe
squirrel_census_df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240901.csv")

#Save only "Primary Fur Color" Series from complete dataframe
primary_fur_color_Series = squirrel_census_df[FUR_COLOR_COLUMN_TITLE]


#Using pandas' .count()
#gray_squirrels_count = primary_fur_color_Series[primary_fur_color_Series == 'Gray'].count()
#Using python's len()
#gray_squirrels_count = len(primary_fur_color_Series[primary_fur_color_Series == 'Gray'])

#count each color from the primary fur color Series
gray_squirrels_count = primary_fur_color_Series[primary_fur_color_Series == 'Gray'].count()
red_squirrels__count = primary_fur_color_Series[primary_fur_color_Series == 'Cinnamon'].count()
black_squirrels_count = primary_fur_color_Series[primary_fur_color_Series == 'Black'].count()

#Dict to convert to dataframe
fur_count ={
    'Fur color':['gray', 'red', 'black'],
    'Count': [gray_squirrels_count,red_squirrels__count,black_squirrels_count]
}

#Convert fur_count dict into a dataframe
fur_color_df = pd.DataFrame(fur_count)
#Export dataframe into .csv
fur_color_df.to_csv('squirrel_count.csv')