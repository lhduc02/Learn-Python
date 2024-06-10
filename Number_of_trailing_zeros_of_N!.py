"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.
N! = 1 * 2 * 3 *  ... * N
Be careful 1000! has 2568 digits...

Examples:
 ________________________________________________________________________
|  N  |  Product                      |  N factorial  |  Trailing zeros  |
|------------------------------------------------------------------------|
|  6  |  1*2*3*4*5*6	                |  720	        |  1               |
|  12 |  1*2*3*4*5*6*7*8*9*10*11*12	  |  479001600    |  2               |
|________________________________________________________________________|

"""

import math
def zeros(n):
    if n==0:
        return 0
    a = math.floor(math.log(n)/math.log(5))
    count = 0
    for i in range(1, a+1):
        count += n//(5**i)
    return count
