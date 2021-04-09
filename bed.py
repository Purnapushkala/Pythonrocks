# read in the input
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())



# solve the problem
length = x2 - x1
width = y2-y1
area = length * width
# output the result
print(abs(area))