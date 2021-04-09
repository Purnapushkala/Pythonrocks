# add your solution here
n = int(input())
l = []
for i in range(n):
	l.append(int(input()))
a = sorted(l)
print(n)
count = 0
for i in range(1,n):
	if a[i] !=a[i-1]:
		count= n-i
		for j in range(a[i] - a[i-1]):		
			print(count)

	
