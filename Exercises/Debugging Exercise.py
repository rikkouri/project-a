# This program contains several bugs. Find and correct as many as you can.
a_dict = { 'pc': '21.4', 'xbox 360': '113.1', 'ps3': '84.5', '3ds':'11.7', 'Wii': '9.3'}
selection = ''
while selection is not 'end':
    selection = raw_input('Enter a platform name: \n')
    if selection == 'all':
        total = 0
        for key in a_dict:
            total += a_dict[key]
        print('Total = ' + total)
    else:
        print(selection + ' total game sales in 2015 were ' + a_dict[selection])
