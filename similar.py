# Read in the input
x,y,z = map(int,input().split())
if x==y and x==z:
	print("same")
elif x!=y and x!=z and y!=z:
	print("distinct")
else:
	print("similar")

# Solve the problem and output the result
