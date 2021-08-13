import opcode_table

def errors(s):
    if(s=="regE"):
        return "Typos in instruction name or register name"

    elif(s=="undefVarE"):
        return "Use of undefined variables"
    elif(s=="UndefLabelE"):
        return "Use of undefined labels"
    elif(s=="flagsE"):
        return "Illegal use of FLAGS register"
    elif(s=="ImmE"):
        return "Illegal Immediate values (less than 0 or more than 255)"
    elif(s=="labelMisuseE"):
        return "Misuse of labels as variables or vice-versa"
    elif(s=="varNotDecE"):
        return "Variables not declared at the beginning"
    elif(s=="missingHltE"):
        return "Missing hlt instruction"
    elif(s=="hltNotLastE"):
        return "hlt not being used as the last instruction"
    elif("syntaxE"):
        return "Wrong syntax used"
    else:
        return "General Syntax Error"

'''def convert(lst):
    return (lst.split())'''


# main function for checking S[0], if it's a label or not

def identifyE(S,Symbol_table):

    S=S.split()
    if (len(S)!=0):
        if S[0][-1] == ":":
            return identifyE_sub(S[1:],Symbol_table)
        else:
            return identifyE_sub(S,Symbol_table)
    return list([])


# sub main function for checking syntax for various operations

def identifyE_sub(S,Symbol_table):
    
    flag = False
    l=[]
    error=""
    
    if(S[0]=="hlt"):
        flag=False
        l.append(flag)
        l.append(error)

        return l
    
    if(S[0]=="var"):
        if len(S) == 2:
            for i in S[1]:
                if(not(i.isalnum())):
                    if(i!="_"):
                        flag=True
                        error=errors("syntaxE")
                        l.append(flag)
                        l.append(error)

                        return l
            l.append(flag)
            l.append(error)
            return l
        else:
            error=errors("Gen")
            flag = False
            l.append(flag)
            l.append(error)
            return l

    if(S[0] not in opcode_table.opcode):
        error=errors("gen")
        flag=True
        #l.append((flag,error))
        l.append(flag)
        l.append(error)
        return l
    
    if(opcode_table.opcode[S[0]][1]=="A"):
    #if(S[0]=="add" or S[0]=="sub" or S[0]=="mul" or S[0]=="xor"):
        if(len(S)>4):
            flag=True
            error=errors("SyntaxE")
            #l.append((flag,error))
            l.append(flag)
            l.append(error)
            return l
        
        for i in range(1,len(S)-1):
            if(S[i] not in opcode_table.registers):
                error=errors("regE")
                flag=True
                #l.append((flag,error))
                l.append(flag)
                l.append(error)
                return l
    

    if(opcode_table.opcode[S[0]][1]=="B"):
        if(len(S)>3):
            flag=True
            error=errors("SyntaxE")
            #l.append((flag,error))
            l.append(flag)
            l.append(error)
            return l
        
        #for i in range(1,len(S)-1):
        if(S[1] not in opcode_table.registers):
            error=errors("regE")
            flag=True
            #l.append((flag,error))
            l.append(flag)
            l.append(error)
            return l
        
        #add something to check whether S[2] is an immediate value or not in the beginning becuase mov will give error
        
        for j in S[2]:
            if j in "1234567890":
                continue
            else:
                error = errors("ImmE")
                flag =  True
                #l.append((flag,error))
                l.append(flag)
                l.append(error)
                return l
        if j > 255:
            error = errors("ImmE")
            flag =  True
            #l.append((flag,error))
            l.append(flag)
            l.append(error)
            return l

    if(opcode_table.opcode[S[0]][1]=="C"):
        if(len(S)>3):
            flag=True
            error=errors("SyntaxE")
            #l.append((flag,error))
            l.append(flag)
            l.append(error)
            return l
        
        for i in range(1,len(S)-1):
            if(S[i] not in opcode_table.registers):
                error=errors("regE")
                flag=True
                #l.append((flag,error))
                l.append(flag)
                l.append(error)
                return l
        #add something to check whether S[2] is a register or not in the begining 
    
    if(opcode_table.opcode[S[0]][1]=="D"):
        if(len(S)>3):
            flag=True
            error=errors("SyntaxE")
            #l.append((flag,error))
            l.append(flag)
            l.append(error)
            return l
        
        #for i in range(1,len(S)-1):
        if(S[1] not in opcode_table.registers):
            error=errors("regE")
            flag=True
            #l.append((flag,error))
            l.append(flag)
            l.append(error)
            return l
        
        #code for checking S[2] is a mem_addr
        if S[2] not in Symbol_table:
            error=errors("undefVarE")
            flag=True
            #l.append((flag,error))
            l.append(flag)
            l.append(error)
            return l
    

    if(opcode_table.opcode[S[0]][1]=="E"):
        if(len(S)>2):
            flag=True
            error=errors("SyntaxE")
            #l.append((flag,error))
            l.append(flag)
            l.append(error)
            return l
        
        #for i in range(1,len(S)-1):
        
        #check how to check errors for mem_addr

        if S[1] not in Symbol_table:
            flag=True
            error=errors("UndefLabelE")
            #l.append((flag,error))
            l.append(flag)
            l.append(error)
            return l

    if(opcode_table.opcode[S[0]][1]=="F"):
        if(len(S)>1):
            flag=True
            error=errors("SyntaxE")
            #l.append((flag,error))
            l.append(flag)
            l.append(error)
            return l

    #l.append((False,error))
    l.append(flag)
    l.append(error)
    
    return l
