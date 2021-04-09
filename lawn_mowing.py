# Good luck! You've got this!
x,y = map(int,input().split())
hi = int(min(x,y))
if x!=y:
	cf = int(4*min(x,y)*max(x,y)*(3/2))	
elif x == y:
	cf = int(4*((x/2)**2)*10)
print(str(cf+hi))