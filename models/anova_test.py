from src.config import df_1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
