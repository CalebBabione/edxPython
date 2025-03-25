#define a new class
class Point():
    #this is a function that will be called everytime a new point was made
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 8)
print(p.x)
print(p.y)
#this is alot let's right down how this works.

#here we define the object
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        #add_passenger will check for vacant seats by calling open_seats
        #what that does is subtract the number of passengers from the max capacity
        #if it is = 0 then we cannot add any seats and will return false.
        #if the number of seats are greater than 0 then we have room and will return true and append the name to the 
        #passengers array at the beginning of the object.
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

#this is going to call the object and add the number of seats. in this case 3.
flight = Flight(3)

#afterwards we define the people
people = ["Harry", "Ron", "Hermione", "Ginny"]
#this is where the magic happens.
#we start wth a for loop the array is comping from people.
for person in people:
    #we need to know if we can add people now.
    #this will call a function in the object titled "add_passenger"
    success = flight.add_passenger(person)
    #depending on whether success is true or false.
    #it will print the outcome on the bottom
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")