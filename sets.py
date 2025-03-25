# Create an empty set
s = set()
#add some elements
s.add(1)
s.add(2)
s.add(3)
s.add(4)
#even though I've added 3 it will not show again because I've already added it.
#no element can appear twice in a set.
s.add(3)
print(s)
#remove elements
s.remove(2)
print(s)
#goot to know in the brackets you can use any function.
#this one is being used to determine the length of the "s" set and then adding it in. 
print(f"The set has {len(s)} elements.")