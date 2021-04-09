# Good luck! Write your solution below.
lis = list(map(int, input().split()))
length =1
longi = 1
for i in range(1,len(lis)):
	if lis[i] == lis[i-1]:
		length +=1
		longi = max(longi,length)
	else:
		length = 1
print (longi)