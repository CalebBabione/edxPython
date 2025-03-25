name = "Harry"
#Just like in C a string is just a fancy array.
#You can use an array at the end of the variable to pull only 1 letter
print(name[0])

#how can we store multiple names?
#well just use a 3d array silly!
names = ["Harry", "Ron", "Hermione"]
#below will only point to the individual names in the array. But an array of strings is just an array of arrays!
print(names[0])
#The below is how we will pull the n in "ron"
print(names[1][2])