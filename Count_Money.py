"""
Bạn đi làm thêm ở một cửa hàng tạp hóa và được giao công việc là tính và trả tiền. Nhưng những người mua hàng ở đây lại có thói quen rất lạ.
Nếu bạn muốn được bo thêm thì bạn phải trả lời số lượng cách để trả tiền chính xác cho món đồ của người mua bằng các tờ 1, 2 và 5 đồng.
Bạn cần tiền và cần trả lời nhanh nhất có thể, nếu không người khách sẽ không bo cho bạn nữa.

Yêu cầu: Hãy viết một chương trình để tính đúng số cách trả tiền.

Input:
Số tiền mà người mua hàng mua.

Output:
In ra số cách trả tiền.
"""

# Code by Chat GPT

def count_payment_methods(amount):
    # Tạo một mảng để lưu số cách trả tiền cho từng số tiền
    dp = [0] * (amount + 1)

    # Khởi tạo giá trị cơ sở
    dp[0] = 1

    # Duyệt qua từng mệnh giá tiền tệ
    denominations = [1, 2, 5]
    for coin in denominations:
        # Tính số cách trả tiền cho từng số tiền
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    # Trả về số cách trả tiền cho số tiền mua hàng
    return dp[amount]

# Đọc số tiền mua hàng từ input
amount = int(input())

# Gọi hàm count_payment_methods và in ra kết quả
result = count_payment_methods(amount)
print(result)
