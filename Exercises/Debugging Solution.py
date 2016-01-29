# Change string values to numbers since we'll be adding them later
a_dict = { 'pc': 21.4, 'xbox 360': 113.1, 'ps3': 84.5, '3ds':11.7, 'wii': 9.3}
selection = ''
# Change is not to != since is not compares to see if it's the same object
# We're only interested in value
while selection != 'end':
    selection = raw_input('Enter a platform name: \n')
    # Hold onto the original input value to output later
    oldselection = selection
    # Convert the input value to lowercase since our keys are all lowercase
    selection = selection.lower()
    if selection == 'all':
        total = 0
        for key in a_dict:
            total += a_dict[key]
        print('Total game sales for all platforms in 2015 were ' + str(total) + ' million units.')
    #Add an else condition to check the key is present before we try to get the associated value
    elif selection in a_dict.keys():
        print(oldselection + ' total game sales in 2015 were ' + str(a_dict[selection]) + ' million units.')
    #Output an error message if we can't find the value and we're not quitting
    elif selection != 'end':
        print( 'Sorry, couldn\'t find ' + oldselection )
    # Output a message if we're quitting
    else:
        print('Goodbye.')
