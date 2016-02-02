from Car import Car
from Passenger import Passenger
from Person import Person

# Create an instance of Car with the default empty occupant list
mycar = Car( make='Kia', model='Sportage')

# Create the driver and passenger, both instances of Passenger
driver = Passenger()
driver.setName('Paul')
driver.setAge(43)
driver.setIsDriver(True)
driver.setSeatPosition(0)

passenger = Passenger()
passenger.setName('Bob')
passenger.setAge(23)
passenger.setIsDriver(False)
passenger.setSeatPosition(1)

# Create a Person object
person = Person()
person.setName('Charlie')
person.setAge(35)

# Add both our passengers
mycar.addOccupant(driver)
mycar.addOccupant(passenger)

# And then our person. The addOccupant method does not specify an object type.
# We could add some handling inside the Car class to raise an error if
# the occupant to be added does not match an expected type.
mycar.addOccupant(person)

print( 'The ' + mycar.getMake() + ' ' + mycar.getModel() + ' is transporting ')
for occupant in mycar.getOccupants():
    # We'll hit an (unhandled) exception here when we try to call a nonexistent method on the Person object
    print(occupant.getName() + (', driving' if occupant.getIsDriver() else ', passenger'))
