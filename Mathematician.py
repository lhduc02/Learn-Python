"""
Số x được coi là "số n, modulo m" nếu:
    + Nó có thể nhận được bằng cách sắp xếp lại các chữ số của số n.
    + Nó không có bất kỳ số 0 nào đứng đầu.
    + Số còn lại sau khi chia số x cho m bằng 0.
Hãy đếm số lượng số x
"""
import itertools
n, m = [int(i) for i in input().split()]
count = 0
test = []
p = list(str(n))
t = list(itertools.permutations(p))
for i in t:
    i = list(i)
    check = int("".join(i))
    if check // 10**(len(p)-1)>=1:
        test.append(check)
test = set(test)
test = list(test)
for i in test:
    if i%m==0:
        count+=1
print(count)
