# put your solution here

def consec(a, n):
 
    leng = 1
    li = []

    if (n == 0):
        return list

    for i in range (1, n + 1):
        if (i == n or a[i] -
            a[i - 1] != 1):
 
            if (leng == 1):
                li.append(str(a[i - leng]))
            elif leng == 2:
                temp = (str(a[i - leng]) + " "+
                         str(a[i - 1]))
                li.append(temp)
            else:
                temp = (str(a[i - leng]) +
                        "-" + str(a[i - 1]))
                li.append(temp)
            leng = 1
        
        else:
            leng += 1
    return li
 
if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    an = sorted(l)
    
    ans = consec(an, n)
    for i in range(len(ans)):
     
        if(i == len(ans) - 1):
            print (ans[i]) 
        else:
            print (ans[i], end = " ")
     
    