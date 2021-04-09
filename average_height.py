# the floor() function might be useful
# for a floating point number x, floor(x) is the greatest integer <= x
from math import floor


# read in the input
numbers = list(map(int, input().split()))

# now "numbers" is a list containing all integers in the input


# solve the problem
average = sum(numbers)/len(numbers)

# output the solution
print(floor(average))
