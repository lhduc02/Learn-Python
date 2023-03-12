"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:
rgb(255, 255, 255)    # returns FFFFFF
rgb(255, 255, 300)    # returns FFFFFF
rgb(0,0,0)            # returns 000000
rgb(148, 0, 211)      # returns 9400D3
"""

conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
 
 
# function which converts decimal value
# to hexadecimal value
def decimalToHexadecimal(decimal):
    if decimal < 0:
        decimal = 0
    elif decimal > 255:
        decimal = 255
    hexadecimal = ''
    while(decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16
    hexadecimal = str(hexadecimal)
    if hexadecimal == "":
        return "00"
    if len(hexadecimal) == 1:
        hexadecimal = "0" + hexadecimal
    return hexadecimal

def rgb(r, g, b):
    return str(decimalToHexadecimal(r)) + str(decimalToHexadecimal(g)) + str(decimalToHexadecimal(b))
