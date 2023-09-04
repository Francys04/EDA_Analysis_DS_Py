from src.config import df_house
import pandas as pd

"""Overall, this code defines two functions: one for importing housing data from a URL and another for calculating 
various statistics for each column in the housing dataset. The statistics are stored in a DataFrame for analysis."""

"""This function takes a URL as input, reads a CSV file from that URL, assigns it to a new DataFrame called df_house, 
and drops the 'Id' column. It then returns this DataFrame."""

"""In summary, this function systematically calculates and compiles various statistics for each column in a DataFrame, 
whether the column contains numeric or non-numeric data. The statistics include count, missing values, unique values, 
data type, numeric flag, mode, mean, minimum, quartiles, median, maximum, standard deviation, skewness, and kurtosis. 
These statistics are stored in a new DataFrame for further analysis."""


def import_housig_data(url):
    df_house = pd.read_csv(url)
    df_house.drop(columns=['Id'], inplace=True)
    return df_house


print(df_house.head())


def unistats(df_house):  # Define the function unistats that takes the DataFrame df_house as an input parameter.
    output_df_h = pd.DataFrame(columns=['Count', 'Missing', 'Unique', 'Dtype', 'Numeric', 'Mode', 'Mean', 'Min', '25%',
                                        'Median', '75%', 'Max', 'Std', 'Skew', 'Kurt'])
    for col in df_house:
        if pd.api.types.is_numeric_dtype(df_house[col]):
            output_df_h.loc[col] = [df_house[col].count(),
                                    df_house[col].isnull().sum(),
                                    df_house[col].nunique(),
                                    df_house[col].dtype,
                                    pd.api.types.is_numeric_dtype(df_house[col]),
                                    df_house[col].mode().values[0],
                                    df_house[col].mean(),
                                    df_house[col].min(),
                                    df_house[col].quantile(0.25),
                                    df_house[col].median(),
                                    df_house[col].quantile(0.75),
                                    df_house[col].max(),
                                    df_house[col].std(),
                                    df_house[col].skew(),
                                    df_house[col].kurt()]
        else:
            output_df_h.loc[col] = [df_house[col].count(),
                                    df_house[col].isnull().sum(),
                                    df_house[col].nunique(),
                                    df_house[col].dtype,
                                    pd.api.types.is_numeric_dtype(df_house[col]),
                                    df_house[col].mode().values[0],
                                    '-',
                                    '-',
                                    '-', '-', '-', '-', '-', '-', '-']

    return output_df_h.sort_values(by=['Numeric', 'Unique'], ascending=False)

# print(df_house.info())
# pd.set_option('display.max_rows', 100)
# pd.set_option('display.max_columns', 200)

# unistats(df_house)
