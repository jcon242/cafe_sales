import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

store.to_csv('clean_cafe_sales.csv', index=False)