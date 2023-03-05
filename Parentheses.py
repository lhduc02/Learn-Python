"""
Given a string containing only characters (, ), [, ] {, }.
Write a program that check whether the string is correct in expression.
Example:
      ([]{()}()[]): correct
      ([]{()]()[]): incorrect

Input: One line contains the string (the length of the string is less than or equal to 10^6)
Output: Write 1 if the sequence is correct, and write 0, otherwise

Example:
      input: (()[][]{}){}{}[][]({[]()})
      output: 1
"""

p = input()
while(1):
    if '()' in p:
        p = p.replace('()', '')
    elif '[]' in p:
        p = p.replace('[]', '')
    elif '{}' in p:
        p = p.replace('{}', '')
    else:
        break
if len(p) > 0:
    print(0)
else:
    print(1)
