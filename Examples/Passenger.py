from Person import Person

class Passenger(Person):
    def __init__(self):
        Person.__init__(self)
        self.__seat = None
        self.__isDriver = False

    def getSeatPosition(self):
        return self.__seat

    def getIsDriver(self):
        return self.__isDriver

    def setSeatPosition(self, position):
        self.__seat = position

    def setIsDriver(self, isDriver):
        self.__isDriver = isDriver


