n = int(input())
r = input()
r = [*r]

p = []
for i in range(n):
    if i % 2 == 0:
        p.append('1')
    else:
        p.append('0')

q = []
for i in range(n):
    if i % 2 == 0:
        q.append('0')
    else:
        q.append('1')

c1 = 0
for i in range(n):
    if r[i] != p[i]:
        c1 += 1

c2 = 0
for i in range(n):
    if r[i] != q[i]:
        c2 += 1

print(min(c1, c2))
