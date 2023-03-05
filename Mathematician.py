"""
Bi là một nhà toán học trẻ, rất nổi tiếng ở IT. Thật không may, Lema không nghĩ như vậy. Để khiến Lema thay đổi ý định, Bi sẵn sàng giải bất kỳ bài toán nào. Sau một hồi suy nghĩ, Lema yêu cầu Roma tìm xem có bao nhiêu số "số n, modulo m".
+ Nó có thể nhận được bằng cách sắp xếp lại các chữ số của số n.
+ Nó không có bất kỳ số 0 nào đứng đầu.
+ Số còn lại sau khi chia số x cho m bằng 0.
Hãy giúp Bi giải quyết bài toán
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
