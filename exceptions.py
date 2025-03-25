import sys
#there isn't much happening
#essentially instead of displayinga messy error it will export a nicer looking error telling you what is wrong.
#in this example that could be a string into an int or trying to divide by 0
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: invalid value")
    sys.exit(1)
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"x / y = {result}")