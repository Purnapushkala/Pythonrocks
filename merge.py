# Get the input
one = list(input().split())
two = list(input().split())
b = []
final = []
# now do something similar to get the list of vehicles in the right lane
if len(one)>=len(two):
	a = len(one)
	b = one
	f = two
else:
	a = len(two)
	b = two
	f = one
for i in range(a):
	if i < len(f):
		final.append(one[i])
		final.append(two[i])
	else:
		final.append((b[i]))
lists = ' '.join([str(e) for e in final])
print(lists)


# Solve the problem


# Print the result
