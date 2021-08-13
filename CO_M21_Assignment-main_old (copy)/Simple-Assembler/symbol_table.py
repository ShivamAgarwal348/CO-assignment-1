import opcode_table

def symbols(Lines):

    count_l = 0
    words = []
    Symbol_table = {}

    for line in Lines :
        words = line.split()
    
        if words[0] in opcode_table.opcode:
            count_l +=1
        elif(words[0][-1] == ':'):
            Symbol_table[words[0][0:-1]] = ["label" , count_l]
            count_l+=1

    for line in Lines :
        words = line.split()
        if( words[0] == 'var'):
            Symbol_table[words[1]] = ["variable",count_l]
            count_l+=1



    for i in Symbol_table:
        a = bin(Symbol_table[i][1])
        a = a[2:]
        length = len(a)
        while length < 8 :
            a = "0" + a
            length += 1
        Symbol_table[i][1] = a
    
    return Symbol_table
