def binary(x):
    a = bin(x)
    a=a[2:]
    l = len(a)
    while l < 8 :
        a = "0" + a
        l += 1
    return a