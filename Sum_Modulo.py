"""
Cho trước 2 số nguyên N, K. Định nghĩa hàm F(N, K) như sau:F(N, K) = (1 % K) + (2 % K) + ... + (N % K)
(với X%Y là phép toán lấy số dư của phép chia số X cho số Y)
Yêu cầu: Tính F(N, K) và đưa ra phần dư của kết quả khi chia cho 10^9+7

Input:
      Dòng đầu tiên chứa số nguyên dương T – số lượng testcases   (1 <= T <= 10^5).
      T dòng tiếp theo, mỗi dòng chứa hai số nguyên dương N và K  (1 <= N <= K <= 10^18).

Output:
      Trên T dòng, dòng thứ i chứa kết quả của testcase thứ i.

Sample Test
Input:
      7
      657 164
      538 767
      47 613
      95 450
      477 86
      230 302
      486 907
Output:
      53465
      144991
      1128
      4560
      19403
      26565
      118341
"""

def modulo(n, k):
    p = n//k
    q = n%k
    return ( (k-1)*(k)//2*p + q*(q+1)//2 ) % (10**9+7)
 
n = int(input())
for i in range(n):
    n, k = [int(i) for i in input().split()]
    print(modulo(n, k))
