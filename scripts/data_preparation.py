import os
import pandas as pd

df = pd.read_csv('data/processed/car_sales_data_final.csv')
df.info()
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns    


def binary_columns(dataframe):
    binary_cols = [col for col in numeric_cols if df[col].dropna().isin([0, 1]).all()]
    return binary_cols
def continuous_columns(dataframe):
    continuous_columns = [col for col in numeric_cols if col not in binary_columns(dataframe)]
    return continuous_columns
def categorical_columns(dataframe):
    categorical_columns = dataframe.select_dtypes(include=['object', 'category']).columns.tolist()
    return categorical_columns

binary_cols = binary_columns(df)
print("Binary columns:", binary_cols)
continuous_cols = continuous_columns(df)
print("Continuous columns:", continuous_cols)
categorical_cols = categorical_columns(df)
print("Categorical columns:", categorical_cols)