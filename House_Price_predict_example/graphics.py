import pandas as pd  # for data manipulation and analysis.
import seaborn as sns  # for statistical data visualization.
from House_Price_predict_example.bivariate_statistics import df_house
import matplotlib.pyplot as plt  # for statistical models and tests.
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.diagnostic import het_white
import statsmodels.api as sm
from statsmodels.formula.api import ols
from House_Price_predict_example.bivariate_statistics import df_house
from scipy import stats

"""Now, let's discuss the purpose of this code. It appears to be focused on data analysis and visualization of house 
price data. It includes functions for checking heteroscedasticity, creating scatter plots with regression lines, and 
preprocessing the dataset by renaming columns. The final part of the code sets display options for pandas and prints 
the initial rows of the dataset for inspection."""


def heterscedasticity(df_house, feature, label):
    model = ols(formula=(label + '~' + feature), data=df_house).fit()

    white_test = het_white(model.resid, model.model.exog)
    bp_test = het_breuschpagan(model.resid, model.model.exog)

    out_df = pd.DataFrame(columns=['LM stat', 'LM p-value', 'F-stat', 'F p-value'])
    out_df.loc['White'] = white_test
    out_df.loc['Breusch-Pagan'] = bp_test
    return out_df.round(3)


"""Function with specific feature (OverallQual) and label (SalePrice) from the df_house DataFrame."""


def scatter(feature, label):
    m, b, r, p, err = stats.linregress(feature, label)
    textstr = 'y = ' + str(round(m, 2)) + 'x + ' + str(round(b, 2)) + '\n'
    textstr += 'r2 = ' + str(round(r ** 2, 2)) + '\n'
    textstr += 'p = ' + str(round(p, 2)) + '\n'
    textstr += str(feature.name) + 'skew = ' + str(round(feature.skew(), 2)) + '\n'
    textstr += str(label.name) + 'skew = ' + str(round(label.skew(), 2)) + '\n'
    textstr += str(heterscedasticity(pd.DataFrame(label).join(pd.DataFrame(feature)), feature.name, label.name))

    sns.set(color_codes=True)
    bbox = dict(boxstyle='square', facecolor='lavender', alpha=0.5)
    ax = sns.jointplot(feature, label, kind='reg')
    ax.fig.text(1.1, 1, textstr, fontsize=12, ha='center',
                transform=ax.ax_joint.transAxes, bbox=bbox, verticalalignment='top')
    plt.show()


scatter(df_house.OverallQual, df_house.SalePrice)


def import_house_data(df_house):
    df_house.drop(columns=['Id'], inplace=True)
    df_house.dropna(axis=1, inplace=True)

    for col in df_house:
        if col[0].isdigit():
            nums = ['zero', 'one', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
            df_house.rename(columns={col: nums[int(col[0])] + '_' + col}, inplace=True)
    return df_house


pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.float_format', '{:.5f}'.format)
print(df_house.head())
