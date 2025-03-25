#this is to import functions from other files
#from "functions" i want to import square
#from functions import square
#for i in range (10):
#    print(f"The square of {i} is {square(i)}")

#now there is a different way to do this it is useful if you need to import multiple funcitons from one file.
#this will import the whole file.
import functions

#however. Now we need to specify that the square function we're calling is from the functions file by appending %filename%.%functionname%
for i in range (10):
    print(f"The square of {i} is {functions.square(i)}")