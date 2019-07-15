import pandas as pd
import os
import numpy as np
from GetCountryList import get_country_list

temp_df = pd.read_csv("Resources/GlobalLandTemperaturesByCountry.csv")
temp_df=temp_df.dropna()

temp_df.head()

population_data_file = "Resources/world_population_2018aug.csv"
country_list = get_country_list(data_file = population_data_file, num = 5)
country_list

def averagetemperature_df(country_list, temp_df, Year):    
    temp_df['dt'] = pd.to_datetime(temp_df['dt'])
    temp_df['Year'] = temp_df['dt'].dt.to_period('Y')
    temp_df = temp_df[temp_df['Country'].isin(country_list)]
    temp_df= temp_df[temp_df["Year"] >= Year]
        
    temperature_df = temp_df[['AverageTemperature', 'Country', 'Year']]
    temperature_grouped_df = temperature_df.groupby(['Country', "Year"])
    
    meantemp=temperature_grouped_df["AverageTemperature"].mean()
    mean_temp_df=pd.DataFrame(meantemp)
    
    relative_temp_df=mean_temp_df.copy().reset_index()
        
    relativetemp_list=[]
    a=0
    
    for i in range(len(relative_temp_df["AverageTemperature"])):
            
        j=i+1
        
        if relative_temp_df.iloc[i,0]=="China":                                      #checking for country
            relativetemp=relative_temp_df.iloc[i,2]-relative_temp_df.iloc[0,2]      #subtracting temp of 1960 from other years
            relativetemp_list.append(relativetemp)
            
        if relative_temp_df.iloc[i,0]=="India":                                      #checking for country
            relativetemp=relative_temp_df.iloc[i,2]-relative_temp_df.iloc[54,2]      #subtracting temp of 1960 from other years
            relativetemp_list.append(relativetemp)
            
        if relative_temp_df.iloc[i,0]=="Indonesia":                                      #checking for country
            relativetemp=relative_temp_df.iloc[i,2]-relative_temp_df.iloc[108,2]      #subtracting temp of 1960 from other years
            relativetemp_list.append(relativetemp)
            
        if relative_temp_df.iloc[i,0]=="Pakistan":                                      #checking for country
            relativetemp=relative_temp_df.iloc[i,2]-relative_temp_df.iloc[162,2]      #subtracting temp of 1960 from other years
            relativetemp_list.append(relativetemp)  
        
        if relative_temp_df.iloc[i,0]=="United States":                               #checking for country
            relativetemp=relative_temp_df.iloc[i,2]-relative_temp_df.iloc[216,2]      #subtracting temp of 1960 from other years
            relativetemp_list.append(relativetemp) 
        
        
        
        #else:
            #relativetemp=relative_temp_df.iloc[i,2]-relative_temp_df.iloc[a,2]
            #relativetemp_list.append(relativetemp)
            #k=j+1
            #relativetemp=relative_temp_df.iloc[k,2]-relative_temp_df.iloc[j,2]
            #relativetemp_list.append(relativetemp)
            #a=a+54
            #continue
             
    relative_temp_df["RelativeTemperature"]=pd.DataFrame(relativetemp_list)
    relative_temp_df.to_csv("tempdata.csv")
    
    return relative_temp_df

averagetemperature_df= averagetemperature_df(country_list=country_list, temp_df =temp_df, Year =1960)
averagetemperature_df