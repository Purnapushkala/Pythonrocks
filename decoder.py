# Read in the input
n = int(input())
dictl = {}
# Solve the problem, good luck!
for i in range(n):
	lista= list(input().split())
	dictl[lista[0]] = lista[1]
inp = input()
hi = []
a = list(dictl.keys())
k =0
for i in range (len(inp)):
	for j in range(len(a)):
		if inp[k:(i+1)] == a[j]:
			hi.append(dictl[a[j]])
			k = i +1
print(*hi)



