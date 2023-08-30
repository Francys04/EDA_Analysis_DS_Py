"""Bivariate statistics: Numeric to numeric: Correlation;
Bivariate : Numeric to categoriccal: one-way ANOVA (3+ groups) or t-test (2 groups)
Bivariate: Categorical to categorical: Chi-square"""
from scipy import stats
import pandas as pd
from House_Price_predict_example.processing import df_house
import numpy as np

output_df = pd.DataFrame(columns=['r', 'F', 'X2', 'p-values'])


def bivstats(df_house, label):
    for col in df_house:
        if not col == label:
            if df_house[col].isnull().sum() == 0:
                if pd.api.types.is_numeric_dtype(df_house[col]):
                    r, p = stats.pearsonr(df_house[label], df_house[col])
                    output_df.loc[col] = [round(r, 3), np.nan, np.nan, round(p, 6)]
                else:
                    output_df.loc[col] = [np.nan, np.nan, np.nan, 'nulls']

    return output_df.reindex(output_df.r.abs().sort_values(ascending=False).index)


pd.set_option('display.float_format', '{:.5f}'.format)


print(df_house)

bivstats(df_house, 'SalePrice')
