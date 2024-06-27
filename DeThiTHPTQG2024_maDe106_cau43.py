# Câu 43  mã đề 106 - Đề thi THPT Quốc gia 2024 môn Toán

import math

def func(i):
    return 2/(i**3) + math.log((i+3)/(i-3))

cnt = 0
for i in range(-100000, 2100):
    a = i-2024
    b = 6*i-27
    try:
        f = func(a) + func(b)
    except:
        continue
    if f >= 0:
        cnt += 1
print(cnt)

# Answer: 360
