import pandas as pd
import numpy as np
from src.config import df
import statsmodels.api as sm

label = "charges"

y = df.charges
x = df[['age', 'bmi', 'children']].assign(const=1)

model = sm.OLS(y, x)
results = model.fit()
print(results.summary())

df['predictions'] = results.fittedvalues
print(df)
# single score prediction

print(results.predict([19, 27.9, 0, 1]))
# prediction = [6908.77753344]

'''MLR with categorical values'''

df = pd.get_dummies(df, columns=['sex', 'smoker', 'region'], prefix='', drop_first=True)

print(df.head())
#    age     bmi  children      charges  ...  _yes  _northwest  _southeast  _southwest
# 0   19  27.900         0  16884.92400  ...     1           0           0           1
# 1   18  33.770         1   1725.55230  ...     0           0           1           0
# 2   28  33.000         3   4449.46200  ...     0           0           1           0
# 3   33  22.705         0  21984.47061  ...     0           1           0           0
# 4   32  28.880         0   3866.85520  ...     0           1           0           0

# X = df.drop(columns=[label]).assign(const=1)
# results = sm.OLS(y, X).fit()
# print(results.summary())
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                charges   R-squared:                       0.751
# Model:                            OLS   Adj. R-squared:                  0.749
# Method:                 Least Squares   F-statistic:                     500.8
# Date:                Tue, 29 Aug 2023   Prob (F-statistic):               0.00
# Time:                        23:20:37   Log-Likelihood:                -13548.
# No. Observations:                1338   AIC:                         2.711e+04
# Df Residuals:                    1329   BIC:                         2.716e+04
# Df Model:                           8
# Covariance Type:            nonrobust
# ===============================================================================
#                   coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------
# age          -155.5933     31.584     -4.926      0.000    -217.553     -93.633
# bmi          -231.5183     30.568     -7.574      0.000    -291.485    -171.552
# children     -457.4557    149.387     -3.062      0.002    -750.516    -164.395
# predictions     1.7186      0.142     12.118      0.000       1.440       1.997
# _male        -131.3144    332.945     -0.394      0.693    -784.470     521.842
# _yes         2.385e+04    413.153     57.723      0.000     2.3e+04    2.47e+04
# _northwest   -352.9639    476.276     -0.741      0.459   -1287.298     581.370
# _southeast  -1035.0220    478.692     -2.162      0.031   -1974.097     -95.947
# _southwest   -960.0510    477.933     -2.009      0.045   -1897.636     -22.466
# const         -52.4220     12.639     -4.148      0.000     -77.217     -27.627
# ==============================================================================
# Omnibus:                      300.366   Durbin-Watson:                   2.088
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):              718.887
# Skew:                           1.211   Prob(JB):                    7.86e-157
# Kurtosis:                       5.651   Cond. No.                     1.32e+19
# ==============================================================================

# or in this way
for col in df:
    if not pd.api.types.is_numeric_dtype(df[col]):
        df = pd.get_dummies(df, columns=[col], prefix=col, drop_first=True)
    print(df.head())

