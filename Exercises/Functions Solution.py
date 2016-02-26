# A function to do the calculation  work
def fibonacci(results, ceiling):
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
        fibonacci(results, ceiling)
    #If we hit the end exactly
    elif nextresult == ceiling:
        results.append(nextresult)

# Set up our results with the first two values populated
results = [0, 1]
ceiling = input('Enter a value to reach : ')
fibonacci(results,ceiling)
print(results)
