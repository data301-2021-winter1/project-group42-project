#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


def load_and_process(url_or_path_to_csv_file):

    df1 = (
        pd.read_csv(url_or_path_to_csv_file, encoding = 'unicode_escape')
      )
    df2 = (
        df1
        .drop(columns = ['INCIDENT_NUMBER', 'REPORTING_AREA', 'DAY_OF_WEEK', 'UCR_PART', 'Location', 'OFFENSE_DESCRIPTION', 'Lat', 'Long', 'HOUR', 'OCCURRED_ON_DATE', 'OFFENSE_CODE'])
      )
    df3 = (
         df2
        ['SHOOTING']
        .replace(np.nan, 'N', inplace = True)
     )
    df4 = (
        df2
        .dropna()
    )

    # Make sure to return the latest dataframe

    return df4


# In[ ]:




