from Human import Human

class Person(Human):
    def __init__(self):
        # These attributes are subject to name mangling
        self.__name = None
        self.__age = None

    # Accessor methods
    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    # Mutator methods
    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age
