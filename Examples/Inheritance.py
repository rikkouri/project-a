from Passenger import Passenger

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
