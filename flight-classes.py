# Create a Class Flight
class Flight():
    # save data of the flight in (__init__) model
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    # Add passengers to the flight by (add_passenger) model
    def add_passenger(self, name):
        # first chick if there is a seat for person in the flight by (seat) model
        if not self.seat():
            return False
        self.passengers.append(name)
        return True
    # model to chick how many seats there is ?
    def seat(self):
        return self.capacity - len(self.passengers)

# Let's try our class/model ( Flight )
# create a flight 
flight = Flight(3) # the flight has capacity = 3
# create list of pepole
people = ["Baha", "Anna","Sara", "Jhin"]
# add every person in pepole to the flight
for person in people:
    if flight.add_passenger(person): # True
        print(f"The person >> {person} << has been added to the flight succesfully. ")
    else: # False
        print(f"There is no seat avalable for the person >> {person} << . ")