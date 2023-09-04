"""Each example demonstrates different visualization techniques using seaborn, including scatterplots,
hexbin plots, and kernel density estimation (KDE) plots.
These visualizations are used to explore the relationships and distributions of data in the DataFrame df."""

import matplotlib.pyplot as plt  # Used for creating plots and graphs.
import seaborn as sns  # A data visualization library that works well with pandas and matplotlib.
from models.liniar_regresions import df  # Import the DataFrame df from a module called 'models.liniar_regresions'.

'''Show result with seaborn style graph'''
# Example 1
sns.set(color_codes=True)  # Set seaborn to use color codes.
sns.jointplot(x='age', y='charges', data=df)  # Create a jointplot with 'age' on the x-axis and 'charges' on the y-axis.
# This plot is a scatterplot with marginal histograms.
plt.show()  # Display the plot.

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
