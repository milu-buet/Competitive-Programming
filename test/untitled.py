


def nextPerm(s):
    
    pivot = getPivot(s)

    print(pivot)
    
    beg = ''
    if pivot > -1:
        s[pivot],s[-1] = s[-1],s[pivot]
        beg = s[0:pivot+1]
    
    s =  beg + s[pivot+1:][::-1]
    
    return s

    
def getPivot(s):
    for i in range(len(s)-1)[::-1]:
        if s[i] < s[i+1]:
            return i
    return -1



s = ['1','2','3']

print(nextPerm(s))