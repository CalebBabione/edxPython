#this for loop automates it so you don't have to do the math to make it end :D
#essentially it goes through the whole list and for each instance it will chang i to be the next num in the sequence.
#for i in [0, 1, 2, 3, 4, 5]:
#    print(i)
#python also has ranges :D
#this saves us the trouble of having to type each number ourselves.
for i in range(6):
    print(i)
#you can take already created arrays to get this job done.
#and it will go in a range of 0 - the ammount of stuff you have - 1.
#it will also automatically change the variable of the name.
names = ["Harry", "Ron", "Hermione"]
for name in names:
    print(name)
#This is definitely cool and all but lets test.
# since a string is a name theoretically it can just print the litters of a string
#theoretically if this works it will output the words in the name "Harry"
for name in names[0]:
    print(name)
#IT WAS A SUCCESS!!!!!