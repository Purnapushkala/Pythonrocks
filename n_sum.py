#Good Luck! You've got this! :)
x,y = map(int,input().split())
a = []
s = 0
count = 0

for i in range(x,0,-1):
	if (s+i) <= y:
		count +=1
		a.append(i)
		s = s + i	
a.sort()
print(count)
print(*a)
