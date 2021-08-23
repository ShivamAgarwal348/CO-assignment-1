import opcode_table

global lin
lin=0

def errors(s):
    if(s=="regE"):
        return "Typos in instruction name or register name or something other than register has been used"

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

def inputfile(Lines,Symbol_table):
    global lin
    for line in Lines:
        lin+=1
        errorflag = identifyE(line,Symbol_table)
        if (errorflag[0] == True):
            return errorflag
    return list([False])

def identifyE(S,Symbol_table):

    S=S.split()
    if (len(S)!=0):
        if S[0][-1] == ":":
            return identifyE_sub(S[1:],Symbol_table)
        else:
            return identifyE_sub(S,Symbol_table)
    return list([False])


# sub main function for checking syntax for various operations
global varflag
varflag = True

def identifyE_sub(S,Symbol_table):

    global varflag
    flag = False
    l=[]
    error=""
    
    if(S[0]=="hlt"):
        flag=False
        l.append(flag)
        l.append(error)

        return l
    
    if(S[0]=="var"):
        if varflag == False:
            error = errors("varNotDecE")
            return([True,error])

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

    else:

        varflag = False
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
            
            for i in range(1,len(S)):
                if(S[i] not in opcode_table.registers):
                    error=errors("regE")
                    flag=True
                    #l.append((flag,error))
                    l.append(flag)
                    l.append(error)
                    return l
        
        if S[0] == "mov":
            if(len(S)>3):
                flag=True
                error=errors("SyntaxE")
                #l.append((flag,error))
                l.append(flag)
                l.append(error)
                return l
            
            if(S[1] not in opcode_table.registers):
                error=errors("regE")
                flag=True
                #l.append((flag,error))
                l.append(flag)
                l.append(error)
                return l
            if S[2][0] != "$":
                if(S[2] not in opcode_table.registers):
                    error=errors("regE")
                    flag=True
                    #l.append((flag,error))
                    l.append(flag)
                    l.append(error)
                    return l
            else:
                for j in S[2][1:]:
                    if j in "1234567890":
                        continue
                    else:
                        error = errors("ImmE")
                        flag =  True
                        #l.append((flag,error))
                        l.append(flag)
                        l.append(error)
                        return l
                if int(S[2][1:]) > 255:
                    error = errors("ImmE")
                    flag =  True
                    #l.append((flag,error))
                    l.append(flag)
                    l.append(error)
                    return l
        else:
            

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
                
                for j in S[2][1:]:
                    if j in "1234567890":
                        continue
                    else:
                        error = errors("ImmE")
                        flag =  True
                        #l.append((flag,error))
                        l.append(flag)
                        l.append(error)
                        return l
                if int(S[2][1:]) > 255:
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
                
                for i in range(1,len(S)):
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
