# Control / Flow examples and exercises

def ifExample(smallVal, largeVal):
    # If condition example
    print('\nIf condition example')
    if smallVal < largeVal:
        print("Small < Large")
    else:
        print("Small > Large")

def forExample(data):
    # For loop example
    print('\nFor loop examples')
    print('\nLooping over a counter')
    loopRange = range(1, 11, 1)
    for i in loopRange:
        print(i)

    loopVar = 'Looping over characters in a string'
    print('\n' + loopVar)
    for char in loopVar:
        print(char)

    print('\nLooping over a list with an iterator')
    for datum in data:
        print(datum)

    print('\nLooping over items in a dictionary')
    loopDict = {'name': 'Paul', 'location': 'Bristol', 'age': '>40'}
    for item in loopDict.keys():
        print(item + ' = ' + loopDict[item])


def whileExample(startVal, increment):
    # While loop example
    print('\nWhile loop example')
    while startVal > 0:
        print(startVal)
        startVal -= increment
    else:
        print('Ended!')


#using while loop
def fizzBuzzExercise(ceiling, increment):
    # Classic fizz buzz exercise for conditionals / loops
    print('\nFizzBuzz')
    counter = 0
    while counter < ceiling:
        counter += increment
        if counter % 3 == 0 and counter % 5 == 0:
            print('FizzBuzz')
        elif counter % 5 == 0:
            print('Buzz')
        elif counter % 3 == 0:
            print('Fizz')
        else:
            print counter
    print('Done!')

def fizzBuzzExercise2(ceiling):
    # Classic fizz buzz exercise for conditionals / loops
    print('\nFizzBuzz\n')
    for counter in range(1, ceiling):
        if counter % 3 == 0 and counter % 5 == 0:
            print('FizzBuzz')
        elif counter % 5 == 0:
            print('Buzz')
        elif counter % 3 == 0:
            print('Fizz')
        else:
            print counter
    print('Done!')


# Execute the examples

#ifExample(10, 100)
#ifExample(100, 10)

#forExample([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])
#whileExample(100, 10)

#fizzBuzzExercise(100, 1)
fizzBuzzExercise2(100)
