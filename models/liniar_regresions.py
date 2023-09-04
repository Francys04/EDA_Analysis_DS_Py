"""This code essentially performs various statistical analyses and visualizations, including correlation analysis,
scatter plots, linear regression, and heteroscedasticity diagnostics, to explore the relationship between 'age'
and 'charges' in the dataset."""
import matplotlib.pyplot as plt  # Used for creating plots and graphs.
from src.univariate_stats import df  # Import a DataFrame named df from a module called 'src.univariate_stats'.
import pandas as pd  # Used for data manipulation.
from scipy import stats  # Used for statistical tests.
from statsmodels.stats.diagnostic import het_breuschpagan  # Import specific functions for heteroscedasticity
# tests from statsmodels.stats.diagnostic.
from statsmodels.stats.diagnostic import het_white  # Calculates the Pearson correlation coefficient (r) and its
# associated p-value (p) between 'charges' and 'age'.
from statsmodels.formula.api import ols  # Import the ols function from statsmodels.formula.api for regression analysis.


r, p = stats.pearsonr(df.charges, df.age)
print(round(r, 4))  # 0.299
print(round(p, 29))  # 5.0000000000000004e-29

corr_df = pd.DataFrame(columns=['r', 'p'])
for col in df:
    print(col)
    if pd.api.types.is_numeric_dtype(df[col]) and col != 'charges':
        r, p = stats.pearsonr(df.charges, df[col])
        corr_df.loc[col] = [round(r, 3), round(p, 3)]
print(corr_df)

plt.scatter(df.age, df.charges)
plt.title('Insurance Age vs Charges')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.show()

df_smoker = df[df['smoker'] == 'yes']
df_nonsmoker = df[df['smoker'] == 'no']
plt.scatter(df_smoker.age, df_smoker.charges, label='Smokers')
plt.scatter(df_nonsmoker.age, df_nonsmoker.charges, label='Non-smoker')
plt.title('Smoker vs Non-smoker')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.legend()
plt.ylabel('Charges')
plt.show()

df_smoker_reduces = df_smoker.sample(50)
df_nonsmoker_reduces = df_nonsmoker.sample(50)

plt.scatter(df_smoker_reduces.age, df_smoker_reduces.charges, label='Smokers', color='red', marker='*')
plt.scatter(df_nonsmoker_reduces.age, df_nonsmoker_reduces.charges, label='Non-smoker', color='green', marker='+')

plt.title('Smoker vs Non-smoker')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.legend()
plt.ylabel('Charges')
plt.show()

'''Regression graph'''
# print(stats.linregress(df.age, df.charges))
# LinregressResult(slope=257.7226186668956, intercept=3165.885006063023, rvalue=0.29900819333064776,
# pvalue=4.886693331718281e-29, stderr=22.5023892867703, intercept_stderr=937.1494650703767)

"""Create a scatter plot to compare 'age' vs. 'charges' for the reduced samples:
Scatter plot for smokers in red with '*' markers.
Scatter plot for non-smokers in green with '+' markers.
Set plot title, x-axis label, y-axis label, and add a legend."""
# y = mx + b
# y = slope(x) + intersept
m, b, r, p, err = stats.linregress(df.age, df.charges)
x = range(18, df.age.max() + 2)
y = m * x + b
plt.plot(x, y, color='red')
plt.scatter(df.age, df.charges)
plt.title('Insurance Age vs Charges')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.show()

# diagnostics with statsmdels
model = ols(formula='age~charges', data=df).fit()
white_test = het_white(model.resid, model.model.exog)
breushpagan_test = het_breuschpagan(model.resid, model.model.exog)


output_df = pd.DataFrame(columns=['LM stst', 'LM p', 'F stat', 'F stat'])
output_df.loc['White'] = white_test
output_df.loc['Breusch-Pagan'] = breushpagan_test
print(output_df)
#                   LM stst          LM p     F stat        F stat
# White          113.205738  2.616293e-25  61.695937  2.358806e-26
# Breusch-Pagan   48.227283  3.795702e-12  49.955817  2.525670e-12




