from Passenger import Passenger
# For bonus
from Car import Car

class Driver(Passenger):
    def __init__(self, can_drive=['auto']):
        Passenger.__init__(self)
        self.__can_drive = can_drive

    def getCanDrive(self):
        return self.__can_drive

    def setCanDrive(self, can_drive):
        self.__can_drive = can_drive

# Bonus method
    def canDriveCar(self, car):
        #ShowOff
        if not isinstance(car, Car):
            raise TypeError
        elif car.getTransmission() in self.__can_drive:
            return True
        else:
            return False