# J4F

def triangle(n):
    for i in range(1, n+1):
        print(" " * (n-i) + " *" * i)

triangle(5)

"""
Output:
     *
    * *
   * * *
  * * * *
 * * * * *
"""
