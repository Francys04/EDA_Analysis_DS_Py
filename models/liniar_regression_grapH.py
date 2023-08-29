import matplotlib.pyplot as plt
import seaborn as sns
from models.liniar_regresions import df

'''Show result with seaborn style graph'''
# Example 1
sns.set(color_codes=True)
sns.jointplot(x='age', y='charges', data=df)
plt.show()

# Example 2
sns.set_style("white")
sns.jointplot(x='age', y='charges', data=df, kind='hex')
plt.show()

# Example 3

f, ax = plt.subplots(figsize=(8, 6))
cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=False)
sns.kdeplot(df.age, df.charges, cmap=cmap, n_levels=60, shade=True)

plt.show()

# df.dropna(inplace=True)  # remove null values first
# sns.pairplot(df)
# plt.show()
