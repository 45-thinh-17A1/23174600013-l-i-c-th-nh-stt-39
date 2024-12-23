# Kiểm tra dữ liệu null trong DataFrame
stocks1.isnull().sum()
# Thay thế Null trong cột 'high' bằng giá trị trung bình của cột đó
stocks1['high'].fillna(stocks1['high'].mean(), inplace=True)
# Thay thế Null trong cột 'low' bằng giá trị trung bình của cột đó
stocks1['low'].fillna(stocks1['low'].mean(), inplace=True)
# Kiểm tra lại dữ liệu null
stocks1.isnull().sum()
