#wow a dictionary array neato!
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

#def f(person):
#    return person["name"]
# without the key this will not work.
# it will sort a dictionary like it is a name.
#you create a functionso it can sort easily
#in this case F sorts by name
#people.sort(key=f)

#now that is rare and a long way of doing this.
# let's use a lambda function to do this :D

people.sort(key=lambda person: person["name"])

print(people)