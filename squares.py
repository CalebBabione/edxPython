#this is to import functions from other files
#from "functions" i want to import square
from functions import square

for i in range (10):
    print(f"The square of {i} is {square(i)}")