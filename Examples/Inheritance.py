from Human import Human
from Person import Person
from Passenger import Passenger

def inheritance_one():
    car = {}

    driver = Passenger()
    driver.setName('Bob')
    driver.setAge(30)
    driver.setSeatPosition(0)
    driver.setIsDriver(True)

    passenger = Passenger()
    passenger.setName('Jim')
    passenger.setAge(40)
    passenger.setSeatPosition(1)

    car['driver'] = driver
    car['passenger'] = passenger

    for key in car:
        occupant = car[key]
        print('Occupant ' + occupant.getName() + (', driving' if occupant.getIsDriver() else ', passenger' ) )


def inheritance_two():
    car = {}

    driver = Passenger()
    driver.setName('Bob')
    driver.setAge(30)
    driver.setSeatPosition(0)
    driver.setIsDriver(True)

    passenger = Passenger()
    passenger.setName('Jim')
    passenger.setAge(40)
    passenger.setSeatPosition(1)

    person = Person()
    person.setName('Jack')
    person.setAge(25)

    car['driver'] = driver
    car['passenger'] = passenger
    car['otherpassenger'] = person

    for key in car:
        occupant = car[key]
        try:
            print('Occupant ' + occupant.getName() + (', driving' if occupant.getIsDriver() else ', passenger' ) )
        except AttributeError as ae:
            if isinstance(occupant, Human):
                print('Occupant ' + occupant.getName() )
            else:
                print( 'Error : ' + ae.message)

# inheritance_one()
inheritance_two()