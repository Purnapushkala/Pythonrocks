# add you code here
import sys
x = []
for i in sys.stdin:
    x.append(i.strip().split())
T = int(x[0][0])
p = []
cars = x[1]
for i in range(len(cars)):
    cars[i] = int(cars[i])
    p.append(i)

for i in range(len(cars)):
    p[i] = p[i] + cars[i]*T
	
passed = 0
for j in range(len(p)-1):
    for k in range(j, len(p)):
        if p[j] > p[k]:
            passed = passed + 1
print(passed)