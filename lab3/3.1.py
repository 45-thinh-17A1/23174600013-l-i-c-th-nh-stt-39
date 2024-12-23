import pandas as pd

# Đọc file CSV
stocks1 = pd.read_csv('stocks1.csv')
# Hiển thị 5 dòng đầu tiên
stocks1.head()
# Kiểm tra kiểu dữ liệu của mỗi cột
stocks1.dtypes
# Xem thông tin tổng quan của DataFrame
stocks1.info()
