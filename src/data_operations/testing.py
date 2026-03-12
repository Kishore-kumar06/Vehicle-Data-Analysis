import os
import pandas as pd


path = r"D:\Project\Vehicle-Data-Analysis\source_files\raw_files\raw_vehicle_data - Copy.csv"

data = pd.read_csv(path, encoding='UTF-8')

# # Understaning Data Sets
# print(data.head())
# print(data.info())
# print(data.describe())

# Validating data set
print(data.columns)
print(data.shape)
print(data.dtypes)


# # Standardizing Columns
# data.columns = (data.columns.str.lower().str.strip().str.replace(' ', '_').str.replace('-','_'))


# # Removing irrelevant columns or rows
# data = data.drop(columns=['Bunk']) # columns
# data = data.drop(index=[1,2]) # rows


# # remove duplicate
# duplicate_data = data.duplicated() # finding duplicates
# for i, d in enumerate(duplicate_data):
#     if d == True:
#         print(i, d)

# duplicate_removed = data.drop_duplicates() # removing duplicates
# print(duplicate_removed)


# # remove empty columns or rows
# empty_records = data.isna().sum()
# data[['Other cost','Petrol Cost','Quantity']] = data[['Other cost','Petrol Cost','Quantity']].fillna(0)


# # Standardizing data values
# '''
# remove white spaces
# capitalize/title case the values
# replace invalid characters
# '''


# data = data.apply(lambda x: x.str.strip().str.title() if x.dtype == 'object' else x)
# print(data.tail())


# # standardize datatypes  # NA values cannot be converted
# print(data.dtypes)
# data[['Other cost','Petrol Cost']] = data[['Other cost','Petrol Cost']].astype(int) # integers
# data["Date"] = pd.to_datetime(data["Date"], yearfirst=True) # date
# data['Total Expenses'] = pd.to_numeric(data['Total Expenses'], 'coerce')


# # Handle Outliers
''' 
remove
cap
investigate
'''
# print(data.describe())


# # Check for uniques values especially id column
# data['Bunk'] = data['Bunk'].is_unique
# data['Bunk'] = data['Bunk'].unique()

# # Check Data Consistency 
# print(data['Petrol Cost'].where(data['Petrol Cost'] > 0))


# Sorting data

# data['Total Expenses'] = data.sort_values(by='Total Expenses', ascending=False)
# print(data['Total Expenses'])

