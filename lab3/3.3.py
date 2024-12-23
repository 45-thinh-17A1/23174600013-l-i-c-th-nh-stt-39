# Đọc file CSV thứ hai
stocks2 = pd.read_csv('stocks2.csv')
# Gộp hai DataFrame
stocks = pd.concat([stocks1, stocks2], ignore_index=True)
# Tính giá trung bình cho mỗi ngày
stocks['date'] = pd.to_datetime(stocks['date'])  # Đảm bảo cột 'date' là kiểu datetime
stocks_grouped = stocks.groupby('date')[['open', 'high', 'low', 'close']].mean()
# Hiển thị 5 dòng đầu tiên của kết quả
stocks_grouped.head()
