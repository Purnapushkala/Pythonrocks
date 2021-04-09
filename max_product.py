n =  int(input())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
list1.sort()
list2.sort()
suma = 0
for i in range(n):
	a = list1[i] * list2[i]
	suma = suma + a
print(suma)