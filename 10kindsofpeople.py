# read the input
x,y = list(map(int,input().split()))
a=input()
c0 = 0
c1 = 0
b =[]
for i in range(y):
	k,j = list(map(int,input().split()))
	c1 = 0
	c0 = 0
# solve the problem
	for j in a[k-1:j]:
		if j == "1":
			c1 +=1
		elif j == "0":
			c0 +=1
	if c1 >0 and c0 ==0:
		b.append("one")
	elif c0 > 0 and c1 == 0:
		b.append("zero")
	else:
		b.append("both")

# output the answer
print(*b,sep = "\n")
