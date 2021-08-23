import math
def dec_bin(x,y):
    a = bin(x)
    a=a[2:]
    l = len(a)
    while l < y :
        a = "0" + a
        l += 1
    return a

def bin_dec(x):
    y = len(x) - 1
    a = 0
    l = 0
    while(y >=0):
        if(x[y] == '1'):
            a += math.pow(2,l)
        l +=1
        y-=1
    return int(a)



    