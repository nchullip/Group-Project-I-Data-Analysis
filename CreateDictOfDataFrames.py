# Importing Dependencies
import pandas as pd
import numpy as np

def create_dataFrame(country_list, full_data_df):
############################################################################
# This function takes the list of countries, Pandas DataFrame and 
# an empty python dictionary as input and returns a Dictionary of DataFrames
# Arguments: country_list = A List with country names
#            full_data_df = Pandas DataFrame
#            output       = Empty Dictionary
############################################################################
	output = {}
	for country in country_list:
        # CO2 Emission Computations
		CO2_emissions_df = full_data_df[full_data_df['Indicator Name'] == 'CO2 emissions (metric tons per capita)']

        # Isolating values for the particular country and creating a separate DataFrame
		CO2_emissions_updated = CO2_emissions_df[CO2_emissions_df['Country Name'] == country].T

        # Data Clean-Up
		cell_count = int(CO2_emissions_updated.columns[0])
		CO2_emissions_updated = CO2_emissions_updated.rename(columns = {cell_count: "CO2 Emissions"})
		CO2_emissions_updated = CO2_emissions_updated.dropna()
		CO2_emissions_updated = CO2_emissions_updated.reset_index().iloc[4:]
		CO2_emissions_updated = CO2_emissions_updated.rename(columns = {"index": "Years"})


        # Forest Area Percentage Computations
		Forest_Area_df = full_data_df[full_data_df['Indicator Name'] == 'Forest area (% of land area)']

        # Isolating values for the particular country and creating a separate DataFrame
		Forest_Area_updated = Forest_Area_df[Forest_Area_df['Country Name'] == country].T

        # Data Clean-Up
		cell_count = int(Forest_Area_updated.columns[0])
		Forest_Area_updated = Forest_Area_updated.rename(columns = {cell_count: "Forest Area Percentage"})
		Forest_Area_updated = Forest_Area_updated.dropna()
		Forest_Area_updated = Forest_Area_updated.reset_index().iloc[4:]
		Forest_Area_updated = Forest_Area_updated.rename(columns = {"index": "Years"})


        # Air Pollution Computation
		air_pollution_df = full_data_df[full_data_df['Indicator Name'] == 'PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)']

        # Isolating values for the particular country and creating a separate DataFrame
		air_pollution_updated = air_pollution_df[air_pollution_df['Country Name'] == country].T

        # Data Clean-Up
		cell_count = int(air_pollution_updated.columns[0])
		air_pollution_updated = air_pollution_updated.rename(columns = {cell_count: "Air Pollution Index"})
		air_pollution_updated = air_pollution_updated.dropna().iloc[4:].reset_index()
		air_pollution_updated = air_pollution_updated.rename(columns = {"index": "Years"})

		output[country] = [CO2_emissions_updated, Forest_Area_updated, air_pollution_updated]
        
	return output