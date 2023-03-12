"""
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram.
Return True if it is, False if not. Ignore numbers and punctuation.
"""

def is_pangram(s):
    p = []
    q = []
    for i in range(65, 91):
        p.append(chr(i))
    for i in range(97, 123):
        q.append(chr(i))

    s = [*s]
    for i in range(26):
        if p[i] not in s and  q[i] not in s:
            return False
    return True
