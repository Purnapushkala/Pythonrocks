# Good luck! Remember the points are *real*, not necessarily *integer*.
import math
intn = []
intm = []
h = False
n = int(input())
intn = [ list(map(float, input().split())) for y in range(n)] 
m = int(input())
intm = [ list(map(float, input().split())) for y in range(m)] 
print(intn)
for i in range(n):
	for j in range(m):
		a = math.sqrt(((intn[i][0]-intm[j][0])**2) + ((intn[i][1]-intm[j][1])**2))
		if a == intn[i][2]:
			print("Large")
			h = True
			break
	if not h:
		print("Small")
