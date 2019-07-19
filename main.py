# Python code
# A calculator with premade equations
# User inputs with an immediate conversion to int

x = int(input('SAT 1: '))
y = int(input('SAT 2: '))
z = int(input('GPA: '))

# The designated equations

if x >= 1090 and y >=1100:
    e = x / 1600 * 69 + y / 1600 * 15 + z
    g = x / 1600 * 75 + y / 1600 * 15 + z
    if x <= 1090 and y >= 1100:
        e = x / 1600 * 60 + y / 1600 * 15 + z
        g = x / 1600 * 60 + y / 1600 * 15 + z
    elif x >= 1090 and y <= 1100:
        e = x / 1600 * 69 + y / 1600 * 0 + z
        g = x / 1600 * 75 + y / 1600 * 0 + z
    elif x <= 1090 and y <=1100:
        e = x / 1600 * 60 + y / 1600 * 0 + z
        g = x / 1600 * 60 + y / 1600 * 0 + z
    print ('The score for public universities:', e)
    print ('The score for private universities:', g)
else: 
    print("Invalid entry")