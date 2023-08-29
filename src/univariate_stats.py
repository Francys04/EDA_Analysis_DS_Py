import pandas as pd
from src.config import df
import numpy as np
from scipy.stats import kurtosis, skew
# print(df.describe())
#                age          bmi     children       charges
# count  1338.000000  1338.000000  1338.000000   1338.000000
# mean     39.207025    30.663397     1.094918  13270.422265
# std      14.049960     6.098187     1.205493  12110.011237
# min      18.000000    15.960000     0.000000   1121.873900
# 25%      27.000000    26.296250     0.000000   4740.287150
# 50%      39.000000    30.400000     1.000000   9382.033000
# 75%      51.000000    34.693750     2.000000  16639.912515
# max      64.000000    53.130000     5.000000  63770.428010

# print(df.shape)
# (1338, 7)

''' Processing the dataframe '''
print(f'age: {df.age.count()}')
print(f'columns: {df.columns}')

# show the data from columns
# print(f'age: {df.age.count()}')  # age: 1338
# print(f'sex: {df.sex.count()}')  # sex: 1338
# print(f'bmi: {df.bmi.count()}')  # bmi: 1338
# print(f'children: {df.children.count()}')  # children: 1338
# print(f'smoker: {df.smoker.count()}')  # smoker: 1338
# print(f'region: {df.region.count()}')  # region: 1338
# print(f'charges: {df.charges.count()}')  # charges: 1338

# data type
# print(f'age: {df.age.dtype}')
# print(f'sex: {df.sex.dtype}')
# print(f'bmi: {df.bmi.dtype}')
# print(f'children: {df.children.dtype}')
# print(f'smoker: {df.smoker.dtype}')
# print(f'region: {df.region.dtype}')
# print(f'charges: {df.charges.dtype}')

# verify missing data
#
# print(f'age: {df.age.isnull().sum()}')
# print(f'sex: {df.sex.isnull().sum()}')
# print(f'bmi: {df.bmi.isnull().sum()}')
# print(f'children: {df.children.isnull().sum()}')
# print(f'smoker: {df.smoker.isnull().sum()}')
# print(f'region: {df.region.isnull().sum()}')
# print(f'charges: {df.charges.isnull().sum()}')

'''Boundaries'''

print(df.charges.min())
print(df.charges.quantile(.25))
print(df.charges.quantile(.50))
print(df.charges.quantile(.75))
print(df.charges.max())

print(df.charges.mean())
print(df.charges.median())
print(df.charges.mode().values[0])

print(df.charges.std())  # 12110.011236694001 => pandas

print(np.std(df.charges))  # 12105.484975561612 => numpy


print(skew(df.charges, bias=False))  # 1.5158796580240383
print(kurtosis(df.charges, bias=False)) # 1.6062986532967916



