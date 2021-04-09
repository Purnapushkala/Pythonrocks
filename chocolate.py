line = input().split()
chocolates = int(line[0])
jars = int(line[1])
count = 0
left = 0

# write your code here

for i in range(jars):
	jar = input().split()
	choc = int(jar[0])
	sub = int(jar[1]) - int(jar[0])
	if chocolates <=sub:
		count = count +1

print(count)
