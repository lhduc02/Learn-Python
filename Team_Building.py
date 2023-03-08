"""
Once, the Sun* company organizes team building for x male and y female friends in a project.
To play a game, the game director picks out teams, each team includes z people and includes no less than one girl and no less than four male friends.
Asking how many how to create a team? Each member does not belong to 2 or more teams.

Input:    Three integers x, y, z (x ≤ 4 ≤ 30, 1 ≤ y ≤ 30, 5 ≤ z ≤ x + y).

Output:   The number of ways to create teams.
"""

import math
x, y, z = [int(i) for i in input().split()]
s = 0
for i in range(4, min(z, x+1)):
    if x-i>=0 and z-i>=0 and y-z+i>=0:
        a = math.factorial(x)//math.factorial(i)//math.factorial(x-i)
        b = math.factorial(y)//math.factorial(z-i)//math.factorial(y-z+i)
        s += a*b
print(int(s))
