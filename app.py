# Imports
import pandas as pd
import numpy as np

# Load Data
store = pd.read_csv('dirty_cafe_sales.csv')
store.head()

# Clean Column Names
store.columns = store.columns.str.lower().str.replace(' ', '_')

# Check for Duplicates
store.duplicated().sum()

# Handle Nulls & Bad Values
store['item'].value_counts(dropna=False)
store.replace(['ERROR', 'UNKNOWN'], np.nan, inplace=True)

# Fix Data Types
cols_to_convert = ['quantity', 'price_per_unit', 'total_spent']
store[cols_to_convert] = store[cols_to_convert].apply(pd.to_numeric, errors='coerce')
store['transaction_date'] = pd.to_datetime(store['transaction_date'])

food = ['Salad', 'Cake', 'Sandwich', 'Cookie']
drink = ['Juice', 'Coffee', 'Smoothie', 'Tea']

store.loc[store['item'].isin(food), 'item_category'] = 'food'
store.loc[store['item'].isin(drink), 'item_category'] = 'drink'

store.to_csv('clean_cafe_sales.csv', index=False)