"""
Một bộ ba chỉ số (i,j,k) đôi một phân biệt được coi là bộ chỉ số đẹp nếu như ai + aj = ak.
Hãy cho biết có thể tìm được một bộ chỉ số đẹp nào đó hay không?
Bạn phải trả lời T truy vấn như vậy.

Input
  Dòng đầu tiên của file dữ liệu chứa một số nguyên dương T (1 <= T <= 50) - số truy vấn. Mỗi truy vấn có dạng như sau:
      + Dòng đầu tiên chứa một số nguyên dương n (3 < n < 100)
      + Dòng thứ hai chứa n số nguyên a1, a2, ..., an (|ai| < 10^6)

Sample Test
Input:
      3
      3
      1 2 3
      5
      0 1 2 6 9
      5
      3 1 7 -9 4

Output:
      YES
      NO
      YES
"""

def addsum(m, p):
    if len(p)<3:
        return "NO"
    for i in range(m-1):
        for j in range(i+1, m):
            q = p.copy()
            o = q[i]+q[j]
            del q[i]
            del q[j-1]
            if o in q:
                return "YES"
    return "NO"
 
n = int(input())
for f in range(n):
    m = int(input())
    p = [int(i) for i in input().split()]
    print(addsum(m, p))
