#A function to sum a range of numbers
def summer(upper_bound):
    total = 0
    calc_range = range(1, upper_bound, 1)
    for count in calc_range:
        total += count

    return total

value = input('Upper bound\n')
print(summer(value))