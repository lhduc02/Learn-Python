"""
Nay Lema sẽ là người đánh đố Bi. Lema cho một chuỗi ký tự bao gồm các ký tự từ “a” đến “z” trong bảng chữ cái và các chữ số từ 0 đến 9.
Nhiệm vụ mà Lema giao cho Bi là tính tổng các số có mặt trong chuỗi ký tự đó và kiểm tra xem đó có phải là số nguyên tố hay không,
nếu là số nguyên tố thì in ra “Yes”, còn không phải thì in ra “No”. Lema đảm bảo cho tổng các số không vượt quá giới hạn 10^9.

Input:
      + Dòng đầu tiên nhập vào số nguyên T là số bộ Test.
      + T dòng tiếp theo, mỗi dòng nhập vào một chuỗi ký tự không chứa dấu cách,
      gồm các ký tự chữ cái thường từ “a” - “z” và các số từ 0 – 9 với độ dài không quá 10^4
Constraints:
      T≤100
      1 <= Ti <= 10^4
Output:
      In ra trên T dòng, mỗi dòng in ra kết quả của chuỗi đó
      
Sample Test
Input:
      2
      1abc2x30yz67
      a7 
Output:
      No
      Yes
"""

import math
def snt(n):
    if n <= 1:
        return "No"
    if n == 2:
        return "Yes"
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n%i==0:
            return "No"
    return "Yes"
 
def tong_so(a):
    a = [*a]
    a.insert(0, '*')
    s = 0
    so = 0
    j = 0
    for i in range(len(a)-1, -1, -1):
        if a[i].isnumeric():
            so += int(a[i])*(10**j)
            j+=1
        else:
            s += so
            so = 0
            j = 0
    return s
 
t = int(input())
for i in range(t):
    a = input()
    print(snt(tong_so(a)))
