import numpy as np
efficiency = np.loadtxt('efficiency.txt', dtype=float)
shifts = np.loadtxt('shifts.txt', dtype=str)

print("Dữ liệu hiệu suất:", efficiency)
print("Dữ liệu ca làm việc:", shifts)
# Tạo mảng NumPy
np_efficiency = np.array(efficiency)
np_shifts = np.array(shifts)

print("Kiểu dữ liệu np_efficiency:", np_efficiency.dtype)
print("Kiểu dữ liệu np_shifts:", np_shifts.dtype)
# Hiệu suất trung bình theo ca
morning_efficiency = np_efficiency[np_shifts == 'Morning']
other_efficiency = np_efficiency[np_shifts != 'Morning']

print("Hiệu suất trung bình ca Morning:", np.mean(morning_efficiency))
print("Hiệu suất trung bình các ca khác:", np.mean(other_efficiency))
# Tạo structured array
workers = np.array(list(zip(np_shifts, np_efficiency)), dtype=[('shift', 'U10'), ('efficiency', 'float')])

# Sắp xếp theo hiệu suất
sorted_workers = np.sort(workers, order='efficiency')
print("Ca làm việc hiệu suất thấp nhất:", sorted_workers[0])
print("Ca làm việc hiệu suất cao nhất:", sorted_workers[-1])
