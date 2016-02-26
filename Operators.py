# #Operators and Precedence Examples and Exercises
# smallInt = 5;
# largeInt = 5000;
#
# def basicOperators():
#     #Basic Maths
#     #Addition
#     operation = str(largeInt) + '+' + str(smallInt)
#     result = eval(operation)
#     print(operation + ' = ' + str(result))
#     print('\n')
#     #Subtraction
#     operation = str(smallInt) + '-' + str(largeInt)
#     result = eval(operation)
#     print(operation + ' = ' + str(result))
#     print('\n')
#     #Multiplication
#     operation = str(smallInt) + '*' + str(largeInt)
#     result = eval(operation)
#     print(operation + ' = ' + str(result))
#     print('\n')
#     #Division
#     operation = str(largeInt) + '/' + str(smallInt)
#     result = eval(operation)
#     print(operation + ' = ' + str(result))
#     print('\n')
#     #Modulo
#     operation = str(smallInt) + '%' + str(largeInt)
#     result = eval(operation)
#     print(operation + ' = ' + str(result))
#     print('\n')
#
# def relationalOperators():
#     # Build a series of relational operations, execute and print the results
#     print('Relational')
#     smallInt = '5'
#     largeInt = '5000'
#     operators = [ '<','>','==','!=','>=','<=']
#     for op in operators:
#         operation = smallInt + op + largeInt
#         result = eval(operation)
#         print(operation + ' = ' + str(result))
#     print('\n')
#
# def logicalOperators():
#     # Build a series of logical operations, execute and print the results
#     print('Logical')
#     trueVar = 'True'
#     falseVar = 'False'
#     operators = [ 'and','or','and not']
#     for op in operators:
#         operation = '(trueVar ' + op + ' falseVar == True)'
#         result = eval(operation)
#         print(operation + ' = ' + str(result))
#     print('\n')
#
# def assignmentOperators():
#     # Build a series of assignment operations, execute and print the results
#     print('Assignment')
#     target = 15
#     source = 5
#     operators = ['+=', '*=', '-=', '/=', '%=', '**=', '//=']
#     print('target = ' + str(target))
#     for op in operators:
#         operation = 'target' + op + str(source)
#         print(operation)
#         exec(operation)
#         print('target = ' + str(target) +'\n')
#     print('\n')
#
# def precedenceExamples():
#     a = 2
#     b = 4
#     c = 8
#
#     print('Default order:\t' + str(a) + ' * ' + str(c) + ' + ' + str(b) + ' = ' + str(eval('a * c + b')))
#     print('Forced order:\t' + str(a) + ' * (' + str(c) + ' + ' + str(b) + ') = ' + str(eval('a * ( c + b)')))
#     print('\n')
#     print('Default order:\t' + str(c) + ' // ' + str(b) + ' - ' + str(a) + ' = ' + str(eval('c // b - a')))
#     print('Forced order:\t' + str(c) + ' // (' + str(b) + ' - ' + str(a) + ') = ' + str(eval('c // ( b - a)')))
#
#
# basicOperators()
# relationalOperators()
# logicalOperators()
# assignmentOperators()
# precedenceExamples()
#
# # WAPT sum odd and even numbers over a range
# def ops_exercise():
#     range_lower = input('Enter a lower bound\n')
#     range_upper = input('Enter an upper bound\n')
#     sum_range = range(range_lower, range_upper + 1)
#     sum_even = 0
#     sum_odd = 0
#     for i in sum_range:
#         if i % 2 == 0:
#             sum_even += i
#         else:
#             sum_odd += i
#     print('Examining numbers from ' + str(range_lower) + ' to ' + str(range_upper))
#     print('Sum of odds = ' + str(sum_odd))
#     print('Sum of evens = ' + str(sum_even))
#
# # An exercise to build a calculator
# def calc_exercise():
#     pass
#
#
# #ops_exercise()
#
# #Option 1
# result = input('Enter a sum : ')
# print result
#
# #Option 2
# left = raw_input('Enter a value: ')
# operator = raw_input('Enter an operator: ')
# right = raw_input('Enter another value: ')
# sum = str(left) + operator + str(right)
# result = eval( sum )
# print result
#
# #Relationship Operators Exercise
#
# #Option 1
# secret = 42
# value = raw_input('Enter a value: ')
# result = (int(value) >= secret)
# print(value + ' >= ??? is ' + str(result))
#
# #Option 2
# secret = 42
# value = raw_input('Enter a value: ')
# operator = raw_input('Enter an operator: ')
# result = eval( value + operator + str(secret) )
# print(value + operator + ' ??? is ' + str( result ) )
#



#Membership
ceiling = int( raw_input('Enter a maximum value: '))
# threes = []
# fours = []
#
# for value in range(0, ceiling):
#     if ( (value * 3) < ceiling):
#         threes.append( value * 3 )
#     if ( (value * 4) < ceiling ):
#         fours.append( value * 4 )
#     if value not in threes and value not in fours:
#         print( value )

for value in range(0, ceiling):
    if ( (value < ceiling) and (value % 3 != 0) and (value % 4 != 0) ):
        print( value )



