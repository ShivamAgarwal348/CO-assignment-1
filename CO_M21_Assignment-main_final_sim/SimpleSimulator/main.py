import registers
import Inputsim
from programCounter import ProgramCounter
import bina
import funcs
import matplotlib.pyplot as plt


register = {"000":"0000000000000000","001":"0000000000000000",
"010":"0000000000000000","011":"0000000000000000","100":"0000000000000000",
"101":"0000000000000000","110":"0000000000000000","111":"0000000000000000"}

cycArr=[]
memAddrArr=[]
Inputsim.Inputsim()
text_file = open("inputsim.txt",'r')
Lines = text_file.readlines()
Cycle = 0

PC = ProgramCounter(0)

F1 = False
E = False
F2 = ''
def output(F1):
    if F1:
        register['111'] = "0000000000000000"
        F1 = False
    print(bina.dec_bin(PC.getPC(),8) + ' ' + register["000"] + ' ' +  register["001"] + ' ' + register["010"] + ' ' +register["011"] + ' ' + register["100"] + ' ' + register["101"] + ' ' + register["110"] + ' ' + register["111"])
    return F1

'''def reset_flag():
    register['111'] = "0000000000000000"'''


opcode = ""
while True:
    
    line = Lines[PC.getPC()]
    
    
    cycArr.append(Cycle)
    
    memAddrArr.append((PC.getPC()))
    flag = True
    opcode = line[0:5]


    if (opcode in registers.opcodes["A"]):
        if(opcode == "00000"):
            flag,register[line[7:10]] = funcs.add(register[line[10:13]],register[line[13:16]])
            if flag:
                register['111'] = '0000000000001000'
                F1 = False
            F1 = output(F1)
            F = True
        elif(opcode == "00001"):
            flag,register[line[7:10]] = funcs.sub(register[line[10:13]],register[line[13:16]])
            if flag:
                register['111'] = '0000000000001000'
                F1 = False
            F1 = output(F1)
            F = True

        elif(opcode == "00110"):
            flag,register[line[7:10]] = funcs.mul(register[line[10:13]],register[line[13:16]])
            if flag:
                register['111'] = '0000000000001000'
                F1 = False
            F1 = output(F1)
            F = True

        elif(opcode == "01010"):
            register[line[7:10]] = funcs.xor(register[line[10:13]],register[line[13:16]])
            F1 = output(F1)

        elif(opcode == "01011"):
            register[line[7:10]] = funcs.Or(register[line[10:13]],register[line[13:16]])
            F1 = output(F1)

        elif(opcode == "01100"):
            register[line[7:10]] = funcs.And(register[line[10:13]],register[line[13:16]])
            F1 = output(F1)

    elif(opcode in registers.opcodes["B"]):

        if(opcode == "00010"):
            register[line[5:8]] = "00000000" + line[8:16]
            F1 = output(F1)

        elif(opcode == "01000"):
            register[line[5:8]] = funcs.R_shift(register[line[5:8]],line[8:16])
            F1 = output(F1)

        elif(opcode == "01001"):
            register[line[5:8]] = funcs.L_shift(register[line[5:8]],line[8:16])
            F1 = output(F1)

    elif(opcode in registers.opcodes["C"]):

        if(opcode == "00011"):
            register[line[10:13]] = register[line[13:16]]
            F1 = output(F1)

        elif(opcode == "00111"):
            register["000"],register["001"] = funcs.div(register[line[10:13]], register[line[13:16]])
            F1 = output(F1)

        elif(opcode == "01101"):
            register[line[10:13]] = funcs.Inv(register[line[13:16]])
            F1 = output(F1)
        elif(opcode == "01110"):
            
            a = bina.bin_dec(register[line[10:13]])
            b = bina.bin_dec(register[line[13:16]])

            if(a < b):
                register["111"] = "0000000000000100"
            elif(a > b):
                register["111"] = "0000000000000010"
            else:
                register["111"] = "0000000000000001"
            F1 = False
            F1 = output(F1)
            F1 = True
            
            

    elif(opcode in registers.opcodes["D"]):

        if(opcode == "00100"):
            register[line[5:8]] = Lines[bina.bin_dec(line[8:16])]            
            F1 = output(F1)
            cycArr.append(Cycle)    
            memAddrArr.append(bina.bin_dec(line[8:16]))

        elif(opcode == "00101"):
            Lines[bina.bin_dec(line[8:16])] = register[line[5:8]] + ' \n'
            F1 = output(F1)
            cycArr.append(Cycle)    
            memAddrArr.append(bina.bin_dec(line[8:16]))

    elif (opcode in registers.opcodes["E"]):
        
        E = True
        F2 = register['111']
        F1 = output(F1)

    elif (opcode in registers.opcodes["F"]):

        F1 = output(F1)
        for l in Lines:
            print(l,end = '')
        plt.scatter(cycArr,memAddrArr)
        plt.xlabel("Cycle")
        plt.ylabel("Memory Address")
        plt.title("Memory Accesses V/S Cycles")
        plt.grid()
        plt.show()
        plt.savefig('plot.png')
        exit(1)

    Cycle +=1
    
    if E:
        PC.update(line,F2)
    else:
        PC.update(line,register["111"])
    
        

        


