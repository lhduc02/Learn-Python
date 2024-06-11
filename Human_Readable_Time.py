"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

  Example 1:
Input:   60
Output:  00:01:00

  Example 2:
Input:   86399
Output:  23:59:59
"""

def make_readable(seconds):
    h = seconds//3600
    if h <= 9:
        h = "0" + str(h)
    else:
        h = str(h)
    t = seconds%3600
    
    m = t//60
    if m <= 9:
        m = "0" + str(m)
    else:
        m = str(m)
    
    s = t%60
    if s <= 9:
        s = "0" + str(s)
    else:
        s = str(s)
    
    ans = h + ":" + m + ":" + s
    return ans
