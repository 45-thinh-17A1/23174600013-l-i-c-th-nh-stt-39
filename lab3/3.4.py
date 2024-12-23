# Đọc file companies.csv
companies = pd.read_csv('companies.csv')
# Hiển thị 5 dòng đầu tiên của companies
companies.head()
# Kết hợp dữ liệu stocks và companies dựa trên cột 'symbol'
merged_data = pd.merge(stocks, companies, on='symbol', how='inner')
# Tính giá đóng cửa trung bình cho mỗi công ty
average_close = merged_data.groupby('name')['close'].mean()
# Hiển thị 5 công ty đầu tiên
average_close.head()
