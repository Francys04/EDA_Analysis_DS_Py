from src.config import df_1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""The primary purpose of this code is to preprocess the 'Education', 'Commute Distance', and 'Purchased Bike' 
columns in the DataFrame df_1, converting categorical data into numeric values for further analysis. However, there 
are some issues with the code, as mentioned in lines 16, 18, and 20, where the casting of data types should be applied 
to the DataFrame columns and assigned back to those columns. Additionally, the function clean_bikebuyesr()
 is defined but not called in the code, so it needs to be called to perform the data cleaning and transformation."""


# print(df_1.Education.unique())
# ['Bachelors' 'Partial College' 'High School' 'Partial High School'
#  'Graduate Degree']

def clean_bikebuyesr():
    df_1['Education_rank'] = df_1['Education']
    df_1['Commute_rank'] = df_1['Commute Distance']
    df_1['Purchased Bike'] = df_1['Purchased Bike']
    df_1.Education_rank.replace(['Partial High School', 'High School', 'Partial College', 'Bachelors',
                                 'Graduate Degree'], [1, 2, 3, 4, 5], inplace=True)
    df_1.Commute_rank.replace(['0-1 Miles', '1-2 Miles', '2-5 Miles', '5-10 Miles', '10+ Miles'],
                              [0, 1, 2, 5, 10], inplace=True)
    df_1['Purchased Bike'].replace(['Yes', 'No'], [0, 1], inplace=True)
    df_1.astype({'Education_rank': 'int64'})
    df_1.astype({'Commute_rank': 'int64'})
    df_1['Purchased Bike'].astype('int64')
    pd.set_option('display.max_rows', 50)
    pd.set_option('display.max_columns', 50)
    print(df_1)
    return df_1


clean_bikebuyesr()
