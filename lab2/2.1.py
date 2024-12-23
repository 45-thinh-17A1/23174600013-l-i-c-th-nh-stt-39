import numpy as np
np.random.seed(0) 
temperatures = np.round(np.random.uniform(15, 35, 30), 2)
average_temperature = np.mean(temperatures)
print("Nhiệt độ hàng ngày:", temperatures)
print("Nhiệt độ trung bình trong tháng:", average_temperature)
# Xác định ngày có nhiệt độ cao nhất và thấp nhất
max_temp_day = np.argmax(temperatures) + 1 
min_temp_day = np.argmin(temperatures) + 1
temp_diff = np.diff(temperatures)
max_temp_diff_day = np.argmax(np.abs(temp_diff)) + 1
print(f"Ngày có nhiệt độ cao nhất: Ngày {max_temp_day}, Nhiệt độ: {temperatures[max_temp_day - 1]}°C")
print(f"Ngày có nhiệt độ thấp nhất: Ngày {min_temp_day}, Nhiệt độ: {temperatures[min_temp_day - 1]}°C")
print(f"Ngày có sự biến đổi nhiệt độ lớn nhất: Ngày {max_temp_diff_day}, Biến đổi: {np.abs(temp_diff[max_temp_diff_day - 1])}°C")
# Ngày có nhiệt độ > 20°C
days_above_20 = np.where(temperatures > 20)[0] + 1
temps_above_20 = temperatures[temperatures > 20]
selected_days = [5, 10, 15, 20, 25]
temps_selected_days = temperatures[np.array(selected_days) - 1]
days_above_avg = np.where(temperatures > average_temperature)[0] + 1
temps_above_avg = temperatures[temperatures > average_temperature]
temps_even_days = temperatures[1::2] 
temps_odd_days = temperatures[0::2]   
print("Ngày có nhiệt độ > 20°C:", days_above_20)
print("Nhiệt độ ngày đã chọn (5, 10, 15, 20, 25):", temps_selected_days)
print("Ngày có nhiệt độ trên trung bình:", days_above_avg)
print("Nhiệt độ ngày chẵn:", temps_even_days)
print("Nhiệt độ ngày lẻ:", temps_odd_days)

