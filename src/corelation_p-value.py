"""The code essentially calculates and presents the strength and significance of the linear relationships between
the 'charges' column and all other numeric columns in the DataFrame 'df'."""
import numpy as np # numerical operations.
import pandas as pd # Used for data manipulation and DataFrame handling.
from src.config import df
from scipy import stats

# print(df.corr())
#                age       bmi  children   charges
# age       1.000000  0.109272  0.042469  0.299008
# bmi       0.109272  1.000000  0.012759  0.198341
# children  0.042469  0.012759  1.000000  0.067998
# charges   0.299008  0.198341  0.067998  1.000000

# print(df.charges.corr(df.bmi)) # 0.19834096883362887
# corr = stats.pearsonr(df.charges, df.age)
# print(corr) # PearsonRResult(statistic=0.29900819333064743, pvalue=4.886693331718505e-29)

r, p = stats.pearsonr(df.charges, df.age)
print(round(r, 4))  # 0.299
print(round(p, 29))  # 5.0000000000000004e-29

corr_df = pd.DataFrame(columns=['r', 'p'])

"""Iterate through each column in the DataFrame 'df':
Check if the column is numeric (excluding the 'charges' column).
If the column is numeric, calculate the Pearson correlation coefficient ('r')
and p-value ('p') between 'charges' and the current column.
Round the 'r' and 'p' values to 3 decimal places.
Add the 'r' and 'p' values to the 'corr_df' DataFrame with the column name as the index."""

for col in df:
    print(col)
    if pd.api.types.is_numeric_dtype(df[col]) and col != 'charges':
        r, p = stats.pearsonr(df.charges, df[col])
        corr_df.loc[col] = [round(r, 3), round(p, 3)]
print(corr_df)
#               r      p
# age       0.299  0.000
# bmi       0.198  0.000
# children  0.068  0.013
