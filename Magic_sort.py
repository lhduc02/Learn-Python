"""
Linh được thầy giáo đưa cho 1 dãy N số tự nhiên. Thầy yêu cầu Linh sắp xếp lại N số này theo quy tắc sau:
    + Sắp xếp từ trái qua phải sao cho tổng các chữ số của các số này tăng dần.
    + Nếu các số có tổng các chữ số bằng nhau thì chúng được sắp xếp tăng dần theo giá trị.
Bạn có thể giúp Linh vượt qua thử thách này không?

Input:  Dòng thứ nhất là số tự nhiên N(1≤n≤100).
        Dòng thứ hai là dãy gồm N số tự nhiên, giá trị không vượt qua 10^5, phân tách bởi dấu cách.

Output: Dãy N số phân tách bởi dấu cách đã sắp xếp xong.

Ví dụ:
    Input
    3
    12 11 21

    Output
    11 12 21
"""

n = int(input())
p = [int(i) for i in input().split()]
p.sort()
ss = 0
while(ss < 45):
    for i in p:
        si = [eval(i) for i in [*str(i)]]
        if ss == sum(si):
            print(i, end = " ")
    ss += 1
