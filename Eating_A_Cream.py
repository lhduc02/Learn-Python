"""
Trong thời gian thất nghiệp trước khi đi làm IT, An đã tậu một xe kem, thử buôn bán một phen.
Khi anh đỗ xe trước cổng trường cấp 2 liền có 1 loạt các em đến đứng xếp hàng mua.
Trong tay các em là các tờ tiền có mệnh giá 25 đồng, 50 đồng, 100 đồng. Giá một que kem là 25 đồng.
Trong tay An hiện không có đồng nào. Hỏi An có thể bán kem và trả tiền thừa đúng cho từng người và đúng thứ tự đã xếp hàng được không?

Input:
      + Dòng đầu tiên là n (1 ≤ n ≤ 10^5) — số lượng các em trong hàng.
      + Dòng tiếp theo là n số nguyên, mỗi 25, 50 hoặc 100 — mệnh giá các tờ tiền. Các số sắp theo thứ tự từ đầu hàng đến cuối hàng.
Output:
      In ra YES (không có dấu ngoặc kép) nếu An có thể bán kem và trả tiền thừa đúng cho từng người và đúng thứ tự đã xếp hàng, không thì in ra NO.

Sample Test 1
Input:
      4
      25 25 50 50
Output:
      YES

Sample Test 2
Input:
      4
      50 50 25 25
Output:
      NO
"""

def icream(n, p):
    if p[0]!=25:
        return "NO"
    else:
        s = []
        s.append(25)
        c = 1
        for i in range(1, n):
            if p[i]==25:
                s.append(25)
            elif p[i]==50:
                if 25 in s:
                    s.remove(25)
                    s.append(50)
                elif 25 not in s:
                    return "NO"
            elif p[i]==100:
                if 25 in s and 50 in s:
                    s.remove(25)
                    s.remove(50)
                    s.append(100)
                else:
                    return "NO"
        return "YES"
 
n = int(input())
p = [int(i) for i in input().split()]
print(icream(n, p))
