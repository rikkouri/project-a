#Prompt the user to input two values
operandOne = raw_input('Enter a value: ')
operandTwo = raw_input('Enter another value: ')

#Now perform the sums and output the result
print( operandOne + ' + ' + operandTwo + ' = ' + str( int(operandOne) + int(operandTwo) ) )
print( operandOne + ' - ' + operandTwo + ' = ' + str( int(operandOne) - int(operandTwo) ) )
print( operandOne + ' * ' + operandTwo + ' = ' + str( int(operandOne) * int(operandTwo) ) )
print( operandOne + ' / ' + operandTwo + ' = ' + str( int(int(operandOne) / int(operandTwo)) ) )
print( operandOne + ' % ' + operandTwo + ' = ' + str( int(operandOne) % int(operandTwo) ) )
print( operandOne + ' ** ' + operandTwo + ' = ' + str( int(operandOne) ** int(operandTwo) ) )

