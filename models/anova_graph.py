from models.anova_test import clean_bikebuyesr  # function from a module called 'models.anova_test'
import pandas as pd  # Used for data manipulation.
import numpy as np  # Used for numerical operations.
import seaborn as sns  # Used for statistical data visualization.
import matplotlib.pyplot as plt  # Used for creating plots and graphs.

"""This code combines Seaborn and Matplotlib to create bar plots visualizing the relationship between education 
levels and bike purchase as well as quarterly sales data for different locations. 
The second figure is used to create a larger version of the bar plot."""

df_2 = clean_bikebuyesr()

plt.figure(1)
sns.barplot(x=df_2['Education'], y=df_2["Purchased Bike"])

plt.figure(2, figsize=(10, 5))
sns.barplot(x=df_2['Education'], y=df_2["Purchased Bike"])

'''Example of quantitative graph'''
"""Extract and flatten data from the 'Q1 Sales', 'Q2 Sales', 'Q3 Sales', and 'Q4 Sales' 
columns of df_3 into four separate lists: list_1, list_2, list_3, and list_4."""
df_3 = pd.DataFrame({'Locations': ['Bucharest', 'Timisoara', 'Cluj-Napoca', 'Iasi'],
                     'Q1 Sales': [154943, 6473247, 823843, 825893],
                     'Q2 Sales': [15494123, 64733247, 82343643, 823893],
                     'Q3 Sales': [1324943, 64743247, 823543, 8253293],
                     'Q4 Sales': [1543943, 643233247, 843843, 825893]})

#  Create the position for the bars
x = np.arange(len(df_3.Locations))
# Store the three columns from the dataframe and 'flatten' them to appear as a regular Python list structure
list_1 = df_3['Q1 Sales'].values.flatten()
list_2 = df_3['Q2 Sales'].values.flatten()
list_3 = df_3['Q3 Sales'].values.flatten()  # Plot the bars for Q3 sales, starting from the top of Q1 and Q2 sales.
list_4 = df_3['Q4 Sales'].values.flatten()  # Plot the bars for Q4 sales, starting from the top of Q2 and Q3 sales.

# plot the bar charts
plt.bar(x, list_1, label='Q1')
plt.bar(x, list_2, bottom=list_1, label='Q2')
plt.bar(x, list_3, bottom=list_1 + list_2, label='Q3')
plt.bar(x, list_4, bottom=list_2 + list_3, label='Q4')

# plot the pokemon names as the x ticks
plt.xticks(x, df_3.Locations)

# Create legend
plt.legend(loc='upper right')

# add labels and title
plt.xlabel('Markets')
plt.ylabel('Sales in Millions')
plt.title('Sales by Quarter of Location')

# add as SNS style and increase figure size
sns.set_style("white")
sns.set_context({"figure.figsize": (4, 6)})
sns.despine(top=True, right=True)

# show the plot
plt.show()
