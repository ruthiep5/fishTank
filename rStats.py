def findAvg(lst):
    #Finds the average of a list
    t = 0 
    n = 0
    for x in lst:
        t += x
        n += 1
    avg = t/n
    return avg

def absoluteError(lst1, lst2):
    n = len(lst1)
    a = 0
    for i in range(n):
        # print(i,lst1[i], lst2[i])
        d = lst1[i] - lst2[i]
        a += abs(d)
    return(a)
    
def avg(lst):
    return sum(lst)/len(lst)

def res(lst1, lst2):
    n = len(lst1)
    s = 0
    for i in range(n):
       # print(i,lst1[i], lst2[i])
        d = (lst1[i] - lst2[i]) ** 2
        s += d
    return s

def meanDif(lst):
    t = 0
    avg = findAvg(lst)
    for x in lst:
        t += (x - avg)**2
    return t

def dsq(lst1):
    n = len(lst1)
    s = 0
    for i in range(n):
       # print(i,lst1[i], lst2[i])
        d = (lst1[i] - avg(lst1)) ** 2
        s += d
    return s

def rSquared(lst1, lst2):
    r2 = 1 - (res(lst1, lst2) / dsq(lst1) )
    return r2