"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
 (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples:
      "The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""

def to_camel_case(text):
    t = []
    i = 0
    while(i != len(text)):
        if text[i] == '-' or text[i] == "_":
            t.append(text[i+1].upper())
            i+=2
        else:
            t.append(text[i])
            i+=1
    return "".join(t)
  
