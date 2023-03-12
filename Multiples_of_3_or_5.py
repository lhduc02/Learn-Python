"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0 (for languages that do have them).
Note: If the number is a multiple of both 3 and 5, only count it once.
"""

def solution(number):
    if number < 0:
        return 0
    number -= 1
    count = 0
    n5 = number//5
    n3 = number//3
    n15 = number//15
    return int(3*n3*(n3+1)//2 + 5*n5*(n5+1)//2 - 15*n15*(n15+1)//2)
