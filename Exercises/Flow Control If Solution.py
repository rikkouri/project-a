#Get a number from the user
number = int(raw_input('Enter a number: '))

#Bonus: Test so see if we have a zero
if (number == 0):
    print( str(number) + ' is not valid input.')
#Test to see if the number is even
elif (number % 2 == 0):
    print( str(number) + ' is even.')
#Otherwise it must be even
else:
    print( str(number) + ' is odd.')
