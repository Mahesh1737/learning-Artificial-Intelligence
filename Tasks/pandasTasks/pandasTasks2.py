import pandas as pd
import numpy as np

# Example dataframe (you can replace with your own dataset)
df = pd.DataFrame({
    'customer_name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Bob'],
    'category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics', 'Clothing'],
    'order_value': [250, 150, 300, 100, 400, 220],
    'discount': [0.10, 0.20, 0.25, 0.05, 0.30, 0.18],
    'order_date': pd.to_datetime(['2025-09-01', '2025-09-15', '2025-09-20', 
                                   '2025-08-30', '2025-09-25', '2025-09-18']),
    'profit': [50, 20, 100, 10, 150, 60]
})

print("Initial Data:")
print(df)

#Combine different selection methods

# High-value orders (>200) in Electronics
# high_value_elec = df[(df['order_value'] > 200) & (df['category'] == 'Electronics')]
# print("\nHigh-value Electronics Orders:\n", high_value_elec)

#Orders from last 30 days with discount > 15%
# recent_orders = df[(df['order_date'] >= (df['order_date'].max() - pd.Timedelta(days=30))) & 
#                    (df['discount'] > 0.15)]
# print("\nRecent Orders with discount > 15%:\n", recent_orders)

#Subset with selected columns

# subset_df = df[['customer_name', 'order_value', 'profit']]
# print("\nSubset with selected columns:\n", subset_df)



#Data Inspection

# def data_quality_report(df):
#     report = {}
#     report['shape'] = df.shape
#     report['dtypes'] = df.dtypes.to_dict()
#     report['missing_values'] = df.isnull().sum().to_dict()
#     report['missing_percentage'] = (df.isnull().mean()*100).to_dict()
#     report['stat_summary'] = df.describe(include='all').to_dict()
#     report['unique_counts'] = df.nunique().to_dict()
#     return report

# report = data_quality_report(df)
# print("\nData Quality Report:")
# for k,v in report.items():
#     print(f"{k}:\n{v}\n")

