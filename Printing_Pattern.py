"""
Print a pattern of numbers from 1 to n as shown below. Each of the numbers is separated by a single space.

Sample Input:
    5
Sample Output:
    5 5 5 5 5 5 5 5 5
    5 4 4 4 4 4 4 4 5
    5 4 3 3 3 3 3 4 5
    5 4 3 2 2 2 3 4 5
    5 4 3 2 1 2 3 4 5
    5 4 3 2 2 2 3 4 5
    5 4 3 3 3 3 3 4 5
    5 4 4 4 4 4 4 4 5
    5 5 5 5 5 5 5 5 5
"""

n = int(input())
mt = []
for i in range(2*n-1):
    a = [0 for i in range(2*n-1)]
    mt.append(a)

dem = n
while(dem != 0):
    for i in range(n-dem, n+dem-1):
        for j in range(n-dem, n+dem-1):
            mt[i][j] = dem
    dem -= 1

for i in range(2*n-1):
    for j in range(2*n-1):
        print(mt[i][j], end = " ")
    print()
