import numpy as np

# Đọc dữ liệu từ file CSV
data = np.genfromtxt('diem_hoc_phan.csv', delimiter=',', dtype=None, encoding='utf-8', skip_header=1)

# Chuyển dữ liệu điểm học phần thành mảng số thực
scores = np.array(data[:, 2:], dtype=float)  # Chỉ lấy cột HP1, HP2, HP3
print("Dữ liệu điểm số học phần:\n", scores)
# Hàm quy đổi điểm sang điểm chữ
def grade_letter(score):
    if 8.5 <= score <= 10:
        return 'A'
    elif 8.0 <= score < 8.5:
        return 'B+'
    elif 7.0 <= score < 8.0:
        return 'B'
    elif 6.5 <= score < 7.0:
        return 'C+'
    elif 5.5 <= score < 6.5:
        return 'C'
    elif 5.0 <= score < 5.5:
        return 'D+'
    elif 4.0 <= score < 5.0:
        return 'D'
    else:
        return 'F'

# Áp dụng hàm quy đổi
grades = np.vectorize(grade_letter)(scores)
print("Điểm tín chỉ:\n", grades)
# Tách từng học phần
hp1 = scores[:, 0]
hp2 = scores[:, 1]
hp3 = scores[:, 2]

# Phân tích thống kê
print("HP1 - Tổng:", np.sum(hp1), "Trung bình:", np.mean(hp1), "Độ lệch chuẩn:", np.std(hp1))
print("HP2 - Tổng:", np.sum(hp2), "Trung bình:", np.mean(hp2), "Độ lệch chuẩn:", np.std(hp2))
print("HP3 - Tổng:", np.sum(hp3), "Trung bình:", np.mean(hp3), "Độ lệch chuẩn:", np.std(hp3))
# Đếm số lượng từng loại điểm
unique, counts = np.unique(grades, return_counts=True)
grade_summary = dict(zip(unique, counts))
print("Phân tích điểm tổng hợp:\n", grade_summary)

