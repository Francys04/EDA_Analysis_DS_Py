import matplotlib.pyplot as plt  # Used for creating plots and graphs.
from scipy import stats  # Used for statistical tests.
import statistics as stat  # Used for calculating statistical measures.
import seaborn as sns  # A data visualization library that works well with pandas and matplotlib.
import pandas as pd  # Used for data manipulation.
from src.config import df  # Import a DataFrame named df from a module called 'src.config'.


# Start with simple data in lists, with the different nr of values in lists
edu_PartialHS = [30000, 1000, 1000, 20000, 70000, 30000, 10000, 20000, 10000, 30000]
edu_HighSchool = [20000, 30000, 60000, 20000, 40000, 60000, 60000]
edu_PartialCollege = [60000, 40000, 30000, 130000, 60000, 40000]
edu_Bachelors = [40000, 20000, 90000, 120000, 60000, 130000, 20000, 10000, 80000, 30000, 10000, 12000]
edu_Graduate = [160000, 50000, 80000, 30000, 40000, 80000, 130000, 10000, 130000, 50000, 130000]

# t, p = stats.ttest_ind(edu_PartialHS, edu_HighSchool)
#
# print(f't-value = {t}')
# print(f'p-value = {p}')
# t-value = -1.9912776506273298
# p-value = 0.06498548565092015


# sns.distplot(edu_PartialHS, label="Partial High School")
# sns.distplot(edu_HighSchool, label="High School")
# sns.distplot(edu_PartialCollege, label="Partial College")
# sns.distplot(edu_Bachelors, label="Bachelors")
# sns.distplot(edu_Graduate, label="Graduate")
# plt.legend()
# plt.show()

# statsistics_ = stats.f_oneway(edu_Bachelors, edu_Graduate, edu_HighSchool, edu_PartialCollege, edu_PartialHS)
# print(statsistics_) # F_onewayResult(statistic=3.4085325297772786, pvalue=0.01700249936126447)

f, p = stats.f_oneway(edu_Bachelors, edu_Graduate, edu_HighSchool, edu_PartialCollege, edu_PartialHS)
# print(f'f-value = {f}')
# print(f'p-value = {p}')
## f-value = 3.4085325297772786
## p-value = 0.01700249936126447


'''Create graph for df file (insurance.csv)'''
plt.figure(1)
sns.histplot(data=df, x="charges", hue='sex', kde=True)
plt.figure(2)
sns.histplot(data=df, x="charges", hue='smoker', kde=True)
plt.show()

smoker_y = df[df['smoker'] == 'yes']
smoker_n = df[df['smoker'] == 'no']
stat_1 = stats.ttest_ind(smoker_y['charges'], smoker_n['charges'])
print(stat_1)
# TtestResult(statistic=46.66492117272371, pvalue=8.271435842179102e-283, df=1336.0)

feature = 'smoker'
label = 'charges'

groups = df[feature].unique()
# print(groups)
grouped_values = []
for group in groups:
    grouped_values.append(df[df[feature] == group][label])
print(grouped_values)

print(stats.f_oneway(*grouped_values)) # F_onewayResult(statistic=2177.614868056519, pvalue=8.271435842182967e-283)
