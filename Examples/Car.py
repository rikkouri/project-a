from Passenger import Passenger

class Car:
    def __init__(self, make, model, occupants=None):
        self.__make = make
        self.__model = model
        if occupants == None:
            self.__occupants = []
        else:
            self.__occupants = occupants

    def setMake(self, make):
        self.__make = make

    def setModel(self, model):
        self.__model = model

    def setOccupants(self, occupants):
        self.__occupants = occupants

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model

    def getOccupants(self):
        return self.__occupants

    def addOccupant(self, occupant):
        # We could add a check here to raise an exception if the supplied
        # object is not of the required type
        # if not isinstance(occupant, Passenger):
        #     raise TypeError
        # else:
        self.__occupants.append(occupant)

    def removeOccupant(self, occupant):
        found = False
        for passenger in self.__occupants:
            if passenger == occupant:
                found = True
                break;

        if found:
            self.__occupants.remove(passenger)
        else:
            raise LookupError

