while True:
    try:
        x = int(input('SAT 1: '))
        y = int(input('SAT 2: '))
        z = int(input('GPA: '))  
        assert 400 <= x <= 1600
        assert 400 <= y <= 1600
        assert 10 <= z <= 40
    except ValueError:
        print("Not an integer! Please enter an integer.")
    except AssertionError:
        print("Please enter an integer for SAT scores between 400 and 1600 and for GPA between 10 and 40.")
    else:
        break

# Calculate scores based on SAT ranges
if x >= 1090 and y >= 1100:
    e = x / 1600 * 69 + y / 1600 * 15 + z
    g = x / 1600 * 75 + y / 1600 * 15 + z
elif x <= 1090 and y >= 1100:
    e = x / 1600 * 60 + y / 1600 * 15 + z
    g = x / 1600 * 60 + y / 1600 * 15 + z
elif x >= 1090 and y <= 1100:
    e = x / 1600 * 69 + y / 1600 * 0 + z
    g = x / 1600 * 75 + y / 1600 * 0 + z
elif x <= 1090 and y <= 1100:
    e = x / 1600 * 60 + y / 1600 * 0 + z
    g = x / 1600 * 60 + y / 1600 * 0 + z
else:
    print("Invalid entry")
    e = None
    g = None

if e is not None and g is not None:
    print('The score for public universities:', e)
    print('The score for private universities:', g)

