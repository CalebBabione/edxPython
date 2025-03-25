#input will always return a string.
#will need type cast to turn "n" into an INT
#n = input("Number: ")
#the below text will turn the "input" into an INT
n = int(input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")