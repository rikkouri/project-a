class Person:
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


try:
    # No exception should be raised
    bob = Person()
    bob.setName('Bob')
    bob.setAge(50)
except:
    print('An error occurred')
else:
    try:
        # However if try to access the variables directly, mangling causes an error
        print(bob.__name + ' is ' + str(bob.__age) + ' years old.')
    except AttributeError as e:
        print 'Error: ', e.message
    finally:
        # But using the accessor methods returns the expected values
        print(bob.getName() + ' is ' + str(bob.getAge()) + ' years old.')

