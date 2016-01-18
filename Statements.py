import time

#Simple Statement Examples

#assert
#Input a value and assert if true. Catch the exception and print an error if it fails.
def assertTest():
    try:
        varToTest = input('True or False value\n')
        assert(varToTest == True)
        print('Assert passed')
    except:
        if not 'varToTest' in locals():
            varToTest = None
        print( 'varToTest = ' + str(varToTest) )
    finally:
        print( 'Assert Done')
        again = raw_input('Again?\n')
        if str(again) == 'y':
            assertTest()

#pass
def passExample():
    pass

#del
#Create a dictionary then progressively delete values
def delExample():
    someDict = { 'name': 'Homer J', 'location': 'Springfield','occupation': 'Nukular Safety Technician' }
    print('Current values')
    print(someDict)
    print('Deleting occupation')
    del someDict['occupation']
    print(someDict)
    print('Deleting location')
    del someDict['location']
    print(someDict)
    print('Deleting name')
    del someDict['name']
    print(someDict)
    print('Adding Marge')
    someDict['name'] = 'Marge S'
    someDict['location'] = 'Springfield'
    someDict['occupation'] = 'Homemaker / Police Office (Ret\'d)'
    print(someDict)

#print
#Take some input and print it. Output a message if nothing was entered
def printExample():
    toOutput = raw_input('Type something in\n')
    if not toOutput in locals() and not toOutput == None and not toOutput == '':
        print('You typed \'' + toOutput + '\'')
    else:
        print('You didn\'t enter anything')

#return
#Input a value, pass it to another function, decorate it, return it and output
def returnExample():
    userValue = raw_input('Enter a value: \n')
    if not userValue in locals() and not userValue == None and not userValue == '':
        newValue = returnFunc(userValue)
        print(newValue)
    else:
        print('You didn\'t enter anything')

def returnFunc(value):
    value += ' was returned'
    return value

#yield
#Define a generator function using yield
def genExample(end):
    num = 0
    while num <= end:
        yield num
        num += 1

def genRunner():
    end = raw_input('Number to end on: \n')
    sumOfNumbers = sum(genExample(int(end)))
    print('Sum of numbers 1 to ' + end + ' = ' + str(sumOfNumbers))

#raise
#Cause an exception using assert, continue execution and then raise and handle the exception (again)
def raiseTest():
    someVar = 'Foo'
    try:
        assert someVar == 'Bar'
    except:
        print( 'An exception was raised')
    finally:
        print('But we handled it and continued')

    print( 'Variable value is ' + someVar)
    print( 'Re-raising the handled exception')
    try:
        raise
    except:
        print('Exception raised')
    finally:
        print('Done')


#break
def getTime():
    current_time = int(round(time.time() * 1000 ))
    return current_time

def breakTest():
    targetValue = int(raw_input( 'Enter a numeric value > 100 : \n'))
    print('Fail slow example without break')
    startTime = getTime()
    loopRange = range(0,10000000,1)
    for counter in loopRange:
        # print(str(counter))
        if counter == targetValue:
            print('Found ' + str(counter))
    endTime = getTime()
    elapsed = (int(endTime) - int(startTime)) #/ 1000
    print('Done with slow example in ' + str(elapsed) + ' milliseconds')
    print('Faster example with break')
    startTime = getTime()
    for counter in loopRange:
        # print(str(counter))
        if counter == targetValue:
            print('Found ' + str(counter))
            break
    endTime = getTime()
    elapsed = (int(endTime) - int(startTime)) #/ 1000
    print('Done in ' + str(elapsed) + ' milliseconds')

#continue

#import

#global

#exec


#Simple Statement Exercises

#Compound Statements

#Compound Statement Exercises


# Function calls to run the tests / examples
#assertTest()

#print('Pass example about to run')
#passExample()
#print('Pass example complete')

#delExample()

#printExample()

#returnExample()

#genRunner()

#raiseTest()

breakTest()