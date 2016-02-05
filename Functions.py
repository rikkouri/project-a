#A function to sum a range of numbers
def summer(upper_bound):
    total = 0
    calc_range = range(1, upper_bound, 1)
    for count in calc_range:
        total += count

    return total

#value = input('Upper bound\n')
#print(summer(value))

# A function to do the calculation  work
# def fibonacci(results, ceiling):
#     # The first time in we need to use the first two values
#     if ( len(results) < 3 ):
#         nextresult = results[0] + results[1]
#     # Subsequently we calculate the positions of the last two values
#     else:
#         nextresult = results[ len(results) - 2 ] + results[len(results) - 1]
#
#     # Check to see if we've reached the limit
#     if nextresult < ceiling:
#         results.append(nextresult)
#         # If not, we go round again
#         fibonacci(results, ceiling)
#     elif results == ceiling:
#         results.append(nextresult)
#
# # Set up our results with the first two values populated
# results = [0, 1]
# ceiling = input('Enter a value to reach : ')
# fibonacci(results,ceiling)
# print(results)


#Same using globals
# A function to do the calculation  work
def fibonacci():
    global r
    global c
    # The first time in we need to use the first two values
    if ( len(results) < 3 ):
        nextresult = results[0] + results[1]
    # Subsequently we calculate the positions of the last two values
    else:
        nextresult = results[ len(results) - 2 ] + results[len(results) - 1]

    # Check to see if we've reached the limit
    if nextresult < ceiling:
        results.append(nextresult)
        # If not, we go round again
        fibonacci()
    elif results == ceiling:
        results.append(nextresult)

# Set up our results with the first two values populated
r = [0, 1]
c = input('Enter a value to reach : ')
fibonacci()
print(r)