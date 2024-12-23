# Tạo Pivot Table
pivot_table = stocks.pivot_table(values='close', index='date', columns='symbol', aggfunc='mean')
pivot_table['total_volume'] = stocks.groupby('symbol')['volume'].sum()
pivot_table = pivot_table.sort_values(by='total_volume', ascending=False)
pivot_table.head()
