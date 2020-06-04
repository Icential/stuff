import math
import string

def br():
    print('===============================================')
def inVar(var):
    print('Enter ' + var + ' variable value here:')
    var = input()
    if var in list(string.ascii_lowercase):
        print('No letters allowed!')
        exit()
    else:
        return int(var)
def basiCheck(foo):
    if len(str(foo)) > 7:
        print('Variable value too big!')
        exit()
    if '-' in str(foo):
        print('Invalid variable value!')
        exit()
def pytha(var, var0, res):
    var = inVar(var)
    basiCheck(var)
    br()
    var0 = inVar(var0)
    basiCheck(var0)
    br()
    if res is 'c':
        finRes = math.sqrt(var**2 + var0**2)
        return print(res + ' = ' + str(finRes))
    else:
        finRes = math.sqrt(var0**2 - var**2)
        return print(res + ' = ' + str(finRes))
def sina(var, var0, var1, res):
    var = inVar(var)


print('Select a math equation:')
print('a. Pythagoras Theorem\nb. Sine Rule (Angles)')
begin = input()
br()
if begin is 'a':
    print('Pythagoras Theorem: c^2 = a^2 + b^2')
    print('What variable are you looking for? (a, b, c)')
    start = input()
    br()
    if start is 'a':
        pytha('b', 'c', 'a')
    elif start is 'b':
        pytha('a', 'c', 'b')
    elif start is 'c':
        pytha('a', 'b', 'c')
    else:
        print(start + ' is not an appropriate variable!')
elif begin is 'b':
    print('Sine Rule (Angles): (sin A°)/a = (sin B°)/b = (sin C°)/c')
elif begin is 'c':
    print('Sine Rule (Area): 0.5ab * sin C°')
    print('What variable are you looking for? (Area, a, b, C°')
    start = input()
    br()
    if start is 'Area':
        sina()
    elif start is 'a':
        sina()
    elif start is 'b':
        sina()
    elif start is 'C' or 'c' or 'C°' or 'c°':
        sina()
    else:
        print(start + ' is not an appropriate variable!')
else:
    'Invalid input!'
    exit()