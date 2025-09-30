product_performance = df_orders.groupby('product')['amount'].agg(['sum', 'mean', 'count'])
print(product_performance)
