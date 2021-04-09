# read the input
def longPl(string): 
    maxlen = 1
  
    s = 0
    length = len(string) 
  
    l = 0
    h = 0

    for i in range(1, length): 

        l = i - 1
        h = i 
        while l >= 0 and h < length and string[l] == string[h]: 
            if h - l + 1 > maxlen and ((h-l+1)%2 != 0): 
                s = l 
                maxlen = h - l + 1
            l -= 1
            h += 1
  

        l = i - 1
        h = i + 1
        while l >= 0 and h < length and string[l] == string[h]: 
            if (h - l + 1 > maxlen) and ((h-l+1)%2 != 0): 
                s = l 
                maxlen = h - l + 1
            l -= 1
            h += 1
  

    return maxlen 
  

string = input()
print (str(longPl(string)))
