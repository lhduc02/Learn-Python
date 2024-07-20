import random

def estimate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return (inside_circle / num_points) * 4

r = 1  # Bán kính hình tròn
num_points = 1000000  # Số lượng điểm ngẫu nhiên
estimated_area = estimate_pi(num_points) * (r ** 2)

print(estimated_area)
