import bina

def div(a,b):
    a = bina.bin_dec(a)
    b = bina.bin_dec(b)

    return bina.dec_bin(int(a/b),16),bina.dec_bin(int(a%b),16)

def Inv(a):

    b = ""
    for i in a:
        if(i == '0'):
            b += '1'
        else:
            b += '0'
    return b

def check(value3):
    if(value3 > pow(2,16)-1):
        return True
    return False

def add(value1,value2):
    value1 = int(value1,2)
    value2 = int(value2,2)
    value3 = value1+value2
    a = check(value3)
    value3 = bin(value3)[2:]
    l=16-len(value3)
    if a:
        value3 = value3[-16:]
    else:
        for i in range(1,l+1):
            value3 = "0" + value3
    
    return a,value3

def sub(value1,value2):
    value1 = int(value1,2)
    value2 = int(value2,2)
    value3 = value1-value2
    if value3 < 0:
        value3=0
        a = True
    else:
        a = False
    value3 = bin(value3)[2:]
    l=16-len(value3)
    for i in range(1,l+1):
        value3 = "0" + value3
    return a,value3

def mul(value1,value2):
    value1 = int(value1,2)
    value2 = int(value2,2)
    value3 = value1*value2
    
    a = check(value3)
    value3 = bin(value3)[2:]
    l=16-len(value3)
    if a:
        value3 = value3[-16:]
    else:
        for i in range(1,l+1):
            value3 = "0" + value3
    
    return a,value3

def xor(value1,value2):
    value1 = int(value1)
    value2 = int(value2)
    value3 = value1 ^ value2
    value3 = str(value3)
    l=16-len(value3)
    for i in range(1,l+1):
        value3 = "0" + value3
    return value3

def Or(value1,value2):
    value3 =''
    for i in range(0,16):
        n = int(value1[i]) | int(value2[i])
        value3 = value3 + str(n)
    
    return value3

def And(value1,value2):
    value3 =''
    for i in range(0,16):
        n = int(value1[i]) & int(value2[i])
        value3 = value3 + str(n)
    
    return value3

def L_shift(value1,value2):
    value1 = int(value1,2)
    value2 = int(value2,2)
    value3 = value1 << value2
    value3 = bin(value3)[2:]
    l=16-len(value3)
    for i in range(1,l+1):
        value3 = "0" + value3
    return value3

def R_shift(value1,value2):
    value1 = int(value1,2)
    value2 = int(value2,2)
    value3 = value1 >> value2
    value3 = bin(value3)[2:]
    l=16-len(value3)
    for i in range(1,l+1):
        value3 = "0" + value3
    return value3

