class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def addPassenger(self,name):
        if not self.available_seat():
            return False
        self.passengers.append(name)
        return True


    def available_seat(self):
        return self.capacity - len(self.passengers)

    


flight = Flight(3)


people = ["harry","Ron","Harmanny","Ginny"]

for person in people:
    if flight.addPassenger(person):
        print(f"We added {person} to the flight succesfully")
    else:
        print(f"no available  seat for {person}")

