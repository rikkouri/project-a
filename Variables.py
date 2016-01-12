# Example variable assignment
a = 10
print(a)

# Data types Exercise
# Integer
a = 10
print(a)
# Float
a = 10.537
print(a)
# Boolean
a = "False"
print(a)
# Interesting discussion point here to test for 'False' and have it output 'True'
print(a == 'False')
# String
a = "string value"
print(a)
# Dict
a = {'name': 'Paul', 'location': 'Bristol'}
print(a)
print(a['location'])
print(a['name'])

# Type conversion example
print('\nType conversion example')
varToConvert = '10'
convertedVar = int(varToConvert)
print('varToConvert')
print(varToConvert)
print('convertedVar')
print(convertedVar)
try:
    # Try to concatenate the str and the int. Exception will be caught.
    print('varToConvert + convertedVar')
    print(varToConvert + convertedVar)
except TypeError as error:
    print('An error occurred :\n' + str(error))
finally:
    print('\n')
    print('Converting int to str and concatenating:\n')
    nextAttempt = 'varToConvert + str(convertedVar)'
    print(nextAttempt)
    print(eval(nextAttempt))
# Trying to add str value to int. Exception will be caught.
print('convertedVar + varToConvert')
try:
    print(convertedVar + varToConvert)
except TypeError as error:
    print('An error occurred :\n' + str(error))
finally:
    print('\n')
    print('Converting str to int and adding:\n')
    nextAttempt = 'int(varToConvert) + convertedVar'
    print(nextAttempt)
    print(eval(nextAttempt))

# Null checking
# Null unsafe
b = 'Some value'
print(b)
b = b + c
print(b)

# Null safe
b = 'Some value'
print(b)
try:
    b = b + c
except NameError as error:
    print('An error occurred. The error message received was:\n' + str(error))
finally:
    c = 'Some other value'
    b = b + ' ' + c
    print(b)
