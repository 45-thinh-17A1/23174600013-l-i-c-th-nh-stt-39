# Tạo MultiIndex cho DataFrame
stocks.set_index(['date', 'symbol'], inplace=True)
# Tính giá trung bình và volume trung bình cho mỗi ngày, mỗi mã chứng khoán
grouped_data = stocks.groupby([stocks.index.get_level_values('date'), stocks.index.get_level_values('symbol')])[['open', 'high', 'low', 'close', 'volume']].mean()
# Sắp xếp dữ liệu theo ngày và mã chứng khoán
grouped_data.sort_index(inplace=True)
grouped_data.head()
