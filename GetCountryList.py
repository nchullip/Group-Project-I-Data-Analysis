# Importing Dependencies
import pandas as pd
import numpy as np


def get_country_list(data_file, num):
################################################
# This function takes the Data file as input and returns 
# a list of countries with the most population.
#
# Argument: data_file - CSV file
#           num       - Integer
################################################
    # Read the file and store into Pandas data frame
    population_data = pd.read_csv(data_file)

    # Filtering the DataFrame to use only required information
    country_yr_df = population_data[["Country Name","2018"]]
    
    # Sorting the DataFrame
    country_yr_df = country_yr_df.sort_values(["2018"],ascending=False)
    country_df = country_yr_df[:num]
    
    # Converting DataFrame to List
    country_list = country_df['Country Name'].tolist()
    
    return country_list