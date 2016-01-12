#Control / Fl;ow examples and exercises

def ifExample( smallVal, largeVal):
    # If condition example
    print('\nIf condition example')
    if ( smallVal < largeVal):
        print( "Small < Large")
    else:
        print("Small > Large")

def forExample(data):
    # For loop example
    print('\nFor loop example')
    for datum in data:
        print(datum)

def whileExample(startVal, increment):
    # While loop example
    print('\nWhile loop example')
    while startVal > 0:
        print(startVal)
        startVal -= increment
    else:
        print('Ended!')


def fizzBuzzExercise(ceiling, increment):
    #Classic fizz buzz exercise for conditionals / loops
    print('\nFizzBuzz')
    counter = 0
    while counter < ceiling:
        counter += increment
        if counter % 15 == 0:
            print('FizzBuzz')
        elif counter % 5 == 0:
            print('Buzz')
        elif counter % 3 == 0:
            print('Fizz')
        else:
            print counter
    print('Done!')



ifExample(10, 100)
ifExample(100,10)

forExample( [1,2,4,8,16,32,64,128,256,512,1024])
whileExample(100,10)

fizzBuzzExercise(100,1)