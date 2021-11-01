import pandas as pd
import numpy as np
def load_and_process(url_or_path_to_csv_file):
    #Method Chain 1 - loading data
    df_0=(pd.read_csv(url_or_path_to_csv_file, encoding='unicode_escape'))
    
    #Method Chain 2 - dropping columns and processing data for df1
    df_1=(df_0
          .drop(columns=['INCIDENT_NUMBER', 'OFFENSE_CODE', 'REPORTING_AREA', 'SHOOTING', 'OCCURRED_ON_DATE' , 'YEAR', 'MONTH', 'DAY_OF_WEEK', 'HOUR', 'UCR_PART', 'Lat', 'Long'])
          .replace(np.nan, 'N', regex=True)
          .dropna()
         )
    #Ensure it returns to the lastest dataframe
    return df_1
def load_and_process(url_or_path_to_csv_file):
    #Method Chain 1 - loading data
    df_0=(pd.read_csv(url_or_path_to_csv_file, encoding='unicode_escape'))
    
    #Method Chain 2 - dropping columns and processing data for df2
    df_2=(df_0
          .drop(columns=['INCIDENT_NUMBER', 'OFFENSE_CODE', 'REPORTING_AREA', 'SHOOTING', 'OCCURRED_ON_DATE', 'UCR_PART', 'Lat', 'Long', 'Location', 'STREET', 'DISTRICT'])
          .replace(np.nan, 'N', regex=True)
          .dropna()
         )
    #Ensure it returns to the lastest dataframe
    return df_2