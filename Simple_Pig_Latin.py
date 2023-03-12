"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool')     # igPay atinlay siay oolcay
pig_it('Hello world !')         # elloHay orldway !
"""

def pig_it(text):
    text = text.split(" ")
    t = []
    khdb = ['?', '!', '.']
    for i in text:
        if '?' not in i and '!' not in i and '.' not in i:
            t.append(i[1:] + i[0] + "ay")
        else:
            t.append(i)
    return " ".join(t)
