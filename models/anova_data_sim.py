import matplotlib.pyplot as plt  # Used for creating plots.
from scipy import stats  # for statistical functions.
import pandas as pd  # Used for data manipulation.
from models.anova_test import clean_bikebuyesr  # models.anova_test.clean_bikebuyesr is a function to clean the data.
import seaborn as sns  # Used for statistical data visualization.
from statsmodels.stats.multicomp import MultiComparison  # for post hoc analysis.
from scipy.stats import ttest_ind  # for performing t-tests.

"""This code combines statistical analysis techniques, including ANOVA and t-tests, with data visualization using 
Seaborn and Matplotlib to analyze the relationship between education levels and bike purchases."""

df_4 = clean_bikebuyesr()

groups = df_4['Education'].unique()
group_labels = []
for g in groups:
    group_labels.append(df_4[df_4['Education'] == g]['Purchased Bike'])

# Now calculate the ANOVA results
F, p = stats.f_oneway(*group_labels)
print(f'F: ' + str(round(F, 4)))
print(f'p: ' + str(round(p, 4)))
# F: 6.4653
# p: 0.0

r, p1 = stats.pearsonr(df_4['Education_rank'], df_4['Purchased Bike'])
print(f'r: ' + str(round(F, 4)))
print(f'p: ' + str(round(p1, 4)))
# r: 6.4653
# p: 0.0


viz = sns.barplot(x=df_4['Education'], y=df_4['Purchased Bike'],
                  order=['Partial High School', 'High School', 'Partial College', 'Bachelors', 'Graduate Degree'])
viz.set_xticklabels(viz.get_xticklabels(), rotation=25)
plt.show()

partial_high_school = df_4[df_4.Education == 'Partial High School']
high_school = df_4[df_4.Education == 'High School']
t, p2 = stats.ttest_ind(partial_high_school['Purchased Bike'], high_school['Purchased Bike'])

print(f't: ' + str(round(t, 2)))
print(f'p: ' + str(round(p2, 2)))
# r: 6.4653
# p: 0.0

'''Statistical graph'''

mc = MultiComparison(df_4['Purchased Bike'], df_4['Education'])
print(mc.tukeyhsd())
#            Multiple Comparison of Means - Tukey HSD, FWER=0.05
# =========================================================================
#      group1            group2       meandiff p-adj   lower  upper  reject
# -------------------------------------------------------------------------
#       Bachelors     Graduate Degree   0.0121  0.999 -0.1163 0.1404  False
#       Bachelors         High School   0.1109 0.1204 -0.0162 0.2381  False
#       Bachelors     Partial College   0.1032 0.0942 -0.0102 0.2166  False
#       Bachelors Partial High School   0.2891 0.0001  0.1159 0.4623   True
# Graduate Degree         High School   0.0989 0.3297  -0.045 0.2428  False
# Graduate Degree     Partial College   0.0912 0.3236 -0.0407  0.223  False
# Graduate Degree Partial High School   0.2771 0.0005  0.0913 0.4629   True
#     High School     Partial College  -0.0077 0.9998 -0.1385  0.123  False
#     High School Partial High School   0.1782 0.0655 -0.0068 0.3632  False
# Partial College Partial High School   0.1859 0.0322  0.0101 0.3617   True
# -------------------------------------------------------------------------

e_type = df_4.Education.unique()
tests = []

for i, e in enumerate(e_type):
    # 0.Bachelors
    # 1.Partial College
    # 2.High School
    # 3.Partial High School
    # 4.Graduate Degree

    for i2, e2 in enumerate(e_type):
        # print(e, '--', e2)
        if i2 > i:
            g1 = df_4[df_4.Education == e]['Purchased Bike']
            g2 = df_4[df_4.Education == e2]['Purchased Bike']
            t, p = stats.ttest_ind(g1, g2)

            tests.append([f'{e} - {e2}:', {t.round(4)}, {p.round(4)}])

    # print(f'T-tests')
# ['Bachelors - Partial College:', {-2.4693}, {0.0138}]
# ['Bachelors - High School:', {-2.3675}, {0.0183}]
# ['Bachelors - Partial High School:', {-4.6253}, {0.0}]
# ['Bachelors - Graduate Degree:', {-0.2546}, {0.7991}]
# ['Partial College - High School:', {-0.1601}, {0.8729}]
# ['Partial College - Partial High School:', {-2.9354}, {0.0036}]
# ['Partial College - Graduate Degree:', {1.8728}, {0.0618}]
# ['High School - Partial High School:', {-2.698}, {0.0074}]
# ['High School - Graduate Degree:', {1.862}, {0.0634}]
# ['Partial High School - Graduate Degree:', {4.1685}, {0.0}]

textstr = f'       Anova\n'
textstr += f'F:  {F.__round__(4)}\n'
textstr += f'p:  {p.__round__(4)}\n'
textstr += f'Sig. comparisons (Bonferonni)\n'

threshold = 0.05 / len(tests)

print(f'Significant t-test below {threshold}:')
for t in tests:
    if t[2] <= threshold:
        textstr += f'{t[0]} {t[1]} {t[2]}'

plt.figure(3)
viz = sns.barplot(x=df_4['Education'], y=df_4['Purchased Bike'],
                  order=['Partial High School', 'High School', 'Partial College', 'Bachelors', 'Graduate Degree'])
viz.set_xticklabels(viz.get_xticklabels(), rotation=25)
plt.text(1, 0, textstr, fontsize=12, transform=plt.gcf().transFigure)
plt.show()
