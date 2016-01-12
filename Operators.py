#Operators and Precedence Examples and Exercises
smallInt = 5;
largeInt = 5000;

def basicOperators():
    #Basic Maths
    #Addition
    operation = str(largeInt) + '+' + str(smallInt)
    result = eval(operation)
    print(operation + ' = ' + str(result))
    print('\n')
    #Subtraction
    operation = str(smallInt) + '-' + str(largeInt)
    result = eval(operation)
    print(operation + ' = ' + str(result))
    print('\n')
    #Multiplication
    operation = str(smallInt) + '*' + str(largeInt)
    result = eval(operation)
    print(operation + ' = ' + str(result))
    print('\n')
    #Division
    operation = str(largeInt) + '/' + str(smallInt)
    result = eval(operation)
    print(operation + ' = ' + str(result))
    print('\n')
    #Modulo
    operation = str(smallInt) + '%' + str(largeInt)
    result = eval(operation)
    print(operation + ' = ' + str(result))
    print('\n')

def relationalOperators():
    # Build a series of relational operations, execute and print the results
    print('Relational')
    smallInt = '5'
    largeInt = '5000'
    operators = [ '<','>','==','!=','>=','<=']
    for op in operators:
        operation = smallInt + op + largeInt
        result = eval(operation)
        print(operation + ' = ' + str(result))
    print('\n')

def logicalOperators():
    # Build a series of logical operations, execute and print the results
    print('Logical')
    trueVar = 'True'
    falseVar = 'False'
    operators = [ 'and','or','and not']
    for op in operators:
        operation = '(trueVar ' + op + ' falseVar == True)'
        result = eval(operation)
        print(operation + ' = ' + str(result))
    print('\n')

def assignmentOperators():
    # Build a series of assignment operations, execute and print the results
    print('Assignment')
    target = 15
    source = 5
    operators = ['+=', '*=', '-=', '/=', '%=', '**=', '//=']
    print('target = ' + str(target))
    for op in operators:
        operation = 'target' + op + str(source)
        print(operation)
        exec(operation)
        print('target = ' + str(target) +'\n')
    print('\n')

def precedenceExamples():
    a = 2
    b = 4
    c = 8

    print('Default order:\t' + str(a) + ' * ' + str(c) + ' + ' + str(b) + ' = ' + str(eval('a * c + b')))
    print('Forced order:\t' + str(a) + ' * (' + str(c) + ' + ' + str(b) + ') = ' + str(eval('a * ( c + b)')))
    print('\n')
    print('Default order:\t' + str(c) + ' // ' + str(b) + ' - ' + str(a) + ' = ' + str(eval('c // b - a')))
    print('Forced order:\t' + str(c) + ' // (' + str(b) + ' - ' + str(a) + ') = ' + str(eval('c // ( b - a)')))


basicOperators()
relationalOperators()
logicalOperators()
assignmentOperators()
precedenceExamples()